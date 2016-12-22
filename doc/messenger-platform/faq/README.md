#  Messenger Platform Technical FAQ

##  Webhooks

Why am I not receiving a callback to my webhook?

There are 2 steps to receiving callbacks. First, make sure your webhook is
setup properly (https://developers.facebook.com/docs/messenger-
platform/webhook-reference#setup). There is an indicator when webhooks are
properly setup.

Second, you must subscribe to each page. All pages that are subscribed to will
be listed.

![](https://scontent.xx.fbcdn.net/t39.2365-6/13695315_1141730795884980_248654944_n.png)

If calls to your webhook [ fail for an extended period of time
](https://developers.facebook.com/docs/messenger-platform/webhook-
reference#unsubscribe) , your app will be unsubscribed and you will have to
re-add your webhook and re-subscribe your page.

_ Was this answer helpful?  _ _ Yes  _ _ No  _

Permalink

How do I verify that the webhook call is coming from Facebook for security
reasons?

Calls to the webhook contain a field in the header named [ X-Hub-Signature
](https://developers.facebook.com/docs/messenger-platform/webhook-
reference#security) , which can be used to validate that the call came from
Facebook.

_ Was this answer helpful?  _ _ Yes  _ _ No  _

Permalink

Why do I keep on getting developer alerts that my webhook has not been
accepting updates, or keep getting the same webhook calls repeatedly?

Make sure your webhook is [ responding with a status code of 200
](https://developers.facebook.com/docs/messenger-platform/webhook-
reference#response) . This communicates to us that the webhook was
successfully received. If you do not return a 200, we will retry the call
until successfully completed. Also, if a webhook doesn't return a 200 for an
extended period of time, we will surface developer alerts.

Also, note that a successful status code is returned in a timely manner. A
webhook call with timeout after 20 seconds. Be sure to architecture your code
such that webhooks are processed asynchronously so that a successful status
code can be returned immediately and processed separately.

_ Was this answer helpful?  _ _ Yes  _ _ No  _

Permalink

  

##  Entry points

How do I link a plugin click or my user account to a thread?

When using the [ “Send to Messenger” Plugin
](https://developers.facebook.com/docs/messenger-platform/plugin-
reference/send-to-messenger) , the ** data-ref ** parameter can be used by you
as a pass-through-parameter to send through any information regarding the
context of the click.

People may also discover your page through search in Messenger. In these
cases, you won't have a pass-through-parameter. You can use the [ account
linking feature ](https://developers.facebook.com/docs/messenger-
platform/account-linking) to associate a thread to a user account on your
site.

_ Was this answer helpful?  _ _ Yes  _ _ No  _

Permalink

How come I can't see the "Send to Messenger" plugin?

When an app is in [ development mode ](/docs/apps/managing-development-cycle)
only admins, developers and testers of the app are able to view the plugin.
After the app is reviewed and approved, you make the app available to the
public in the [ App Review tab in the App Dashboard ](/docs/messenger-
platform/app-review) .

_ Was this answer helpful?  _ _ Yes  _ _ No  _

Permalink

  

##  Send/Receive API

Why do I get an "Invalid ID" or "No matching user found" error when sending a
message?

There are multiple reasons why this may happen:

  * ** You're using an ID from Facebook Login. ** User IDs from Facebook Login are not intended to work with the Send/Receive API. Only user IDs obtained through authentication with the Messenger Platform will [ work with the Messenger Platform ](https://developers.facebook.com/docs/messenger-platform/send-api-reference#request) . 

  * ** You're using an ID with the incorrect Page Access Token. ** User IDs for the Messenger Platform are scoped to a page and, therefore, are page specific. If you use a valid user ID but with a page access token that's associated with a different page, the call will not work. Be sure to use the user ID and page access token associated with the same page. 

  * ** You're sending to a phone number that hasn't been recently verified. ** When using the Send API with a phone number, we will only send messages if the [ phone number has been ** recently ** verified ](https://developers.facebook.com/docs/messenger-platform/send-api-reference#phone_number) . Even if the phone number is shown as verified, but has not been recently verified, then the send may fail. Re-verify your phone number and wait 24 hours until trying again. 

_ Was this answer helpful?  _ _ Yes  _ _ No  _

Permalink

Why can't I send messages to test platform users?

Here is a workaround to use a platform test user for your messenger platform
integration:

  1. From your app's [ Roles page ](https://developers.facebook.com/apps/89000000000000/roles/test-users/) , create a new test user by clicking the Add button. 
  2. Toggle the ** Authorize Test Users for This App? ** option and grant permissions _ "manage_pages" _ and _ "page_messaging" _ . 
  3. Use the Edit Button and get an access token for this user (using v2.6). Please save this for later. 
  4. Use the ** Edit ** button to login as the test user. 
  5. After logging in, create a page as the test user. 
  6. Use the user access token for the test user to get the page access token for this user. You can do this with the following call: 
    
        https://graph.facebook.com/v2.6/me/accounts?access_token=[TEST_USER_ACCESS_TOKEN]

( [ Documentation ](https://developers.facebook.com/docs/graph-
api/reference/user/accounts/) )

  7. Use this page access token to link your Facebook Application with your Page: 
    
        https://graph.facebook.com/v2.6/me/subscribed_apps?method=POST&access_token=[TEST_USER_PAGE_ACCESS_TOKEN]
            

( [ Documentation ](https://developers.facebook.com/docs/messenger-
platform/implementation#subscribe_app_pages) )

  8. After you have followed these steps you will receive RTU updates to your Test Page and be able to message your Test User from your Test Page. In addition to the above you can replace your access token with a long-lived token if they are expiring too quickly for your tests. Please follow the documentation [ here ](https://developers.facebook.com/docs/facebook-login/access-tokens/expiration-and-extension) : 
    
        GET /oauth/access_token?  
        grant_type=fb_exchange_token&           
        client_id={app-id}&
        client_secret={app-secret}&
        fb_exchange_token={short-lived-token} 
            

_ Was this answer helpful?  _ _ Yes  _ _ No  _

Permalink

  

_ _

&lt;img height="1" width="1" alt="" style="display:none"
src="https://www.facebook.com/tr?id=675141479195042&amp;amp;ev=PixelInitialized"
/&gt; &lt;img height="1" width="1" alt="" style="display:none"
src="https://www.facebook.com/tr?id=574561515946252&amp;amp;ev=PixelInitialized"
/&gt; &lt;img height="1" width="1" alt="" style="display:none"
src="https://www.facebook.com/tr?id=1668333663438923&amp;amp;ev=PixelInitialized"
/&gt; &lt;img height="1" width="1" alt="" style="display:none"
src="https://www.facebook.com/tr?id=1754628768090156&amp;amp;ev=PixelInitialized"
/&gt;

