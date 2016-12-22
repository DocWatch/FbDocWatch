#  Referral Callback

This callback will occur when an m.me link is used with a referral param and
only in a case this user already has a thread with this bot (for new threads
see [ Postback Event ](/docs/messenger-platform/webhook-reference/postback-
received) ). See also the [ full guide on m.me links ](/docs/messenger-
platform/referral-params) .

To start receiving these events you need to subscribe to ` messaging_referral
` in the webhook settings for your app.

An m.me link with an an added parameter looks like this: `
http://m.me/mybot?ref=myparam ` . The value of the ` ref ` parameter will be
passed to the server via webhook.

##  Example

    
    
    {
      "sender":{
        "id":"USER_ID"
      },
      "recipient":{
        "id":"PAGE_ID"
      },
      "timestamp":1458692752478,
      "referral": {
        "ref": <REF DATA PASSED IN M.ME PARAM>,
        "source": "SHORTLINK",
        "type": "OPEN_THREAD",
      }
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

