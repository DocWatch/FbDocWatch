#  Generic Template

Use the Generic Template with the [ Send API ](/docs/messenger-platform/send-
api-reference#request) to send a horizontal scrollable carousel of items, each
composed of an image attachment, short description and buttons to request
input from the user.

![](https://scontent.xx.fbcdn.net/t39.2365-6/13509251_1026555627430343_1803381600_n.png)

Buttons on templates can do the following:

  * open a URL 
  * make a postback to your [ webhook ](/docs/graph-api/webhooks)
  * call a phone number 
  * open a share dialog 
  * open a payment dialog 
  * and more, see [ Buttons ](/docs/messenger-platform/send-api-reference/buttons)

Read more details about [ message buttons ](/docs/messenger-platform/send-api-
reference/message-buttons) .

##  Example

    
    
    curl -X POST -H "Content-Type: application/json" -d '{
      "recipient":{
        "id":"USER_ID"
      },
      "message":{
        "attachment":{
          "type":"template",
          "payload":{
            "template_type":"generic",
            "elements":[
               {
                "title":"Welcome to Peter\'s Hats",
                "image_url":"https://petersfancybrownhats.com/company_image.png",
                "subtitle":"We\'ve got the right hat for everyone.",
                "default_action": {
                  "type": "web_url",
                  "url": "https://peterssendreceiveapp.ngrok.io/view?item=103",
                  "messenger_extensions": true,
                  "webview_height_ratio": "tall",
                  "fallback_url": "https://peterssendreceiveapp.ngrok.io/"
                },
                "buttons":[
                  {
                    "type":"web_url",
                    "url":"https://petersfancybrownhats.com",
                    "title":"View Website"
                  },{
                    "type":"postback",
                    "title":"Start Chatting",
                    "payload":"DEVELOPER_DEFINED_PAYLOAD"
                  }              
                ]      
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

` payload ` of generic template

|

Y  
  
###  ` payload ` object

Property Name  |  Description  |  Type  |  Required  
---|---|---|---  
  
` template_type `

|

Value must be ` generic `

|

String

|

Y  
  
` elements `

|

Data for each bubble in message

|

Array of  ` element `

|

Y  
  
  * ` elements ` is limited to 10 

###  ` element ` object

Property Name  |  Description  |  Type  |  Required  
---|---|---|---  
  
` title `

|

Bubble title

|

String

|

Y  
  
` subtitle `

|

Bubble subtitle

|

String

|

N  
  
` image_url `

|

Bubble image

|

String

|

N  
  
` default_action `

|

Default action to be triggered when user taps on the element

|

Object

|

N  
  
` buttons `

|

Set of buttons that appear as call-to-actions

|

Array of  ` button `

|

N  
  
  * ` title ` has a 80 character limit 
  * ` subtitle ` has a 80 character limit 
  * ` buttons ` is limited to 3 
  * Image ratio is 1.91:1 

###  ` default_action ` object

The ` default_action ` behaves like a [ URL Button ](/docs/messenger-
platform/send-api-reference/url-button#fields) and contains the same fields
except that the ` title ` field is not needed.

###  ` button ` object

See the [ Message Buttons reference doc ](/docs/messenger-platform/send-api-
reference/message-buttons#fields) for details on the ` button ` object.

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

