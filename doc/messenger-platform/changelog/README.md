#  Messenger Platform Changelog

This changelog covers what's changed in the Messenger Platform APIs. These
changes include server-side APIs, web plugins, mobile apps and other services.

##  November 8th, 2016

  * Support for [ Ref Param in m.me links ](/docs/messenger-platform/referral-params)
  * New [ Checkbox Plugin ](/docs/messenger-platform/plugin-reference/checkbox-plugin)
  * New [ List Template ](/docs/messenger-platform/send-api-reference/list-template)
  * [ Tokenized Payments ](/docs/messenger-platform/complete-guide/payments#tokenized_payment) support. Payments still in BETA, [ request access ](https://www.facebook.com/messenger_platform/payments_requestaccess) . 
  * Better [ Testing for Payments ](/docs/messenger-platform/complete-guide/payments#test_payments) . You don't have to be whitelisted to start testing. 
  * Added list of apps running a page. You can find it in to Page Settings/Messaging tab. 
  * Improved error reporting and [ clear subcodes ](/docs/messenger-platform/send-api-reference#errors)
  * Deprecation announcement: seq id field on inbound messages 

_ _

##  September 12th, 2016

  * Introduced [ Payments ](/docs/messenger-platform/complete-guide/payments) in beta! Request access through this [ form. ](https://www.facebook.com/messenger_platform/payments_requestaccess)
    * For native payments use new [ Buy Button ](/docs/messenger-platform/send-api-reference/buy-button) along with Generic template 
    * For payments from the web see [ Webviews and Extensions ](/docs/messenger-platform/send-api-reference/webview)
  * Added [ Webviews and Extensions ](/docs/messenger-platform/send-api-reference/webview) to get user id for personalization, close the webview and call payments in the browser 
  * Added [ Share Button ](/docs/messenger-platform/send-api-reference/share-button) type (currently supported in Generic template only) so that people can share message bubbles 
  * Added [ Icons support to Quick Replies ](/docs/messenger-platform/send-api-reference/quick-replies)
  * Added [ Location Quick Reply type ](/docs/messenger-platform/send-api-reference/quick-replies)
  * Added webview_height_ratio parameter for [ Url Button ](/docs/messenger-platform/send-api-reference/url-button) to customize webview height 
  * Added [ attachments reuse support ](/docs/messenger-platform/send-api-reference#attachment_reuse) so that you don't have to upload the same attachments every time 

Also:

  * [ Messenger destination ](/docs/messenger-platform/product-overview/entry-points#ads) ad type is now available under the website clicks objective - that means you can acquire users directly into your bot with no friction 
  * Export your [ bot analytics ](/docs/messenger-platform/product-overview/analytics#export) on the app level to see block rates and open threads for all your pages. 
  * [ New welcome screen ](/docs/messenger-platform/product-overview/conversation#welcome_screen) when people first enter a conversation with your bot 

_ _

##  August 30th, 2016

  * Added client-side events for the [ "Send to Messenger" plugin ](/docs/messenger-platform/plugin-reference/send-to-messenger#event)

_ _

##  August 15th, 2016

  * Added a new doc: [ Messenger Platform Policy Overview ](/docs/messenger-platform/policy-overview) . Please review as policy changes may impact your integration. 
  * Re-added the Complete Guide which has now been broken up into multiple sections. 
  * Doc navigation changes. 

_ _

##  July 1st, 2016

###  Send API

  * [ Video ](/docs/messenger-platform/send-api-reference/video-attachment) , [ audio ](/docs/messenger-platform/send-api-reference/audio-attachment) , [ gif ](/docs/messenger-platform/send-api-reference/image-attachment) and [ file ](/docs/messenger-platform/send-api-reference/file-attachment) sends. Support both URLs and file upload. 
  * [ Sender Actions ](/docs/messenger-platform/send-api-reference/sender-actions) : set read receipts and typing indicators. 

###  Receive API

  * New event: [ message_echoes ](/docs/messenger-platform/webhook-reference/message-echo) . Allows developers to receive all messages sent by pages. 
  * New event: [ message_reads ](/docs/messenger-platform/webhook-reference/message-read) . To notify the developer/page a message was read. 
  * New field: [ app_id ](/docs/messenger-platform/webhook-reference/message-echo#format) , to identify the source of the bot message. 
  * New field: [ metadata ](/docs/messenger-platform/send-api-reference#message) , passed from the Send API and sent to the message_echoes callback, to help interoperability betwen multiple bots. 

###  User experience

  * ** Breaking change ** : [ Get Started button ](/docs/messenger-platform/thread-settings/get-started-button) . Triggers a [ postback received callback ](/docs/messenger-platform/webhook-reference/postback-received) instead of firing a message automatically. 
  * New input style: [ Quick replies ](/docs/messenger-platform/send-api-reference/quick-replies) . A new way for bots to receive input with ephemeral buttons attached to the last message 
  * New button type: [ Phone number ](/docs/messenger-platform/send-api-reference/button-template#fields) to invoke the native phone dialer 
  * New thread setting: [ Persistent menu ](/docs/messenger-platform/thread-settings/persistent-menu) . Supports postbacks and urls with up to five elements 
  * New thread setting: [ Greeting text ](/docs/messenger-platform/thread-settings/greeting-text) . To communicate your bot's functionality to first-time users. 
  * [ Browser close ](/docs/messenger-platform/send-api-reference/button-template#close_window) . To allow automatically closing the browser window at the end of a custom web UI flow. 
  * [ Account linking and unlinking ](/docs/messenger-platform/account-linking) : secure protocol for businesses to retrieve a page scoped user ID from within Messenger 
  * [ Bot feedback ](/docs/messenger-platform/product-overview/analytics#ratings) : Users are able to leave a 5-star review and provide feedback for developers. 

_ _

##  April 12th, 2016

  * Messenger Platform launched. 

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

