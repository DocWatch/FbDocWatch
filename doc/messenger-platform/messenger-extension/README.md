#  Webview and Extensions

Using the webview, you can control the display height of the in-app browser
window. This allows you to build more custom experiences that still appear to
be part of the Messenger thread.

![](https://scontent.xx.fbcdn.net/t39.2365-6/14235598_836379243130615_794043810_n.png)

Webviews can be shown in compact, tall and full sizes. Using partial-height
webviews, make it feel like it's part of the thread. These are also useful if
you want to render custom controls or have more control over how content is
displayed.

![](https://scontent.xx.fbcdn.net/t39.2365-6/14235549_307513439610741_1331859866_n.png)

###  Messenger Extensions

We've also added Messenger Extensions which enable your web page to integrate
tightly with Messenger. Using the Messenger Extensions Javascript SDK, you can
do the following:

  * Get the user id associated with the thread 
  * Close the Webview 

Extensions also supports integrated payments. The following payment
functionality is supported:

  * Open a native payment dialog to get a person's information and payment credentials 
  * Process a payment with Stripe 

![](https://scontent.xx.fbcdn.net/t39.2365-6/14235606_102210503572545_1424211441_n.png)

Payment features are in beta. [ Request access to our beta program for
payments ](https://www.facebook.com/messenger_platform/payments_requestaccess)
.

Messenger Extensions only work on iOS and Android. For messenger.com, see the
[ ` fallback_url ` parameter for URL buttons ](/docs/messenger-platform/send-
api-reference/url-button#fields) .

##  Implementation

The Button and Generic Template can open a Webview by adding a `
webview_height_ratio ` field with a [ URL Button ](/docs/messenger-
platform/send-api-reference/url-button) .

    
    
    ...
    
            "buttons":[
                  {
                    "type":"web_url",
                    "url":"https://petersfancyapparel.com/criteria_selector",
                    "title":"Select Criteria",
                    "webview_height_ratio": "compact"
                  }
            ]
            
    ... 

See the [ URL Button reference doc ](/docs/messenger-platform/send-api-
reference/url-button) for field details.

###  Dialog Title

The title of the HTML document will be used as the title of the dialog.

    
    
    <html>
      <head>
        <title>Select Criteria</title>
      </head>
       ...
    </html>

_ _

##  Messenger Extensions

Messenger Extensions allows tight integration between Messenger and the page
being opened in a Webview. With Extensions, you can get the person's user id
and close the webview.

###  Whitelist Your Domain

You must whitelist your domain for security reasons. Read the [ reference doc
](/docs/messenger-platform/thread-settings/domain-whitelisting) for more
details.

    
    
    curl -X POST -H "Content-Type: application/json" -d '{
      "setting_type" : "domain_whitelisting",
      "whitelisted_domains" : ["https://petersfancyapparel.com"],
      "domain_action_type": "add"
    }' "https://graph.facebook.com/v2.6/me/thread_settings?access_token=PAGE_ACCESS_TOKEN"

###  URL Button with Messenger Extensions

In order to enable Messenger Extensions with your URL Button, you must set `
messenger_extensions ` to ` true ` .

    
    
    ...
    
            "buttons":[
                  {
                    "type":"web_url",
                    "url":"https://petersfancyapparel.com/criteria_selector",
                    "title":"Select Criteria",
                    "webview_height_ratio": "full",
                    "messenger_extensions": true,  
                    "fallback_url": "https://petersfancyapparel.com/fallback"
                  }
            ]
            
    ...        

You may also use Webviews from the [ Persistent Menu ](/docs/messenger-
platform/thread-settings/persistent-menu) .

    
    
    ...
          
      "call_to_actions":[
        {
          "type":"web_url",
          "title":"Checkout",
          "url":"https://petersfancyapparel.com/checkout",
          "webview_height_ratio": "full",
          "messenger_extensions": true
        }
      ]    
          
    ...      
        

###  Messenger Extensions Javascript SDK

####  Load the JS SDK

Add the Messenger Extensions Javascript SDK to the page being loaded in the
webview.

    
    
    <script>
    (function(d, s, id){
      var js, fjs = d.getElementsByTagName(s)[0];
      if (d.getElementById(id)) {return;}
      js = d.createElement(s); js.id = id;
      js.src = "//connect.facebook.com/en_US/messenger.Extensions.js";
      fjs.parentNode.insertBefore(js, fjs);
    }(document, 'script', 'Messenger'));
    </script>      

####  SDK Loaded

` window.extAsyncInit ` will be called when the Messenger Extensions JS SDK is
done loading.

    
    
    <script>
      window.extAsyncInit = function() {
        // the Messenger Extensions JS SDK is done loading 
      };
    </script>

###  Check Messenger Extensions is Supported

Messenger Extensions only work on newer versions of Messenger iOS App and
Messenger Android App. After SDK is loaded, `
MessengerExtensions.isInExtension ` can be used to check whether Messenger
Extensions is supported for current webview. It will return a boolean.

    
    
    <script>
        var isSupported = MessengerExtensions.isInExtension();    
    </script>

###  Get User IDs

` MessengerExtensions.getUserID ` will returned the page-scoped user id. You
can use this to identify the person and personalize the Webview for the
viewer.

    
    
    <script>
        MessengerExtensions.getUserID(function success(uids) {
          var psid = uids.psid;
      
        }, function error(err) {      
      
        });    
    </script>

####  Params

Param  |  Description  |  Type  |  Required  
---|---|---|---  
  
success callback

|

This function will be called if ` getUserID ` is successful.

|

function

|

Y  
  
error callback

|

This function will be called if there is an error.

|

function

|

Y  
  
####  Result

Field  |  Description  |  Type  
---|---|---  
  
` uids `

|

Object containing user ids

|

Object  
  
####  ` uids ` fields

Field  |  Description  |  Type  
---|---|---  
  
` psid `

|

Page-scoped user ID

|

Number  
  
###  Close Webview

` MessengerExtensions.requestCloseBrowser ` will close the webview. You may
want to do this after the transaction is completed.

    
    
    <script>
          MessengerExtensions.requestCloseBrowser(function success() {
      
          }, function error(err) {
      
          });
    </script>

####  Params

Param  |  Description  |  Type  |  Required  
---|---|---|---  
  
success callback

|

This function will be called if ` requestCloseBrowser ` is successful.

|

function

|

Y  
  
error callback

|

This function will be called if there is an error.

|

function

|

Y  
  
_ _

##  Payments

Payment features are in beta. [ Request access to our beta program for
payments ](https://www.facebook.com/messenger_platform/payments_requestaccess)
.

With Messenger Extensions, you can integrate payments by doing the following:

  1. Open a payment dialog  to get shipping and payment information. This step also authorizes a payment. 
  2. If you're using credit card tokenization,  request authorized payment credentials  . If you're using Stripe or Paypal,  process the payment  . 

###  Open Payment Dialog

On your checkout page, you should place a button in the payments section that
calls this method. It will trigger a native dialog in Messenger allowing them
to select their shipping and payment information. The information will be sent
to you after they tap 'Continue'.

You should use the returned information to calculate shipping and taxes.
Shipping and payment information should be displayed before they complete the
purchase.

![](https://scontent.xx.fbcdn.net/t39.2365-6/14235596_298504120519333_146285064_n.png)

    
    
    <script>
          MessengerExtensions.requestPaymentCredentials(
             function success(name, email, cardType, cardLastFourDigits, shippingAddress) {
    
             }, 
             function error(err) {
    
             },
             ['CONTACT_NAME', 'CONTACT_EMAIL', 'CONTACT_PHONE', 'SHIPPING_ADDRESS']
      );
    </script>       

####  Params

Param  |  Description  |  Type  |  Required  
---|---|---|---  
  
success callback

|

This function will be called if ` requestPaymentCredentials ` is successful.

|

function

|

Y  
  
error callback

|

This function will be called if there is an error.

|

function

|

Y  
  
requested user info

|

Information requested from person that will render in the dialog. Valid
values: ` shipping_address ` , ` contact_name ` , ` contact_phone ` , `
contact_email ` . You can config these based on your product need. If not
specified, all the fields will be rendered in the checkout flow.

|

Array

|

Y  
  
####  Result

Field  |  Description  |  Type  
---|---|---  
  
name

|

Person's name

|

String  
  
email

|

Person's email

|

String  
  
card type

|

Type of credit card

|

String  
  
card last four digits

|

Last four digits of the credit card number

|

Number  
  
shipping address

|

Person's shipping address

|

Object  
  
####  ` shipping_address ` fields

Field  |  Description  |  Type  
---|---|---  
  
` name `

|

Name on shipping address

|

String  
  
` street1 `

|

Street address

|

String  
  
` city `

|

Shipping city

|

String  
  
` region `

|

Shipping state/region

|

String  
  
` postalCode `

|

Shipping postal code

|

String  
  
` country `

|

Shipping country

|

String  
  
###  Request Authorized Payment Credentials

If you're using credit card tokenization, use this method.

When the person completes the transaction on your page (e.g., taps a buy
button), you can call this method to get their payment credentials. Calling
this method will place a hold on their card. You can use the payment
credentials to charge them.

If the payment is a test payment, you will get a dummy tokenized card back
with the following dummy information (card_number: 4111111111111111, cvv: 123,
expiry month: 11, expiry year: 2020). Testing is available even if your
page/app does not have payment permission. Refers to [ How to Test Payment
](/docs/messenger-platform/complete-guide/payments#test_payments) for details.

You must call ` requestPaymentCredentials ` before calling this method.

Consider sending a purchase confirmation into the thread. You may use the [
Receipt Template ](/docs/messenger-platform/send-api-reference/receipt-
template) to send a receipt.

    
    
    <script>
          MessengerExtensions.requestAuthorizedPaymentCredentials(function success(paymentCredentials) {
            var cardNumber = paymentCredentials.token_card_number;
            var cardCVV = paymentCredentials.token_cvv;
            var cardExpiry = paymentCredentials.token_expiry;
    
          }, function error(err) {
    
          }, 
          amount);
    </script>      
    

####  Params

Param  |  Description  |  Type  |  Required  
---|---|---|---  
  
success callback

|

This function will be called if ` requestAuthorizedPaymentCredentials ` is
successful.

|

function

|

Y  
  
error callback

|

This function will be called if there is an error.

|

function

|

Y  
  
amount

|

Final amount, should include shipping and taxes

|

Decimal

|

Y  
  
####  Result

Field  |  Description  |  Type  
---|---|---  
  
payment credentials

|

Object containing payment credentials

|

Object  
  
####  Payment credentials fields

Field  |  Description  |  Type  
---|---|---  
  
` token_card_number `

|

PGP-signed tokenized charge card

|

String  
  
` token_cvv `

|

PGP-signed CVV number

|

String  
  
` token_expiry `

|

Token Expiry

|

Object  
  
####  ` token_expiry ` fields

Field  |  Description  |  Type  
---|---|---  
  
` month `

|

Expiry month

|

Number  
  
` year `

|

Expiry year

|

Number  
  
You can learn how to decrypt the data by following the [ detailed decrypting
guide here ](/docs/messenger-platform/payments-reference#decrypting) .

##  Process Payment

If you're using Stripe or Paypal, you must use this method to process their
payment. When the person completes the transaction on your page (e.g., taps a
buy button), call this to charge their credit card. We will call the payment
provider and send you the transaction ID.

If the payment is a test payment, we will not charge the card but will send a
result with dummy fb_payment_id/external_transaction_id to you. Please note if
your page has not being accepted to beta program, testing mode is not
available. You can test ` requestAuthorizedPaymentCredentials ` instead.
Refers to [ How to Test Payment ](/docs/messenger-platform/complete-
guide/payments#test_payments) for details.

You must call ` requestPaymentCredentials ` before calling this method.

    
    
    <script>
          MessengerExtensions.processPayment(function success(result) {
            var paymentResult = result.payment_result;
          }, function error(err) {
    
          }, 
          amount);
    </script>      
    

####  Params

Param  |  Description  |  Type  |  Required  
---|---|---|---  
  
success callback

|

This function will be called if ` processPayment ` is successful.

|

function

|

Y  
  
error callback

|

This function will be called if there is an error.

|

function

|

Y  
  
amount

|

Final amount, should include shipping and taxes

|

Decimal

|

Y  
  
####  Result

Field  |  Description  |  Type  
---|---|---  
  
` result.payment_result `

|

PGP-signed transaction details

|

String  
  
####  Decrypted Payment Result

Field  |  Description  |  Type  
---|---|---  
  
` name `

|

Person name

|

String  
  
` amount `

|

Amount of transaction

|

Number  
  
` timestamp `

|

Epoch timestamp

|

Number  
  
` external_transaction_id `

|

Transaction ID from payment processor, in case of test payment, the value will
be test_charge_id_12345.

|

String  
  
` fb_payment_id `

|

Facebook payment ID, in case of a test payment, the value will be
test_payment_id_12345.

|

String  
  
` provider `

|

Facebook payment provider ID

|

String  
  
You can learn how to decrypt the data by following the [ detailed decrypting
guide here ](/docs/messenger-platform/payments-reference#decrypting) .

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

