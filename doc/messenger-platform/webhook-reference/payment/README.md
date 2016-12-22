#  Payment Callback (BETA)

This feature is in beta. [ Request access to our beta program for payments
](https://www.facebook.com/messenger_platform/payments_requestaccess) .

This callback occurs when a persons taps the pay button from the checkout
dialog rendered by the [ Buy Button ](/docs/messenger-platform/send-api-
reference/buy-button) . It contains the requested user information as well as
payment credentials. Depends on the payment provider you use, the payment
credential will differ.

You must subscribe to this callback by selecting the ` messaging_payments `
field when [ setting up ](/docs/messenger-platform/webhook-reference#setup)
your webhook.

##  Stripe/Paypal

The following is the example callback if you are using Stripe/Paypal that
linked in page settings. After user click on pay, user will be charged
directly and the payment will be send to your Stripe/Paypla account. This
webhook event will be called once the process succeed. All the requested user
information that user entered in the payment dialog will be passed back in the
webhook event. The charge_id from Paypal/Stripe will be passed to you for
tracking the payment. You need to return HTTP status of ` 200 ` once you
finished processing the event.

If the payment is a test payment, we will not charge the card but will send a
result with dummy fb_payment_id/charge_id to you. You can do test payment with
Stripe/Paypal only if your page has payment permission for now. Refers to [
How to Test Payment ](/docs/messenger-platform/complete-
guide/payments#test_payments) for details.

    
    
    {
      "object": "page",
      "entry": [
        {
          "id": "PAGE_ID",
          "time": 1473208792799,
          "messaging": [
            {
              "recipient": {
                "id": "PAGE_ID"
              },
              "timestamp": 1473208792799,
              "sender": {
                "id": "USER_ID"
              },
              "payment": {
                "payload": "DEVELOPER_DEFINED_PAYLOAD",
                "requested_user_info": {
                  "shipping_address": {
                    "street_1": "1 Hacker Way",
                    "street_2": "",
                    "city": "MENLO PARK",
                    "state": "CA",
                    "country": "US",
                    "postal_code": "94025"
                  },
                  "contact_name": "Peter Chang",
                  "contact_email": "peter@anemailprovider.com",
                  "contact_phone": "+15105551234"
                },
               "payment_credential": {
                  "provider_type": "stripe", # paypal if you are using paypal as provider
                  "charge_id": "ch_18tmdBEoNIH3FPJHa60ep123",
                  "fb_payment_id": "123456789",
                },      
                "amount": {
                  "currency": "USD",
                  "amount": "29.62"
                }, 
                "shipping_option_id": "123"
              }
            }
          ]
        }
      ]
    }
        

##  Tokenized Payment

If you are using tokenized payment, when user click on pay, we will send you a
single-use Discover virtual card provisioned by PayPal. The card credential
will be encrypted by the public key you provided in previous steps. You can
then decrypt the tokenized card by following the [ detail steps here
](/docs/messenger-platform/complete-guide/payments#decrypting) . After you
successfully decoded the credential, you can then integrate with your
preferred payment provider to charge the card. You need to return HTTP status
of ` 200 ` once you finished processing the event.

If the payment is a test payment, you will get a dummy tokenized card back
with the following dummy information (card_number: 4111111111111111, cvv: 123,
expiry month: 11, expiry year: 2020). You can test tokenized payment even if
your page/app has not been accepted to beta program. Refers to [ How to Test
Payment ](/docs/messenger-platform/complete-guide/payments#test_payments) for
details.

    
    
    {
      "object": "page",
      "entry": [
        {
          "id": "PAGE_ID",
          "time": 1473208792799,
          "messaging": [
            {
              "recipient": {
                "id": "PAGE_ID"
              },
              "timestamp": 1473208792799,
              "sender": {
                "id": "USER_ID"
              },
              "payment": {
                "payload": "DEVELOPER_DEFINED_PAYLOAD",
                "requested_user_info": {
                  "shipping_address": {
                    "street_1": "1 Hacker Way",
                    "street_2": "",
                    "city": "MENLO PARK",
                    "state": "CA",
                    "country": "US",
                    "postal_code": "94025"
                  },
                  "contact_name": "Peter Chang",
                  "contact_email": "peter@anemailprovider.com",
                  "contact_phone": "+15105551234"
                },
                "payment_credential":{
                   "provider_type" : "token",
                   "tokenized_card": "__tokenized_card__",
                   "tokenized_cvv":"tokenized cvv",
                   "token_expiry_month":"3",
                   "token_expiry_year":"2019"
                   "fb_payment_id" : "123456789",
                },
                "amount": {
                  "currency": "USD",
                  "amount": "29.62"
                }, 
                "shipping_option_id": "123"
              }
            }
          ]
        }
      ]
    }
        

###  Callback Fields

####  ` payment ` object

Field Name  |  Description  |  Type  
---|---|---  
  
` payload `

|

Metadata defined in the Buy Button.

|

String  
  
` requested_user_info `

|

Information that was requested from the user by the Buy Button.

|

Object  
  
` payment_credential `

|

Payment credentials.

|

Object  
  
` amount `

|

Total amount of transaction.

|

Object  
  
` shipping_option_id `

|

The ` option_id ` of the selected shipping option sent via the [ checkout
update callback ](/docs/messenger-platform/webhook-reference/checkout-
update#response) . Only applicable for flexible payments.

|

String  
  
####  ` requested_user_info ` object

Data in this object will depend on the [ requested user information defined on
the Buy Button ](/docs/messenger-platform/send-api-reference/buy-
button#payment_summary) .

Field Name  |  Description  |  Type  
---|---|---  
  
` shipping_address `

|

Person's shipping address

|

Object  
  
` contact_name `

|

Person's name

|

String  
  
` contact_email `

|

Person's email

|

String  
  
` contact_phone `

|

Person's phone number

|

String  
  
####  ` shipping_address ` object

Field Name  |  Description  |  Type  
---|---|---  
  
` street1 `

|

Shipping address street, first line

|

String  
  
` street2 `

|

Shipping address street, second line

|

String  
  
` city `

|

Shipping address city

|

String  
  
` state `

|

Shipping address state

|

String  
  
` country `

|

Shipping address country

|

String  
  
` postal_code `

|

Shipping address postal code

|

String  
  
####  ` payment_credential ` object

Field Name  |  Description  |  Type  
---|---|---  
  
` provider_type `

|

Payment provider type (one of stripe/paypal/token)

|

String  
  
` charge_id `

|

Payment provider charge id (for stripe/paypal, null for tokenization), for a
test_payment, the charge id will be test_charge_id_12345

|

String  
  
` tokenized_card `

|

PGP-signed tokenized charge card (null for stripe/paypal)

|

String  
  
` tokenized_cvv `

|

PGP-signed CVV number (null for stripe/paypal)

|

String  
  
` token_expiry_month `

|

Expiry month (null for stripe/paypal)

|

String  
  
` token_expiry_year `

|

Expiry year (null for stripe/paypal)

|

String  
  
` fb_payment_id `

|

A facebook issued payment id for tracking. If it is a test payment, the id
will be test_payment_id_12345.

|

String  
  
####  ` amount ` object

Field Name  |  Description  |  Type  
---|---|---  
  
` currency `

|

Currency of amount

|

Object  
  
` amount `

|

Total amount

|

String  
  
##  Response

You must respond to the callback with an HTTP status of ` 200 ` .

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

