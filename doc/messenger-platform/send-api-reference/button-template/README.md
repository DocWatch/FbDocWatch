#  Button Template

Use the Button Template with the [ Send API ](/docs/messenger-platform/send-
api-reference#request) to send a text and buttons attachment to request input
from the user. The buttons can open a URL, or make a back-end call to your [
webhook ](/docs/graph-api/webhooks) .

![](https://scontent.xx.fbcdn.net/t39.2365-6/13509162_1732711383655205_1306472501_n.png)

##  Example

    
    
    curl -X POST -H "Content-Type: application/json" -d '{
      "recipient":{
        "id":"USER_ID"
      },
      "message":{
        "attachment":{
          "type":"template",
          "payload":{
            "template_type":"button",
            "text":"What do you want to do next?",
            "buttons":[
              {
                "type":"web_url",
                "url":"https://petersapparel.parseapp.com",
                "title":"Show Website"
              },
              {
                "type":"postback",
                "title":"Start Chatting",
                "payload":"USER_DEFINED_PAYLOAD"
              }
            ]
          }
        }
      }
    }' "https://graph.facebook.com/v2.6/me/messages?access_token=PAGE_ACCESS_TOKEN"    

##  Fields

###  ` attachment ` object

Property Name  |  Description  |  Required  
---|---|---  
  
` type `

|

Value must be ` template `

|

Y  
  
` payload `

|

` payload ` of button template

|

Y  
  
###  ` payload ` object

Property Name  |  Description  |  Type  |  Required  
---|---|---|---  
  
` template_type `

|

Value must be ` button `

|

String

|

Y  
  
` text `

|

UTF-8 encoded text of up to 320 characters that appears the in main body

|

String

|

Y  
  
` buttons `

|

Set of, one to three, buttons that appear as call-to-actions

|

Array of  ` button `

|

Y  
  
###  ` button ` object

See the [ Message Buttons reference doc ](/docs/messenger-platform/send-api-
reference/message-buttons) for details on the ` button ` object.

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

