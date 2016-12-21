#!/usr/bin/env python3
# vim: fileencoding=utf-8 tw=100 expandtab ts=4 sw=4 :

from urllib.parse import urljoin
from bs4 import BeautifulSoup
from selenium import webdriver
from os import path as ospath, makedirs
from html2text import html2text


BASE_URL = 'https://developers.facebook.com/docs/'

FB_DOC_ROOTS = [
    'messenger-platform',
]

PHANTOM_PATH = '/home/remy/.nvm/versions/node/v5.11.1/bin/phantomjs'


class DocFetcher(object):
    def __init__(self, doc_root):
        self.driver = webdriver.PhantomJS(PHANTOM_PATH)
        self.driver.set_window_size(1600, 900)
        self.doc_root = doc_root

    def _exec(self, *args, **kwargs):
        return self.driver.execute_script(*args, **kwargs)

    def fetch_component(self, component):
        full_url = urljoin(BASE_URL, component)
        self.driver.get(full_url)
        menu_src = self.driver.execute_script(
            '''return document.querySelector('#documentation_primary_nav_pagelet').innerHTML;'''
        )
        soup = BeautifulSoup(menu_src, "html.parser")
        links = soup.find_all('a')
        out = []
        title = ''

        for link in links:
            try:
                node = '/docs/{}/'.format(component)
                if link['href'].startswith(node):
                    topic = link['href'][len(node):]
                    out.append((topic, link.text))
                elif link['href'] == '/docs/{}'.format(component):
                    title = link.text
            except (KeyError, ValueError):
                pass

        return title, out

    def render_component(self, title, links):
        out = [
            '# {}'.format(title),
            '',
        ]

        for topic, label in links:
            out.append('- [{title}]({url})'.format(
                title=label,
                url=topic,
            ))

        out.append('')
        return '\n'.join(out)

    def fetch_topic(self, component, topic):
        def cleanup():
            self._exec('''
                document.querySelector('#developer_documentation_toolbar').remove();
                document.querySelector('.fb_iframe_widget').remove();
            ''')

        url = urljoin(BASE_URL, '{component}/{topic}'.format(
            component=component,
            topic=topic,
        ))
        self.driver.get(url)
        cleanup()
        return self.driver.execute_script(
            '''return document.querySelector('#documentation_body_pagelet').innerHTML;'''
        )

    def render_topic(self, topic_src):
        return html2text(topic_src)

    def handle_component(self, component):
        title, links = self.fetch_component(component)
        self._save(self.render_component(title, links), component)

        for topic, title in links:
            print('---> {}'.format(topic))
            src = self.fetch_topic(component, topic)
            self._save(self.render_topic(src), component, topic)

    def _save(self, content, *args):
        path = ospath.join(self.doc_root, *(args + ('README.md',)))
        makedirs(ospath.dirname(path), exist_ok=True)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)


def main():
    cwd = ospath.dirname(__file__)
    doc_dir = ospath.join(cwd, 'doc')
    fetcher = DocFetcher(doc_dir)

    for root in FB_DOC_ROOTS:
        print('=> {}'.format(root))
        fetcher.handle_component(root)


if __name__ == '__main__':
    main()
