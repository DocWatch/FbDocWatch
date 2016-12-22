#  Greeting Text

You can set a greeting for new conversations. This can be used to communicate
your bot's functionality. If the greeting text is not set, the page
description will be shown in the welcome screen. You can personalize the text
with the person's name.

![](https://scontent.xx.fbcdn.net/t39.2365-6/14287888_188235318253964_1078929636_n.png)

The Greeting Text is only rendered the first time the user interacts with a
the Page on Messenger.

##  Example

###  Adding

    
    
    curl -X POST -H "Content-Type: application/json" -d '{
      "setting_type":"greeting",
      "greeting":{
        "text":"Timeless apparel for the masses."
      }
    }' "https://graph.facebook.com/v2.6/me/thread_settings?access_token=PAGE_ACCESS_TOKEN"    

###  Removing

    
    
    curl -X DELETE -H "Content-Type: application/json" -d '{
      "setting_type":"greeting"
    }' "https://graph.facebook.com/v2.6/me/thread_settings?access_token=PAGE_ACCESS_TOKEN"   
        

##  Fields

Property Name  |  Description  |  Required  
---|---|---  
  
` setting_type `

|

Must be ` greeting `

|

Y  
  
` greeting.text `

|

Greeting text

|

Y  
  
  * ` greeting.text ` must be UTF-8 and has a 160 character limit 

##  Personalization

You can personalize the greeting text using the person's name. You can use the
following template strings:

  * ` {{user_first_name}} `
  * ` {{user_last_name}} `
  * ` {{user_full_name}} `

###  Example

    
    
    curl -X POST -H "Content-Type: application/json" -d '{
      "setting_type":"greeting",
      "greeting":{
        "text":"Hi {{user_first_name}}, welcome to this bot."
      }
    }' "https://graph.facebook.com/v2.6/me/thread_settings?access_token=PAGE_ACCESS_TOKEN"    

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

