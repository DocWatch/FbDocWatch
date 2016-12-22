#  Account Linking Callback

This callback will occur when the [ Linked Account ](/docs/messenger-
platform/account-linking/link-account) or [ Unlink Account ](/docs/messenger-
platform/account-linking/unlink-account) call-to-action have been tapped. The
` status ` parameter is set to inform you whether the user linked or unlinked
their account. The ` authorization_code ` is a pass-through parameter.
allowing you to match the business user entity to the page-scoped ID (PSID) of
the ` sender ` .

##  Example

    
    
    {
      "sender":{
        "id":"USER_ID"
      },
      "recipient":{
        "id":"PAGE_ID"
      },
      "timestamp":1234567890,
      "account_linking":{
        "status":"linked",
        "authorization_code":"PASS_THROUGH_AUTHORIZATION_CODE"
      }
    }    
    
    
    {
      "sender":{
        "id":"USER_ID"
      },
      "recipient":{
        "id":"PAGE_ID"
      },
      "timestamp":1234567890,
      "account_linking":{
        "status":"unlinked"
      }
    }    

##  Fields

###  ` account_linking ` object

Field Name  |  Description  |  Type  
---|---|---  
  
` status `

|

` linked ` or ` unlinked `

|

String  
  
` authorization_code `

|

Value of pass-through ` authorization_code ` provided in the [ Linking Account
](/docs/messenger-platform/account-linking/link-account) flow

|

String  
  
  * ` authorization_code ` is only available when ` status ` is ` linked `

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

