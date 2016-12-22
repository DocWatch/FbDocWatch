#  Message Received Callback

This callback will occur when a message has been sent to your page. You may
receive text messages or messages with attachments (image, audio, video, file
or location). Callbacks contain a ` seq ` number which can be used to know the
sequence of a message in a conversation. Messages are always sent in order.

You can subscribe to this callback by selecting the ` message ` field when [
setting up ](/docs/messenger-platform/webhook-reference#setup) your webhook.

##  Examples

###  Text Message

    
    
    {
      "sender":{
        "id":"USER_ID"
      },
      "recipient":{
        "id":"PAGE_ID"
      },
      "timestamp":1458692752478,
      "message":{
        "mid":"mid.1457764197618:41d102a3e1ae206a38",
        "seq":73,
        "text":"hello, world!",
        "quick_reply": {
          "payload": "DEVELOPER_DEFINED_PAYLOAD"
        }
      }
    }    

###  Message with image attachment

    
    
    {
      "sender":{
        "id":"USER_ID"
      },
      "recipient":{
        "id":"PAGE_ID"
      },
      "timestamp":1458692752478,
      "message":{
        "mid":"mid.1458696618141:b4ef9d19ec21086067",
        "seq":51,
        "attachments":[
          {
            "type":"image",
            "payload":{
              "url":"IMAGE_URL"
            }
          }
        ]
      }
    }    

##  Fields

###  ` message ` object

Field Name  |  Description  |  Type  
---|---|---  
  
` mid `

|

Message ID

|

String  
  
` seq `

|

Message sequence number

|

Number  
  
` text `

|

Text of message

|

String  
  
` attachments `

|

Array containing attachment data

|

Array of  ` attachment `  
  
` quick_reply `

|

Optional custom data provided by the sending app

|

` quick_reply `  
  
###  ` attachment ` object

Property Name  |  Description  |  Type  
---|---|---  
  
` type `

|

` image ` , ` audio ` , ` video ` , ` file ` or ` location `

|

String  
  
` payload `

|

` multimedia ` or  ` location ` payload

|

String  
  
###  ` quick_reply ` object

Property Name  |  Description  |  Type  
---|---|---  
  
` payload `

|

Custom data provided by the app

|

String  
  
A ` quick_reply ` payload is only provided with a text message when the user
tap on a [ Quick Replies ](/docs/messenger-platform/send-api-reference/quick-
replies) button.

###  ` image ` , ` audio ` , ` video ` or ` file ` payload

Property Name  |  Description  |  Type  
---|---|---  
  
` url `

|

URL of the file

|

String  
  
###  ` location ` payload

Property Name  |  Description  |  Type  
---|---|---  
  
` coordinates.lat `

|

Latitude

|

Number  
  
` coordinates.long `

|

Longitude

|

Number  
  
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

