# User Profile API

The profile API can be used to query more information about the user, and
personalize the experience further. This API is only available after the user
initiated the conversation by sending a message or by interacting with a [Web
Plugin](/docs/messenger-platform/plugin-reference).

If the conversation was initiated by using a phone number (customer
matching]), you will only be able to use this API after the user replied to
your message.

## Request

In order to use the User Profile API, make a `GET` call to
`https://graph.facebook.com/v2.6/<USER_ID>?access_token=PAGE_ACCESS_TOKEN`.

### Example

    
    
    curl -X GET "https://graph.facebook.com/v2.6/<USER_ID>?fields=first_name,last_name,profile_pic,locale,timezone,gender&access_token=PAGE_ACCESS_TOKEN"    

### Fields

Field Name |  Description  
---|---  
  
`first_name`

|

First name  
  
`last_name`

|

Last name  
  
`profile_pic`

|

Profile picture  
  
`locale`

|

Locale of the user on Facebook  
  
`timezone`

|

Timezone, number relative to GMT  
  
`gender`

|

Gender  
  
`is_payment_enabled`

|

Is the user eligible to receive messenger platform payment messages  
  
__

## Response

A successful User Profile API request returns a json string with the requested
details about the user.

### Example

    
    
    {
      "first_name": "Peter",
      "last_name": "Chang",
      "profile_pic": "https://fbcdn-profile-a.akamaihd.net/hprofile-ak-xpf1/v/t1.0-1/p200x200/13055603_10105219398495383_8237637584159975445_n.jpg?oh=1d241d4b6d4dac50eaf9bb73288ea192&oe=57AF5C03&__gda__=1470213755_ab17c8c8e3a0a447fed3f272fa2179ce",
      "locale": "en_US",
      "timezone": -7,
      "gender": "male"
    }    

The information at this API is only available after a person has sent a
message to your bot or clicked the "Send to Messenger" plugin. If you call the
API before these actions, then you will receive an empty result. You will also
receive an empty result if a person has revoked platform permissions on
Facebook.

    
    
    {}

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

