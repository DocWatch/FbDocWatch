#  Postback Received Callback

Postbacks occur when a Postback button, Get Started button, Persistent menu or
Structured Message is tapped. The payload field in the callback is defined on
the button.  
You can subscribe to this callback by selecting the ` messaging_postbacks `
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
      "timestamp":1458692752478,
      "postback":{
        "payload": USER_DEFINED_PAYLOAD,
        "referral": {
          "ref": USER_DEFINED_REFERRAL_PARAM,
          "source": "SHORTLINK",
          "type": "OPEN_THREAD",
        }
      }
    }    

##  Fields

###  ` postback ` object

Field Name  |  Description  |  Type  
---|---|---  
  
` payload `

|

` payload ` parameter that was defined with the button

|

String  
  
` referral `

|

Comes only with Get Started postback and if an optional ref param was passed
from the entry point, such as [ m.me link ](/docs/messenger-platform/referral-
params) .

|

Structure follows [ referral event ](/docs/messenger-platform/webhook-
reference/referral)  
  
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

