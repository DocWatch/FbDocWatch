#!/usr/bin/env python3
# vim: fileencoding=utf-8 tw=100 expandtab ts=4 sw=4 :

from urllib.parse import urljoin
from bs4 import BeautifulSoup
from selenium import webdriver
from os import path as ospath, makedirs, getenv
from html2text import html2text
from queue import Queue
import posixpath


BASE_URL = 'https://developers.facebook.com/docs/'

FB_DOC_ROOTS = [
    'messenger-platform',
]

PHANTOM_JS_PATH = getenv('PHANTOM_JS_PATH', 'phantomjs')


def drop_prefix(string: str, prefix: str) -> str:
    """
    Drop the prefix before the string if the strings begins with that prefix.

    :param string: String to be trimmed
    :param prefix: Prefix to look for
    :return: The string, trimmed if necessary
    """

    if string.startswith(prefix):
        return string[len(prefix):]
    return string


def clean_url(url: str, base: str) -> str:
    """
    Clean a URL: given the specified base, transform the URL into a relative URL and drop the
    anchor.

    :param url: URL to make relative
    :param base: Base URL to consider
    :return:
    """

    url = urljoin(base, url).split('#')[0]
    if url.startswith(base):
        return drop_prefix(url, base).lstrip('/'), True
    else:
        return url, False


class DocFetcher(object):
    def __init__(self, doc_root):
        self.driver = webdriver.PhantomJS(PHANTOM_JS_PATH)
        self.driver.set_window_size(1600, 900)
        self.doc_root = doc_root
        self.queue = Queue()
        self.seen = set()

    def _exec(self, *args, **kwargs):
        return self.driver.execute_script(*args, **kwargs)

    def _enqueue(self, topic):
        if topic not in self.seen:
            self.seen.add(topic)
            self.queue.put(topic)

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

    def fetch_topic(self, topic):
        def cleanup():
            self._exec('''(function() {
                function drop(selector) {
                    var el = document.querySelector(selector);
                    if (el) {
                        el.remove();
                    }
                }

                drop('#developer_documentation_toolbar');
                drop('.fb_iframe_widget');
                drop('img[width="1"]');
            }())''')

        url = urljoin(BASE_URL, topic)
        self.driver.get(url)
        cleanup()
        src = self.driver.execute_script(
            '''return document.querySelector('#documentation_body_pagelet').innerHTML;'''
        )
        soup = BeautifulSoup(src, 'html.parser')

        links = soup.find_all('a')
        for link in links:
            try:
                link_url, is_rel = clean_url(link['href'], url)

                if is_rel and link_url:
                    link['href'] = link_url
                    self._enqueue(posixpath.join(topic, link_url))
            except KeyError:
                pass

        return soup.prettify()

    def render_topic(self, topic_src):
        return html2text(topic_src)

    def handle_component(self, component):
        title, links = self.fetch_component(component)
        self._save(self.render_component(title, links), component)

        for topic, title in links:
            self.queue.put(component + '/' + topic)

        while not self.queue.empty():
            topic = self.queue.get()
            print('---> {}'.format(topic))
            src = self.fetch_topic(topic)
            self._save(self.render_topic(src), topic)

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
