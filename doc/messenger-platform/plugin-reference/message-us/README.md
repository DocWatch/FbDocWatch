#  Message-Us Plugin

The "Message Us" plugin can be used to immediately start a conversation and
send the person to Messenger. On the desktop web, the user is sent to
messenger.com and on mobile they are sent to the Messenger native app.

![](https://scontent.xx.fbcdn.net/t39.2365-6/13503475_887082391403702_1479658139_n.png)

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

    
    
    <div class="fb-messengermessageus" 
      messenger_app_id="APP_ID" 
      page_id="PAGE_ID"
      color="blue"
      size="standard" >
    </div>    

##  Settings

Setting  |  HTML5 attribute  |  Values  |  Default  
---|---|---|---  
  
` color `

|

` data-color `

|

` blue ` or ` white `

|

` blue `  
  
` size `

|

` data-size `

|

` standard ` , ` large ` or ` xlarge `

|

` large `  
  
##  Callback

This plugin does not trigger a callback to your webhook. However, you will
receive a [ message callback ](/docs/messenger-platform/webhook-
reference/message) when the user sends a message to the page.

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

