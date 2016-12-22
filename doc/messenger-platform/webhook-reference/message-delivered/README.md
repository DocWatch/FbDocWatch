#  Message Delivered Callback

This callback will occur when a message a page has sent has been delivered.  
You can subscribe to this callback by selecting the ` message_deliveries `
field when [ setting up ](/docs/messenger-platform/webhook-reference#setup)
your webhook.

##  Example

    
    
    {
       "sender":{
          "id":"USER_ID"
       },
       "recipient":{
          "id":"PAGE_ID"
       },
       "delivery":{
          "mids":[
             "mid.1458668856218:ed81099e15d3f4f233"
          ],
          "watermark":1458668856253,
          "seq":37
       }
    }    

##  Fields

###  ` delivery ` object

Field Name  |  Description  |  Type  
---|---|---  
  
` mids `

|

Array containing message IDs of messages that were delivered. Field may not be
present.

|

Array  
  
` watermark `

|

All messages that were sent before this timestamp were delivered

|

Number  
  
` seq `

|

Sequence number

|

Number  
  
Both ` mids ` and ` watermark ` fields are used to determine which messages
were delivered. ` watermark ` is always present and ` mids ` is sometimes
present. ` mids ` provides delivery receipts on a per-message basis but may
not be present (due to backward compatibility reasons with older Messenger
clients). ` watermark ` is always present and is a timestamp indicating that
all messages with a timestamp before ` watermark ` were delivered.

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

