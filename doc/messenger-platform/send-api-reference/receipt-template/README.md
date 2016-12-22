#  Receipt Template

Use the Receipt Template with the [ Send API ](/docs/messenger-platform/send-
api-reference#request) to send a order confirmation, with the transaction
summary and description for each item.

![](https://scontent.xx.fbcdn.net/t39.2365-6/13466939_915325738590743_1056699384_n.png)

##  Example

    
    
    curl -X POST -H "Content-Type: application/json" -d '{
      "recipient":{
        "id":"USER_ID"
      },
      "message":{
        "attachment":{
          "type":"template",
          "payload":{
            "template_type":"receipt",
            "recipient_name":"Stephane Crozatier",
            "order_number":"12345678902",
            "currency":"USD",
            "payment_method":"Visa 2345",        
            "order_url":"http://petersapparel.parseapp.com/order?order_id=123456",
            "timestamp":"1428444852", 
            "elements":[
              {
                "title":"Classic White T-Shirt",
                "subtitle":"100% Soft and Luxurious Cotton",
                "quantity":2,
                "price":50,
                "currency":"USD",
                "image_url":"http://petersapparel.parseapp.com/img/whiteshirt.png"
              },
              {
                "title":"Classic Gray T-Shirt",
                "subtitle":"100% Soft and Luxurious Cotton",
                "quantity":1,
                "price":25,
                "currency":"USD",
                "image_url":"http://petersapparel.parseapp.com/img/grayshirt.png"
              }
            ],
            "address":{
              "street_1":"1 Hacker Way",
              "street_2":"",
              "city":"Menlo Park",
              "postal_code":"94025",
              "state":"CA",
              "country":"US"
            },
            "summary":{
              "subtotal":75.00,
              "shipping_cost":4.95,
              "total_tax":6.19,
              "total_cost":56.14
            },
            "adjustments":[
              {
                "name":"New Customer Discount",
                "amount":20
              },
              {
                "name":"$10 Off Coupon",
                "amount":10
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

` payload ` of receipt template

|

Y  
  
###  ` payload ` object

Property Name  |  Description  |  Type  |  Required  
---|---|---|---  
  
` template_type `

|

Value must be ` receipt ` .

|

String

|

Y  
  
` recipient_name `

|

Recipient's name.

|

String

|

Y  
  
` merchant_name `

|

Merchant's name. If present this is shown as logo text.

|

String

|

N  
  
` order_number `

|

Order number.

|

String

|

Y, must be unique  
  
` currency `

|

Currency for order.

|

String

|

Y  
  
` payment_method `

|

Payment method details. This can be a custom string. ex: "Visa 1234".

|

String

|

Y  
  
` timestamp `

|

Timestamp of the order, in seconds.

|

String

|

N  
  
` order_url `

|

URL of order.

|

String

|

N  
  
` elements `

|

Items in order.

|

Array of  ` element `

|

N  
  
` address `

|

Shipping address.

|

` address ` object

|

N  
  
` summary `

|

Payment summary.

|

` summary ` object

|

Y  
  
` adjustments `

|

Payment adjustments.

|

Array of  ` adjustment `

|

N  
  
  * ` order_number ` must be unique for each user 
  * ` payment_method ` is required but is a String. You may insert an arbitrary string here but we recommend providing enough information for the person to decipher which payment method and account they used (e.g., the name of the payment method and partial account number) 
  * ` elements ` has a maximum of 100 
  * ` elements ` sort order is not guaranteed 
  * ` address ` is optional. If you do not ship an item, you may omit these fields 
  * ` state ` can be a region or province for international addresses 
  * ` adjustments ` allow a way to insert adjusted pricing (e.g., sales). Adjustments are optional 

###  ` element ` object

Property Name  |  Description  |  Type  |  Required  
---|---|---|---  
  
` title `

|

Title of item

|

String

|

Y  
  
` subtitle `

|

Subtitle of item

|

String

|

N  
  
` quantity `

|

Quantity of item

|

Number

|

N  
  
` price `

|

Item price

|

Number

|

Y, but 0 is allowed  
  
` currency `

|

Currency of price

|

String

|

N  
  
` image_url `

|

Image URL of item

|

String

|

N  
  
###  ` address ` object

Property Name  |  Description  |  Type  |  Required  
---|---|---|---  
  
` street_1 `

|

Street address, line 1

|

String

|

Y, if ` address ` is set  
  
` street_2 `

|

Street address, line 2

|

String

|

N  
  
` city `

|

City

|

String

|

Y, if ` address ` is set  
  
` postal_code `

|

Postal code

|

String

|

Y, if ` address ` is set  
  
` state `

|

State abbreviation or Region/Province (international)

|

String

|

Y, if ` address ` is set  
  
` country `

|

Two-letter country abbreviation

|

String

|

Y, if ` address ` is set  
  
###  ` summary ` object

Property Name  |  Description  |  Type  |  Required  
---|---|---|---  
  
` subtotal `

|

Subtotal

|

Number

|

N  
  
` shipping_cost `

|

Cost of shipping

|

Number

|

N  
  
` total_tax `

|

Total tax

|

Number

|

N  
  
` total_cost `

|

Total cost

|

Number

|

Y  
  
  * These numbers should be valid and well formatted decimal numbers, using ' ` . ` ' (dot) as the decimal separator. Note that most currencies only accept up to 2 decimal places. 

###  ` adjustment ` object

Property Name  |  Description  |  Type  |  Required  
---|---|---|---  
  
` name `

|

Name of adjustment

|

String

|

N  
  
` amount `

|

Adjustment amount

|

Number

|

N  
  
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

