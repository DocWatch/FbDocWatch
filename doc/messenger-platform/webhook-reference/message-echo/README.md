#  Message Echo Callback

This callback will occur when a message has been sent by your page. You may
receive ` text ` messsages or messages with attachments ( ` image ` , ` video
` , ` audio ` , ` template ` or ` fallback ` ). The payload will also include
an optional custom ` metadata ` sent by the sender, and the corresponding `
app_id ` .  
You can subscribe to this callback by selecting the ` message_echoes ` field
when [ setting up ](/docs/messenger-platform/webhook-reference#setup) your
webhook.

Multiple types of messages are supported:

  * Text message 
  * Message with image, audio, video or file attachment 
  * Message with template attachment 
  * Message with fallback attachment 

##  Common Format

###  Example

    
    
    {
      "sender":{
        "id":"PAGE_ID"
      },
      "recipient":{
        "id":"USER_ID"
      },
      "timestamp":1457764197627,
      "message":{
        "is_echo":true,
        "app_id":1517776481860111,
        "metadata": "DEVELOPER_DEFINED_METADATA_STRING",
        "mid":"mid.1457764197618:41d102a3e1ae206a38",
        "seq":73,
        ...
      }
    }   

###  Fields

###  ` message ` object

Field Name  |  Description  |  Type  
---|---|---  
  
` is_echo `

|

Indicates the message sent from the page itself

|

Boolean  
  
` app_id `

|

ID of the app from which the message was sent

|

String  
  
` metadata `

|

Custom string passed to the [ Send API ](/docs/messenger-platform/send-api-
reference#request) as the ` metadata ` field

|

String  
  
` mid `

|

Message ID

|

String  
  
` seq `

|

Sequence number

|

Number  
  
` ... `

|

Additional fields specific to the message

|

String  
  
  * ` metadata ` is only present if provided by the sending app 

_ _

##  Text message

###  Example

    
    
    {
      "sender":{
        "id":"PAGE_ID"
      },
      "recipient":{
        "id":"USER_ID"
      },
      "timestamp":1457764197627,
      "message":{
        "is_echo":true,
        "app_id":1517776481860111,
        "metadata": "DEVELOPER_DEFINED_METADATA_STRING",
        "mid":"mid.1457764197618:41d102a3e1ae206a38",
        "seq":73,
        "text":"hello, world!"
      }
    }    

###  Fields

###  ` message ` object

Field Name  |  Description  |  Type  
---|---|---  
  
` text `

|

Text of message

|

String  
  
_ _

##  Message with image, audio, video or file attachment

###  Example

    
    
    {
      "sender":{
        "id":"PAGE_ID"
      },
      "recipient":{
        "id":"USER_ID"
      },
      "timestamp":1458696618268,
      "message":{
        "is_echo":true,
        "app_id":1517776481860111,
        "metadata": "DEVELOPER_DEFINED_METADATA_STRING",
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

###  Fields

###  ` attachments ` object

Field Name  |  Description  |  Type  
---|---|---  
  
` type `

|

Type of attachment: ` image ` , ` audio ` , ` video ` or ` file `

|

String  
  
` payload.url `

|

URL of attachment

|

String  
  
_ _

##  Message with template attachment

###  Example

    
    
    {
      "sender":{
        "id":"PAGE_ID"
      },
      "recipient":{
        "id":"USER_ID"
      },
      "timestamp":1458696618268,
      "message":{
        "is_echo":true,
        "app_id":1517776481860111,
        "metadata": "DEVELOPER_DEFINED_METADATA_STRING",
        "mid":"mid.1458696618141:b4ef9d19ec21086067",
        "seq":51,
        "attachments":[
          {
            "type":"template",
            "payload":{
              "template_type":"button",
              "buttons":[
                {
                  "type":"web_url",
                  "url":"https:\/\/www.messenger.com\/",
                  "title":"Visit Messenger"
                }
              ]
            }
          }
        ]
      }
    }    

###  Fields

###  ` attachments ` object

Field Name  |  Description  |  Type  
---|---|---  
  
` type `

|

` template `

|

String  
  
` payload `

|

Template payload as described in the [ Send API Reference ](/docs/messenger-
platform/send-api-reference#request)

|

String  
  
_ _

##  Message with fallback attachment

A fallback attachment is any attachment not currently recognized or supported
by the Message Echo feature.

###  Example

    
    
    {
      "sender":{
        "id":"PAGE_ID"
      },
      "recipient":{
        "id":"USER_ID"
      },
      "timestamp":1458696618268,
      "message":{
        "is_echo":true,
        "app_id":1517776481860111,
        "metadata": "DEVELOPER_DEFINED_METADATA_STRING",
        "mid":"mid.1458696618141:b4ef9d19ec21086067",
        "seq":51,
        "attachments":[
          {
            "title":"Legacy Attachment",
            "url":"https:\/\/www.messenger.com\/",
            "type":"fallback",
            "payload":null
          }
        ]
      }
    }    

###  Fields

###  ` attachments ` object

Field Name  |  Description  |  Type  
---|---|---  
  
` type `

|

` fallback `

|

String  
  
` title `

|

Title of attachment (optional)

|

String  
  
` url `

|

URL of attachment (optional)

|

String  
  
` payload `

|

Payload of attachment (optional)

|

String  
  
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

