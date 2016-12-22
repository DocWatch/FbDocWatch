#  Quick Replies

Quick Replies provide a new way to present buttons to the user. Quick Replies
appear prominently above the composer, with the keyboard less prominent. When
a quick reply is tapped, the message is sent in the conversation with
developer-defined metadata in the callback. Also, the buttons are dismissed
preventing the issue where users could tap on buttons attached to old messages
in a conversation.

Quick Replies contain text. Optionally, you can add an image.

![](https://scontent.xx.fbcdn.net/t39.2365-6/14175277_1582251242076612_248078259_n.png)

You can also use Quick Replies to prompt a person for their location.

![](https://scontent.xx.fbcdn.net/t39.2365-6/14235551_1274248235927465_1935714581_n.png)

##  Example

###  Text only

    
    
    curl -X POST -H "Content-Type: application/json" -d '{
      "recipient":{
        "id":"USER_ID"
      },
      "message":{
        "text":"Pick a color:",
        "quick_replies":[
          {
            "content_type":"text",
            "title":"Red",
            "payload":"DEVELOPER_DEFINED_PAYLOAD_FOR_PICKING_RED"
          },
          {
            "content_type":"text",
            "title":"Green",
            "payload":"DEVELOPER_DEFINED_PAYLOAD_FOR_PICKING_GREEN"
          }
        ]
      }
    }' "https://graph.facebook.com/v2.6/me/messages?access_token=PAGE_ACCESS_TOKEN"    

###  Text and Image

    
    
    curl -X POST -H "Content-Type: application/json" -d '{
      "recipient":{
        "id":"USER_ID"
      },
      "message":{
        "text":"Pick a color:",
        "quick_replies":[
          {
            "content_type":"text",
            "title":"Red",
            "payload":"DEVELOPER_DEFINED_PAYLOAD_FOR_PICKING_RED",
            "image_url":"http://petersfantastichats.com/img/red.png"
          },
          {
            "content_type":"text",
            "title":"Green",
            "payload":"DEVELOPER_DEFINED_PAYLOAD_FOR_PICKING_GREEN",
            "image_url":"http://petersfantastichats.com/img/green.png"
          }
        ]
      }
    }' "https://graph.facebook.com/v2.6/me/messages?access_token=PAGE_ACCESS_TOKEN"    

###  Location

    
    
    curl -X POST -H "Content-Type: application/json" -d '{
      "recipient":{
        "id":"USER_ID"
      },
      "message":{
        "text":"Please share your location:",
        "quick_replies":[
          {
            "content_type":"location",
          }
        ]
      }
    }' "https://graph.facebook.com/v2.6/me/messages?access_token=PAGE_ACCESS_TOKEN"

##  Fields

###  ` message ` object

Property Name  |  Description  |  Required  
---|---|---  
  
` text `

|

Message text

|

` text ` or ` attachment ` must be set  
  
` attachment `

|

` attachment ` object

|

` text ` or ` attachment ` must be set  
  
` quick_replies `

|

Array of  ` quick_reply ` to be sent with messages

|

N  
  
  * ` quick_replies ` is limited to 11 

###  ` attachment ` object

Property Name  |  Description  |  Required  
---|---|---  
  
` type `

|

Type of attachment, may be ` image ` or ` template `

|

Y  
  
` payload `

|

Payload of attachment

|

Y  
  
Quick Replies work with all message types including text message, image and
template attachments. Please refer to the [ Send API documentation
](/docs/messenger-platform/send-api-reference) for more information on how to
use the ` attachment ` object.

###  ` quick_reply ` object

Property Name  |  Description  |  Type  |  Required  
---|---|---|---  
  
` content_type `

|

` text ` or ` location `

|

String

|

Y  
  
` title `

|

Caption of button

|

String

|

Only if ` content_type ` is ` text `  
  
` payload `

|

Custom data that will be sent back to you via webhook

|

String

|

Only if ` content_type ` is ` text `  
  
` image_url `

|

URL of image for ` text ` quick replies

|

String

|

N  
  
  * ` title ` has a 20 character limit, after that it gets truncated 
  * ` payload ` has a 1000 character limit 
  * If ` content_type ` is ` location ` , ` title ` and ` payload ` are not used 
  * Image for ` image_url ` should be at least 24x24 and will be cropped and resized 

##  Callback

When a Quick Reply is tapped, a text message will be sent to your webhook [
Message Received Callback ](/docs/messenger-platform/webhook-
reference/message-received) . The text of the message will correspond to the
title of the Quick Reply. The message object will also contain a field named `
quick_reply ` containing the ` payload ` data on the Quick Reply.

    
    
    {
      "sender": {
        "id": "USER_ID"
      },
      "recipient": {
        "id": "PAGE_ID"
      },
      "timestamp": 1464990849275,
      "message": {
        "mid": "mid.1464990849238:b9a22a2bcb1de31773",
        "seq": 69,
        "text": "Red",
        "quick_reply": {
          "payload": "DEVELOPER_DEFINED_PAYLOAD_FOR_PICKING_RED"
        }
      }
    }    

When a person shares their location, the callback looks like this:

    
    
    {
      "object": "page",
      "entry": [
        {
          "id": "PAGE_ID",
          "time": 1472672934319,
          "messaging": [
            {
              "sender": {
                "id": "USER_ID"
              },
              "recipient": {
                "id": "PAGE_ID"
              },
              "timestamp": 1472672934259,
              "message": {
                "mid": "mid.1472672934017:db566db5104b5b5c08",
                "seq": 297,
                "attachments": [
                  {
                    "title": "Facebook HQ",
                    "url": "https://www.facebook.com/l.php?u=https%....5-7Ocxrmg",
                    "type": "location",
                    "payload": {
                      "coordinates": {
                        "lat": 37.483872693672,
                        "long": -122.14900441942
                      }
                    }
                  }
                ]
              }
            }
          ]
        }
      ]
    }    

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

