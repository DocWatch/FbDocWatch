# Webhook Reference

Below are the callbacks that are delivered to your webhook for the Messenger
Platform.

If you need to learn how to setup a webhook, read the [detailed
docs](/docs/graph-api/webhooks). This will walk you through the general setup,
the format of the data and how to verify the call came from Facebook.

  * Setup
  * Subscribe App to Page
  * Common Format
  * Response
  * Unsubscribe
  * Batching
  * Security
  * Validation

## Setup

When you setup your webhook, there are 10 relevant webhook events
(subscription fields) for this integration. All fields are optional so select
the fields most relevant for your experience.

Field |  Description  
---|---  
  
`message`

|

Subscribes to [Message Received events](/docs/messenger-platform/webhook-
reference/message-received)  
  
`message_deliveries`

|

Subscribes to [Message Delivered events](/docs/messenger-platform/webhook-
reference/message-delivered)  
  
`message_reads`

|

Subscribes to [Message Read events](/docs/messenger-platform/webhook-
reference/message-read)  
  
`message_echoes`

|

Subscribes to [Message Echo events](/docs/messenger-platform/webhook-
reference/message-echo)  
  
`messaging_postbacks`

|

Subscribes to [Postback Received events](/docs/messenger-platform/webhook-
reference/postback-received)  
  
`messaging_optins`

|

Subscribes to [Plugin Opt-in events](/docs/messenger-platform/plugin-
reference)  
  
`messaging_referrals`

|

Subscribes to [Referral events](/docs/messenger-platform/webhook-
reference/referral)  
  
`messaging_checkout_updates` (BETA)

|

Subscribes to [Checkout Update events](/docs/messenger-platform/webhook-
reference/checkout-update)  
  
`messaging_payments` (BETA)

|

Subscribes to [Payment events](/docs/messenger-platform/webhook-
reference/payment)  
  
`messaging_account_linking`

|

Subscribes to [Account Linking events](/docs/messenger-platform/webhook-
reference/account-linking)  
  
Payment-related callbacks are in beta and will only appear to developers who
have access. [Request access to our beta program for
payments](https://www.facebook.com/messenger_platform/payments_requestaccess).

![](https://scontent-
cdg2-1.xx.fbcdn.net/t39.2365-6/14050177_1818094655103267_1221918034_n.png)

### Edit your Webhook

In order to edit your webhook, click the "Add Product" button in the App
Dashboard and add the "Webhook" option. That will present you with an
interface to edit your webhook.

__

## Subscribe App to Page

Subscribe an app to get updates for a page. You can do this in the Webhooks
section under the Messenger Tab.

A page may have up to 10 apps subscribing to it.

![](https://scontent-
cdg2-1.xx.fbcdn.net/t39.2365-6/13466568_984470978337660_125967052_n.png)

Or you can do this via API:

    
    
    curl -X POST "https://graph.facebook.com/v2.6/me/subscribed_apps?access_token=PAGE_ACCESS_TOKEN"    

If successful, you will receive a response:

    
    
    {
      "success": true
    }    

Note that to create a subscription, the owner of the page access token must
have moderator admin access or higher on the Page.

__

## Common Format

All callbacks for the Messenger Platform have a common structure.

    
    
    {
      "object":"page",
      "entry":[
        {
          "id":"PAGE_ID",
          "time":1458692752478,
          "messaging":[
            {
              "sender":{
                "id":"USER_ID"
              },
              "recipient":{
                "id":"PAGE_ID"
              },
    
              ...
            }
          ]
        }
      ]
    }    

### Payload

Field Name |  Description |  Type  
---|---|---  
  
`object`

|

Value will be `page`

|

String  
  
`entry`

|

Array containing event data

|

Array of `entry`  
  
### `entry` object

Field Name |  Description |  Type  
---|---|---  
  
`id`

|

Page ID of page

|

String  
  
`time`

|

Time of update (epoch time in milliseconds)

|

Number  
  
`messaging`

|

Array containing objects related to messaging

|

Array of `messaging`  
  
### `messaging` object

Field Name |  Description |  Type  
---|---|---  
  
`sender.id`

|

Sender user ID

|

String  
  
`recipient.id`

|

Recipient user ID

|

String  
  
`...`

|

Additional callback specific fields

|  
  
When representing a user, these IDs are page-scoped IDs (PSID). This means
that the IDs of users are unique for a given page.

If you have an existing [Facebook Login](/docs/facebook-login) integration,
user IDs are app-scoped and will not work with the Messenger platform.

__

## Response

Your webhook callback should always return a 200 OK HTTP response when invoked
by Facebook. Failing to do so may cause your webhook to be unsubscribed by the
Messenger Platform.

It is extremely important to return a 200 OK HTTP as fast as possible.
Facebook will wait for a 200 before sending you the next message. In high
volume bots, a delay in returning a 200 can cause significant delays in
Facebook delivering messages to your webhook.

A delivery receipt will automatically be sent to the user after your webhook
has acknowledged the message. You can also use [Sender
Actions](/docs/messenger-platform/send-api-reference/sender-actions) to notify
that the message has been seen.

__

## Unsubscribe

If your webhook returns an error (i.e., not a 2XX status) or times out (i.e.,
takes longer than 20 second to respond) for over 15 minutes, then we will send
you a warning developer alert.

If your webhook continues to fail for 8 hours, then we will send you a
developer alert that the webhook is being disabled and we will unsubscribe
your app. Once you've fixed your issues, you must re-add your webhook and [re-
subscribe your app to the
page](https://developers.intern.facebook.com/docs/messenger-platform/webhook-
reference#subsribe).

![](https://scontent-
cdg2-1.xx.fbcdn.net/t39.2365-6/13480194_134179967005698_496318901_n.png)

__

## Batching

Note that `entry` is an array and may contain multiple objects. Also, the
`messaging` array may contain multiple objects. Be sure to iterate over
`entry` and `messaging` to process all events. Each `messaging` object
contains a `sender` and `recipient`. The object will also contain a data
depending on the type of callback.

We may batch events in a single callback, especially during moments of high
load. Be sure to iterate over `entry` and `messaging` in the response to
capture all the events sent in the request.

__

## Security

The HTTP request will contain an `X-Hub-Signature` header which contains the
SHA1 signature of the request payload, using the app secret as the key, and
prefixed with `sha1=`. Your callback endpoint can verify this signature to
validate the integrity and origin of the payload

Please note that the calculation is made on the escaped unicode version of the
payload, with lower case hex digits. If you just calculate against the decoded
bytes, you will end up with a different signature. For example, the string
`äöå` should be escaped to `\u00e4\u00f6\u00e5`.

__

## Validation

You can test if your webhook works correctly and you're subscribed to a page
using the following endpoint:

    
    
    curl \
    -F "object_id=PAGE_ID" \
    -F "object=page" \
    -F "field=messages" \
    -F 'custom_fields={"page_id": PAGE_ID}' \
    -F "access_token=PAGE_ACCESS_TOKEN" \
    "https://graph.facebook.com/v2.6/APP_ID/subscriptions_sample"

As a result within a few seconds you should receive a webhook event with the
following data:

    
    
    [ { field: 'messages', value: { page_id: PAGE_ID } } ]

This can be helpful, if you want to make sure that your subscription is alive
and your webhook is receiving updates.

__

__

&lt;img height="1" width="1" alt="" style="display:none"
src="https://www.facebook.com/tr?id=675141479195042&amp;amp;ev=PixelInitialized"
/&gt;&lt;img height="1" width="1" alt="" style="display:none"
src="https://www.facebook.com/tr?id=574561515946252&amp;amp;ev=PixelInitialized"
/&gt;&lt;img height="1" width="1" alt="" style="display:none"
src="https://www.facebook.com/tr?id=1668333663438923&amp;amp;ev=PixelInitialized"
/&gt;&lt;img height="1" width="1" alt="" style="display:none"
src="https://www.facebook.com/tr?id=1754628768090156&amp;amp;ev=PixelInitialized"
/&gt;

