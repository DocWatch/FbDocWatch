#  Checkout Update Callback (BETA)

This feature is in beta. [ Request access to our beta program for payments
](https://www.facebook.com/messenger_platform/payments_requestaccess) .

This callback enables you to update pricing for flexible-amount transactions
on the checkout dialog displayed by the [ Buy Button ](/docs/messenger-
platform/send-api-reference/buy-button) .

After the Buy Button is tapped, a call is made to the webhook containing the
person's shipping address. This enables you to update pricing with shipping
and taxes based on a person's location. This callback is made each time the
shipping address is changed.

You can subscribe to this callback by selecting the `
messaging_checkout_updates ` field when [ setting up ](/docs/messenger-
platform/webhook-reference#setup) your webhook.

The ` messaging_checkout_updates ` field will not be available until you've
been accepted into the beta program for payments.

###  Example Callback

    
    
    {
      "object": "page",
      "entry": [
        {
          "id": "PAGE_ID",
          "time": 1473204787206,
          "messaging": [
            {
              "recipient": {
                "id": "PAGE_ID"
              },
              "timestamp": 1473204787206,
              "sender": {
                "id": "USER_ID"
              },
              "checkout_update": {
                "payload": "DEVELOPER_DEFINED_PAYLOAD",
                "shipping_address": {
                  "id": 10105655000959552,
                  "country": "US",
                  "city": "MENLO PARK",
                  "street1": "1 Hacker Way",
                  "street2": "",
                  "state": "CA",
                  "postal_code": "94025"
                }
              }
            }
          ]
        }
      ]
    }      
        

###  Callback Fields

####  ` checkout_update ` object

Field Name  |  Description  |  Type  
---|---|---  
  
` payload `

|

Metadata defined in the Buy Button.

|

String  
  
` shipping_address `

|

The person's shipping address.

|

Object  
  
####  ` shipping_address ` object

Field Name  |  Description  |  Type  
---|---|---  
  
` id `

|

ID of shipping address

|

String  
  
` country `

|

Shipping address country

|

String  
  
` city `

|

Shipping address city

|

String  
  
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
  
` state `

|

Shipping address state

|

String  
  
` postal_code `

|

Shipping address postal code

|

String  
  
##  Response

You must respond to the callback with an HTTP status of ` 200 ` and the body
of the response must contain a list of shipping options. These options will be
displayed when the person taps the "Choose Shipping Options" from the Checkout
dialog. When the option is selected, the pricing line items will be
dynamically updated.

The selected ` option_id ` will be sent in the [ payment callback
](/docs/messenger-platform/webhook-reference/payment) in the `
shipping_option_id ` field.

###  Example Response Body

    
    
    {
      "shipping":[
        {
          "option_id":"1",
          "option_title":"Fedex",
          "price_list":[
            {
              "label":"Shipping",
              "amount":5.99
            },
            {
              "label":"Tax",
              "amount":1.99
            }
          ]
        },
        {
          "option_id":"2",
          "option_title":"USPS",
          "price_list":[
            {
              "label":"Shipping",
              "amount":4.99
            },
            {
              "label":"Tax",
              "amount":0.99
            }
          ]
        }
      ]
    }      
      

###  Response Fields

Field Name  |  Description  |  Type  
---|---|---  
  
` shipping `

|

List of shipping options shown in the checkout dialog.

|

Array  
  
####  ` shipping ` fields

Field Name  |  Description  |  Type  
---|---|---  
  
` option_id `

|

ID of shipping option

|

String  
  
` option_title `

|

Title of option

|

String  
  
` price_list `

|

List of line items that are used to update pricing.

|

Array  
  
####  ` price_list ` fields

Field Name  |  Description  |  Type  
---|---|---  
  
` label `

|

Label of line item.

|

String  
  
` amount `

|

Amount of line item.

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

