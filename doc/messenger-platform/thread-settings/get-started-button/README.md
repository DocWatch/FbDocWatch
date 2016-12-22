#  Get Started Button

The Welcome Screen can display a ** Get Started ** button. When this button is
tapped, we will trigger the [ postback received callback ](/docs/messenger-
platform/webhook-reference/postback-received) and deliver the person's page-
scoped ID (PSID). You can then present a personalized message to greet the
user or present buttons to prompt him or her to take an action.

![](https://scontent.xx.fbcdn.net/t39.2365-6/14302685_243106819419381_1314180151_n.png)

There are certain conditions to seeing the Welcome Screen and the Get Started
button:

  * They are only rendered the first time the user interacts with a the Page on Messenger 
  * Only admins/developers/testers of the app can see it when the app is in development mode 
  * Your app must be subscribed to [ postbacks on your webhook ](/docs/messenger-platform/webhook-reference/postback-received)

##  Example

    
    
    curl -X POST -H "Content-Type: application/json" -d '{
      "setting_type":"call_to_actions",
      "thread_state":"new_thread",
      "call_to_actions":[
        {
          "payload":"USER_DEFINED_PAYLOAD"
        }
      ]
    }' "https://graph.facebook.com/v2.6/me/thread_settings?access_token=PAGE_ACCESS_TOKEN"      

##  Fields

Property Name  |  Description  |  Required  
---|---|---  
  
` setting_type `

|

Must be ` call_to_actions `

|

Y  
  
` thread_state `

|

Must be ` new_thread `

|

Y  
  
` call_to_actions `

|

Array of ` payload ` strings

|

Y  
  
  * ` call_to_actions ` is limited to 1 
  * ` call_to_actions ` must contain at least one ` payload ` string. This data will be sent back to you via webhook. 

##  Callback

A user tapping the ** Get Started ** button triggers the [ postback received
callback ](/docs/messenger-platform/webhook-reference/postback-received) .

##  Response

If the ** Get Started ** button was successfully set, you will get the
following response:

    
    
    {
      "result": "Successfully added new_thread's CTAs"
    }    

##  Delete

In order to delete the Get Started button send a ` DELETE ` request:

    
    
    curl -X DELETE -H "Content-Type: application/json" -d '{
      "setting_type":"call_to_actions",
      "thread_state":"new_thread"
    }' "https://graph.facebook.com/v2.6/me/thread_settings?access_token=PAGE_ACCESS_TOKEN"    

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

