#  Checkbox Plugin

The Checkbox Plugin allows you to authenticate people with Messenger and start
a thread using your website. It's similar to the "Send to Messenger" plugin,
but optimized for forms where you want to provide a seamless way for people to
receive updates via Messenger.

It could be used for just about any form-based flow on a site, including
ecommerce websites where you wish to send receipts and order updates to the
user, for event RSVPs, or even signup forms.

  1. How it Works 
  2. Implementation 
  3. Troubleshooting Tips 

##  How It Works

![](https://scontent.xx.fbcdn.net/t39.2365-6/13679808_631224743722018_2016203957_n.png)

The Checkbox Plugin enables you to integrate authentication into a user flow
on your website. It has a checkbox that fits naturally with existing forms.

![](https://scontent.xx.fbcdn.net/t39.2365-6/13720713_251812788545065_1757191617_n.png)

When a person is logged into Facebook in their browser, their session will be
detected and their name and profile picture will be shown beneath the
checkbox. This lets the user know which identity will be opted into
communication with the business if they proceed.

If the identity displayed isn't the person using the site, they can click the
"Not you?" link to log out. It will clear the active Facebook session and
present a login dialog.

###  Customizing Default State

The default state can be set at render-time to make it either an opt-in or
opt-out experience.

![](https://scontent.xx.fbcdn.net/t39.2365-6/13679808_631224743722018_2016203957_n.png)

###  Customizing Login Behavior

If there is no logged in Facebook user, the plugin will be rendered without a
user identity displayed. Clicking in the checkbox will prompt the user to log
in.

![](https://scontent.xx.fbcdn.net/t39.2365-6/14606901_357573287918916_6893617724933537792_n.png)

If you set ` allow_login ` to false, then the plugin will not render for users
who are not logged in. For users with an active Facebook session, the plugin
will render without the 'Not you?' link.

_ _

##  Implementation

The Facebook JavaScript SDK is required to render the Checkbox plugin.
Subscribe to an event to get the state of the checkbox. Confirm the opt-in by
triggering a client-side event using a [ Facebook App Event ](/docs/app-
events) .

The web plugin takes a ` user_ref ` parameter which is used as an identifier
for the user. When the user finishes the flow, we will pass this identifier
back to you to identify the user. This parameter should be unique not just for
every user, but for every time the plugin is rendered. If the parameter is not
unique, then the plugin may not render.

###  Whitelist your domain

For security reasons, the plugin will render only when loaded on a domain that
you have whitelisted. Refer to this [ reference doc ](/docs/messenger-
platform/thread-settings/domain-whitelisting) to learn how to whitelist your
domain. Once you have whitelisted the domain, you can set it as value for the
plugin ` origin ` parameter.

###  Render the Plugin

Add the plugin to your page by loading the Facebook JavaScript SDK and adding
a ` div ` with the attributes below.

    
    
    <script>
     window.fbAsyncInit = function() {
        FB.init({
          appId      : 'APP_ID',
          xfbml      : true,
          version    : 'v2.6'
        });
    
      };
    
      (function(d, s, id){
        var js, fjs = d.getElementsByTagName(s)[0];
          if (d.getElementById(id)) {return;}
          js = d.createElement(s); js.id = id;
          js.src = "//connect.facebook.net/en_US/sdk.js";
          fjs.parentNode.insertBefore(js, fjs);
        }(document, 'script', 'facebook-jssdk')
      );
    </script>      
          
    <div class="fb-messenger-checkbox"  
      origin=PAGE_URL
      page_id=PAGE_ID
      messenger_app_id=APP_ID
      user_ref="UNIQUE_REF_PARAM" 
      prechecked="true" 
      allow_login="true" 
      size="large"></div>      

####  Field descriptions

Parameter  |  Description  |  Type  |  Required  
---|---|---|---  
  
` class `

|

Value must be ` fb-messenger-checkbox `

|

String

|

Y  
  
` origin `

|

Base domain of the URL where the plugin is loaded.

|

URL

|

Y  
  
` page_id `

|

Page ID

|

Number

|

Y  
  
` messenger_app_id `

|

App ID

|

Number

|

Y  
  
` user_ref `

|

Unique parameter for referencing a user

|

String

|

Y  
  
` prechecked `

|

Setting to precheck the checkbox

|

Boolean

|

N, default is ` true `  
  
` allow_login `

|

Enables people to login if no existing session is present. Also enables the
'Not You' option.

|

Boolean

|

N, default is ` true `  
  
` size `

|

Size of plugin

|

Enum value ( ` small ` , ` medium ` , ` large ` , ` standard ` , ` xlarge ` )

|

N, default is ` large `  
  
When your app is in [ Development Mode ](/docs/apps/managing-development-
cycle) , plugin and API functionality will only work for admins, developers
and testers of the app. After your app is approved and public, it will work
for the general public. This includes rendering with the ` allow_login `
option set to ` true ` , where the plugin will render without a Facebook
session only if the app is approved and public.

###  Check the state of the checkbox

You can subscribe to client-side events to check the state of the checkbox.

    
    
      window.fbAsyncInit = function() {
        FB.init({
          appId      : '197650983945848',
          xfbml      : true,
          version    : 'v2.6'
        });
    
        FB.Event.subscribe('messenger_checkbox', function(e) {
          console.log("messenger_checkbox event");
          console.log(e);
          
          if (e.event == 'rendered') {
            console.log("Plugin was rendered");
          } else if (e.event == 'checkbox') {
            var checkboxState = e.state;
            console.log("Checkbox state: " + checkboxState);
          } else if (e.event == 'not_you') {
            console.log("User clicked 'not you'");
          } else if (e.event == 'hidden') {
            console.log("Plugin was hidden");
          }
          
        });
      }; 

###  Confirming Opt-in

When the form is about to be submitted, or when the flow is otherwise done,
you must send a ` MessengerCheckboxUserConfirmation ` event. It is not
required to verify the state of the checkbox before doing so.

The sample code below uses the [ AppEvents ](/docs/app-events) function to
call to confirm the opt-in.

You may pass an optional ` ref ` parameter if you wish to include additional
context to be passed back in the webhook event. It has the same behavior as
for the [ Send To Messenger plugin ](/docs/messenger-platform/plugin-
reference/send-to-messenger) (as distinct from ` user_ref ` ).

    
    
    <html>
      <head>
        <script>
            function confirmOptIn() {
              FB.AppEvents.logEvent('MessengerCheckboxUserConfirmation', null, {
                'app_id':'APP_ID',
                'page_id':'PAGE_ID',
                'ref':'PASS_THROUGH_PARAM',
                'user_ref':'UNIQUE_REF_PARAM'
              });
          }
        </script>
      </head>
    
      <body>
        <input type="button" onclick="confirmOptIn()" value="Confirm Opt-in"/>
      </body>
    
    </html>        

###  Callback

After the opt-in event, we will post a webhook event to your server if the
checkbox state was checked. This callback has the same format as the [ opt-in
callback ](/docs/messenger-platform/webhook-reference/optins) , but instead of
a ` sender ` field, it has an ` optin ` object with a ` user_ref ` field.

    
    
    {
      "recipient":{
        "id":"PAGE_ID"
      },
      "timestamp":1234567890,
      "optin":{
        "ref":"PASS_THROUGH_PARAM",
        "user_ref":"UNIQUE_REF_PARAM"
      }
    }    

###  Calling the Send API

After you receive the callback event, you can call the [ Send API
](/docs/messenger-platform/send-api-reference) to start messaging the user
using the ` user_ref ` identifier in ` recipient ` as shown below. Note that
this field is the same as the unique user_ref param used before when the
plugin was rendered and in confirming the opt-in.

If the call to the [ Send API ](/docs/messenger-platform/send-api-reference)
is successful, the response will contain a ` recipient_id ` parameter, which
is a stable user ID that you can now use in future API calls.

    
    
    curl -X POST -H "Content-Type: application/json" -d '{
      "recipient": {
        "user_ref":"UNIQUE_REF_PARAM"
      }, 
      "message": {
        "text":"hello, world!"
      }
    }' "https://graph.facebook.com/me/messages?access_token=PAGE_ACCESS_TOKEN" 

_ _

##  Troubleshooting Tips

If you're having trouble getting the plugin to properly render, try the tips
below:

  1. Verify that your app is actually approved for the ` pages_messaging ` permission. 
  2. Verify that your page has webhook subscription to your app. 
  3. If you see a console error like "Refused to display *** in a frame because an ancestor violates the following Content Security Policy directive: ***", check that the domain of the page the plugin is being rendered on [ has been whitelisted ](/docs/messenger-platform/thread-settings/domain-whitelisting) . 
  4. If the ` allow_login ` parameter is set to false, you will need to have a valid Facebook user session (i.e. not logged in as a page) otherwise the plugin will be hidden. 

_ _

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

