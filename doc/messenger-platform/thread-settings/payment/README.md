#  Payments settings

You need to be accepted to our beta program to use payment. You can send test
payment before accepted. [ Request access to our beta program for payments
](https://www.facebook.com/messenger_platform/payments_requestaccess) .

These are settings related to payments. The payment privacy URL must be set
regardless which integration you are using [ Buy Button ](/docs/messenger-
platform/send-api-reference/buy-button) or [ Webviews and Messenger Extensions
](/docs/messenger-platform/send-api-reference/webview) . The payment public
key must be set if you are using [ Webviews and Messenger Extensions
](/docs/messenger-platform/send-api-reference/webview) or tokenized payment
with [ Buy Button ](/docs/messenger-platform/send-api-reference/buy-button) .
You can add payment test users and start to testing without being accepted in
the beta program.

##  Payment Privacy URL

The ` payment_privacy_url ` will appear in our payment dialogs and people will
be able to view these terms.

###  Example

    
    
    curl -X POST -H "Content-Type: application/json" -d '{
      "setting_type": "payment",
      "payment_privacy_url": "https://petersfancyapparel.com/payment_privacy.html"
    }' "https://graph.facebook.com/v2.6/me/thread_settings?access_token=PAGE_ACCESS_TOKEN"

_ _

##  Payment Public Key

The ` payment_public_key ` is used to encrypt sensitive payment data sent to
you. Read more about [ creating encryption keys ](/docs/messenger-
platform/payments-reference#encryption_key) .

###  Example

    
    
    curl -X POST -H "Content-Type: application/json" -d '{
      "setting_type" : "payment",
      "payment_public_key" : "-----BEGIN PGP PUBLIC KEY BLOCK-----\nVersion: GnuPG v1\n\nmQINBFfId.......N5REigmEEW5t\n=gak9\n-----END PGP PUBLIC KEY BLOCK-----\n"
    }' "https://graph.facebook.com/v2.6/me/thread_settings?access_token=PAGE_ACCESS_TOKEN"

_ _

##  Add Payment Test Users

You can add payment test users so that their credit card won't be charged
during your development. Once added, it will impact both Buy Button and
Webview Extension integrations, any payment send to these users will be a
dummy charge. If you are only testing [ Buy Button ](/docs/messenger-
platform/send-api-reference/buy-button) , consider using the ` is_test_payment
` flag which is simpler for testing.

###  Example

    
    
         curl -X POST -H "Content-Type: application/json" -d '{
           "setting_type": "payment",
           "payment_dev_mode_action": "ADD",
           "payment_testers": ["1178041762247207"],
         }' "https://graph.facebook.com/v2.6/me/thread_settings?access_token=PAGE_ACCESS_TOKEN"
       

_ _

##  Fields

Property Name  |  Description  |  Type  
---|---|---  
  
` setting_type `

|

Must be ` payment ` .

|

String  
  
` payment_privacy_url `

|

Valid URL for the payment privacy.

|

String  
  
` payment_public_key `

|

Your PGP Public Key (4096 bit RSA)

|

String  
  
` payment_dev_mode_action `

|

ADD/REMOVE dev mode test users.

|

String  
  
` payment_testers `

|

A list of page scoped user id to be added as payment testers.

|

Array  
  
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

