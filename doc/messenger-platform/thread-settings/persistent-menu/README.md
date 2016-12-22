#  Persistent Menu

The Persistent Menu is a menu that is always available to the user. This menu
should contain top-level actions that users can enact at any point. Having a
persistent menu easily communicates the basic capabilities of your bot for
first-time and returning users.  
The menu can be invoked by a user, by tapping on the 3-caret icon on the left
of the composer.

![](https://scontent.xx.fbcdn.net/t39.2365-6/13509228_581512925362726_878211705_n.png)

##  Example

    
    
    curl -X POST -H "Content-Type: application/json" -d '{
      "setting_type" : "call_to_actions",
      "thread_state" : "existing_thread",
      "call_to_actions":[
        {
          "type":"postback",
          "title":"Help",
          "payload":"DEVELOPER_DEFINED_PAYLOAD_FOR_HELP"
        },
        {
          "type":"postback",
          "title":"Start a New Order",
          "payload":"DEVELOPER_DEFINED_PAYLOAD_FOR_START_ORDER"
        },
        {
          "type":"web_url",
          "title":"Checkout",
          "url":"http://petersapparel.parseapp.com/checkout",
          "webview_height_ratio": "full",
          "messenger_extensions": true
        },
        {
          "type":"web_url",
          "title":"View Website",
          "url":"http://petersapparel.parseapp.com/"
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

Must be ` existing_thread `

|

Y  
  
` call_to_actions `

|

Array of  ` menu_item ` object

|

Y  
  
  * ` call_to_actions ` is limited to 5 

Menus are loaded from cache but updates are fetched each time they're loaded.
If you update the menu, trigger the fetch by loading it and then load it again
to see your changes.

###  ` menu_item ` object

Property Name  |  Description  |  Type  |  Required  
---|---|---|---  
  
` type `

|

Value is ` web_url ` or ` postback `

|

String

|

Y  
  
` title `

|

Button title

|

String

|

Y  
  
` url `

|

For ` web_url ` buttons, this URL is opened in a mobile browser when the
button is tapped

|

String

|

Y, if type is ` web_url `  
  
` payload `

|

For ` postback ` buttons, this data will be sent back to you via webhook

|

String

|

Y, if type is ` postback `  
  
` webview_height_ratio `

|

Height of the [ Webview ](/docs/messenger-platform/send-api-reference/webview)
. Valid values: ` compact ` , ` tall ` , ` full ` .

|

Enum

|

N  
  
` messenger_extensions `

|

Must be ` true ` if using [ Messenger Extensions ](/docs/messenger-
platform/send-api-reference/webview) .

|

Boolean

|

N  
  
  * ` title ` has a 30 character limit 
  * ` payload ` has a 1000 character limit 

##  Response

If the Persistent Menu was successfully set, you will get the following
response:

    
    
    {
      "result": "Successfully added new_thread's CTAs"
    }    

##  Delete

In order to delete the Psersistent Menu send a ` DELETE ` request:

    
    
    curl -X DELETE -H "Content-Type: application/json" -d '{
      "setting_type":"call_to_actions",
      "thread_state":"existing_thread"
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

