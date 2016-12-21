# Send API Reference

Send messages to users.

  * Request
  * Response
  * Phone Number
  * Limits
  * Errors

## Request

The Graph API version should be set to 2.6 or greater.

When your app is in [Development Mode](/docs/apps/managing-development-cycle),
the Send API will only work for admins, developers and testers of the app.
After your app is approved and public, it will work for the general public.

To send a message, make a `POST` request to
`https://graph.facebook.com/v2.6/me/messages?access_token=<PAGE_ACCESS_TOKEN>`
with your page access token. The payload must be provided in JSON format as
described below:

The Send API requires the `pages_messaging` permission.

### Example

    
    
    curl -X POST -H "Content-Type: application/json" -d '{
      "recipient": {
        "id": "USER_ID"
      },
      "message": {
        "text": "hello, world!"
      }
    }' "https://graph.facebook.com/v2.6/me/messages?access_token=PAGE_ACCESS_TOKEN"

### Payload

Property Name |  Description |  Required  
---|---|---  
  
`recipient`

|

`recipient` object

|

Yes  
  
`message`

|

`message` object

|

`message` or `sender_action` must be set  
  
`sender_action`

|

Message state: `typing_on`, `typing_off`, `mark_seen`

|

`message` or `sender_action` must be set  
  
`notification_type`

|

Push notification type: `REGULAR`, `SILENT_PUSH`, or `NO_PUSH`

|

No  
  
  * `message` or `sender_action` must be set
  * `notification_type` details: `REGULAR` will emit a sound/vibration and a phone notification; `SILENT_PUSH` will just emit a phone notification, `NO_PUSH` will not emit either
  * `notification_type` is optional; by default, messages will be `REGULAR` push notification type

### `recipient` object

Property Name |  Description |  Required  
---|---|---  
  
`phone_number`

|

Phone number of the recipient with the format **+1(212)555-2368**. Your bot
must be approved for Customer Matching to send messages this way.

|

`phone_number` or `id` must be set  
  
`id`

|

ID of recipient

|

`phone_number` or `id` must be set  
  
  * `phone_number` or `id` must be set

The `id` must be an ID that was retrieved through the [Messenger entry
points](/docs/messenger-platform/product-overview/entry-points) or through the
[Messenger webhooks](/docs/messenger-platform/webhook-reference) (e.g., a
person may discover your business in Messenger and start a conversation from
there.

These IDs are page-scoped IDs (PSID). This means that the IDs are unique for a
given page.

If you have an existing [Facebook Login](/docs/facebook-login) integration,
user IDs are app-scoped and will not work with the Messenger platform.

### `message` object

Property Name |  Description |  Required  
---|---|---  
  
`text`

|

Message text

|

`text` or `attachment` must be set  
  
`attachment`

|

`attachment` object

|

`text` or `attachment` must be set  
  
`quick_replies`

|

Array of [`quick_reply`](/docs/messenger-platform/send-api-reference/quick-
replies) to be sent with messages

|

N  
  
`metadata`

|

Custom string that will be re-delivered to webhook listeners

|

N  
  
  * `text` or `attachment` must be set
  * `text` and `attachment` are mutually exclusive
  * `text` is used when sending a text message, must be UTF-8 and has a 640 character limit
  * `attachment` is used to send messages with images or Structured Messages
  * `metadata` has a 1000 character limit

### `attachment` object

Property Name |  Description |  Required  
---|---|---  
  
`type`

|

Type of attachment, may be `image`, `audio`, `video`, `file` or `template`

|

Y  
  
`payload`

|

Payload of attachment

|

Y  
  
We support multiple types multimedia and templates attachments:

  * [image](/docs/messenger-platform/send-api-reference/image-attachment)
  * [audio](/docs/messenger-platform/send-api-reference/audio-attachment)
  * [video](/docs/messenger-platform/send-api-reference/video-attachment)
  * [file](/docs/messenger-platform/send-api-reference/file-attachment)
  * [generic template](/docs/messenger-platform/send-api-reference/generic-template)
  * [button template](/docs/messenger-platform/send-api-reference/button-template)
  * [receipt template](/docs/messenger-platform/send-api-reference/receipt-template)

### Attachment Reuse

You can optimize sending multimedia by reusing attachments. If you're sending
the same attachments repeatedly, you should consider reusing them. Attachment
reuse works with sending images, audio clips, videos and files.

Add the `is_reusable` flag and set it to `true` when calling the Send API with
an attachment.

    
    
    curl -X POST -H "Content-Type: application/json" -d '{
      "recipient": {
        "id": "USER_ID"
      },
      "message": {
        "attachment": {
          "type": "image",
          "payload": {
          	"url": "https://petersapparel.parseapp.com/img/shirt.png",
            "is_reusable": true
          }
        }
      }
    }' "https://graph.facebook.com/me/messages?access_token=PAGE_ACCESS_TOKEN"  

The response will contain an `attachment_id`. Please note that this ID is
private and only the page that originally sent the attachment can reuse it.

    
    
    {
      "recipient_id": "USER_ID",
      "message_id": "mid.1473372944816:94f72b88c597657974",
      "attachment_id": "1745504518999123"
    }  

On subsequent calls to the Send API, use the `attachment_id` to send the same
attachment. You can send an attachment to any user for a given page.

    
    
    curl -X POST -H "Content-Type: application/json" -d '{
      "recipient": {
        "id": "USER_ID"
      },
      "message": {
        "attachment": {
          "type": "image",
          "payload": {
            "attachment_id": "1745504518999123"
          }
        }
      }
    }' "https://graph.facebook.com/me/messages?access_token=PAGE_ACCESS_TOKEN"   

#### `attachment` object

Property Name |  Description |  Required  
---|---|---  
  
`type`

|

Type of reused attachment, may be `image`, `audio`, `video`, or `file`

|

Y  
  
`payload.attachment_id`

|

ID of attachment

|

Y  
  
__

## Response

A successful Send API request returns a JSON string containing identifiers for
the message and its recipient.

### Example

    
    
    {
      "recipient_id": "1008372609250235",
      "message_id": "mid.1456970487936:c34767dfe57ee6e339"
    }

### Fields

Property Name |  Description  
---|---  
  
`recipient_id`

|

Unique ID for the user  
  
`message_id`

|

Unique ID for the message  
  
__

## Phone Number

You can send a message to a user without requiring the user interacting with
the page first, by specifying a `phone_number`.

Sending a message to phone numbers requires the `pages_messaging_phone_number`
permission.

When messages are sent to phone numbers, we will only send the message if we
have a certain level of confidence of expected delivery. If you find that
during testing you cannot message your own phone number, re-verify it under
Facebook user settings and wait 24 hours. At that point, you should be able to
successfully send a message to your own phone.

In order to use Customer Matching, the Page must have a United States address
or have at least one admin who is in the United States. The phone number
doesn't need to respect these requirements.

__

## Limits

### Calls to the Send API

We support a high rate of calls to the Send API. However, you should architect
your systems such that you distribute any sudden high amounts of load over
time and are able to control your throughput should you hit our rate limits.
Rate limits are in place to prevent malicious behavior and poor user
experiences. Be sure to catch any errors returned by the Send API including
the one indicating that you've reached the rate limit.

__

## Errors

When a Send API request fails, you'll receive a JSON response describing the
corresponding error `code` and `message`. Messenger Platform errors are
grouped by code, with a different message depending on the error condition.

Below is a list of common errors that you should consider handling at run-
time.

### Example

    
    
    {
      "error": {
        "message": "Invalid OAuth access token.",
        "type": "OAuthException",
        "code": 190,
        "error_subcode": 1234567,
        "fbtrace_id": "BLBz/WZt8dN"
      }
    }

### Internal Errors

Code |  Subcode |  Message  
---|---|---  
  
`1200`

|

\--

|

Temporary send message failure. Please try again later.  
  
### Limit Errors

Code |  Subcode |  Message  
---|---|---  
  
`4`

|

`2018022`

|

Too many send requests to phone numbers  
  
`100`

|

`2018109`

|

Attachment size exceeds allowable limit  
  
`613`

|

\--

|

Calls to this API have exceeded the rate limit  
  
### Bad Parameter Errors

Code |  Subcode |  Message  
---|---|---  
  
`100`

|

\--

|

Invalid `fbid`.  
  
`100`

|

`2018001`

|

No matching user found  
  
### Access Token Errors

Code |  Message  
---|---  
  
`190`

|

Invalid OAuth access token.  
  
### Permission Errors

Permission errors can occur for multiple reasons but generally fit into two
main categories:

  * A specific permission hasn't been [approved](/docs/messenger-platform/app-review)
  * The user hasn't opted-in to receiving messages from the page by using a [Messenger entry point](/docs/messenger-platform/product-overview/entry-points), or has deleted the conversation thread.

Code |  Subcode |  Message  
---|---|---  
  
`10`

|

`2018065`

|

This message is sent outside of allowed window. You need
[page_messaging_subscriptions permission](/docs/messenger-platform/policy-
overview#subscription_messaging) to be able to do it.  
  
`10`

|

`2018108`

|

This Person Cannot Receive Messages: This person isn't receiving messages from
you right now.  
  
`200`

|

`1545041`

|

Message Not Sent: This person isn't receiving messages from you right now.  
  
`200`

|

`2018028`

|

Cannot message users who are not admins, developers or testers of the app
until pages_messaging permission is reviewed and the app is live.  
  
`200`

|

`2018027`

|

Cannot message users who are not admins, developers or testers of the app
until pages_messaging_phone_number permission is reviewed and the app is live.  
  
`200`

|

`2018021`

|

Requires phone matching access fee to be paid by this page unless the
recipient user is an admin, developer, or tester of the app.  
  
### Account-Linking Errors

Code |  Message  
---|---  
  
`10303`

|

Invalid `account_linking_token`  
  
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

