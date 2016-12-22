#  Send-to-Messenger Plugin

The "Send to Messenger" plugin is used to trigger an authentication event to
your webhook. You can pass in data to know which user and transaction was tied
to the authentication event, and link the user on your back-end.

![](https://scontent.xx.fbcdn.net/t39.2365-6/13571135_580861125428370_932811201_n.png)

The first time a person clicks on this button, a confirmation popup will be
presented.

![](https://scontent.xx.fbcdn.net/t39.2365-6/13480198_492903457574570_396748231_n.png)

When your app is in development mode, the plugin is only visible to admins,
developers and testers of the app. In development mode, the plugin will not be
visible if there isn't an active session.

##  Setup

    
    
    <body>
      <script>
    
        window.fbAsyncInit = function() {
          FB.init({
            appId: "APP_ID",
            xfbml: true,
            version: "v2.6"
          });
    
        };
    
        (function(d, s, id){
           var js, fjs = d.getElementsByTagName(s)[0];
           if (d.getElementById(id)) { return; }
           js = d.createElement(s); js.id = id;
           js.src = "//connect.facebook.net/en_US/sdk.js";
           fjs.parentNode.insertBefore(js, fjs);
        }(document, 'script', 'facebook-jssdk'));
    
      </script>
    
    ...    

##  Plugin Code

    
    
    <div class="fb-send-to-messenger" 
      messenger_app_id="APP_ID" 
      page_id="PAGE_ID" 
      data-ref="PASS_THROUGH_PARAM" 
      color="blue" 
      size="standard">
    </div>    

##  Settings

Parameter  |  Description  |  Type  |  Required  
---|---|---|---  
  
` color `

|

Color of the button

|

Enum ( ` blue ` , ` white ` )

|

N, default is ` blue `  
  
` size `

|

Size of the plugin

|

Enum ( ` standard ` , ` large ` , ` xlarge ` )

|

N, default is ` large `  
  
` data-ref `

|

Custom state parameter. It should be encoded and encrypted for security
purposes.

|

String of max 250 characters. Valid characters are ` a-z A-Z 0-9 +/=-.:_ `

|

N  
  
` enforce_login `

|

If ` true ` , logged-in users must login again when clicking the button.

|

boolean

|

N, default is ` false `  
  
Use the ` data-ref ` param to pass state with the authentication. If you
surface the plugin in multiple places, you may want to modify the state based
on the place where the plugin is shown.

##  Event Subscription

Subscribe to plugin events.

    
    
    <script>
    
      FB.Event.subscribe('send_to_messenger', function(e) {
        // callback for events triggered by the plugin
      
      });
    
    </script>

###  Event Fields

Field Name  |  Type  |  Description  
---|---|---  
  
` event `

|

Enum

|

Name of event. Possible values: ` rendered ` , ` clicked ` , ` not_you ` .  
  
` ref `

|

String

|

Contains the value set on the ` data-ref ` param on the plugin.  
  
` is_after_optin `

|

Boolean

|

Indicates whether event happened after the confirmation pop-up was confirmed.  
  
` pluginID `

|

undefined

|

This field is not used.  
  
##  Callback

This triggers the [ opt-in callback ](/docs/messenger-platform/webhook-
reference/optins) .

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

