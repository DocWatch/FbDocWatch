#  Account Linking Url

You can configure the thread to help users link or unlink their Messenger
identity with their identity in your business. Read the [ Account Linking
documentation ](/docs/messenger-platform/account-linking) to learn more about
this process.

Configuring Account Linking on the thread allows users to:

  * Link their account from the Thread Details of the business 
  * Unlink their account, if already linked 

##  Example

    
    
    curl -X POST -H "Content-Type: application/json" -d '{
      "setting_type" : "account_linking",
      "account_linking_url" : "https://www.example.com/oauth?response_type=code&client_id=1234567890&scope=basic"
    }' "https://graph.facebook.com/v2.6/me/thread_settings?access_token=PAGE_ACCESS_TOKEN"    

##  Fields

Property Name  |  Description  |  Required  
---|---|---  
  
` setting_type `

|

Must be ` account_linking `

|

Y  
  
` account_linking_url `

|

URL to the account linking OAuth flow

|

Y  
  
  * ` account_linking_url ` starts a authentication flow to log the user and link the account on your back-end. Read the [ Link Account documentation ](/docs/messenger-platform/account-linking/link-account#authentication) for more information. 

##  Response

If the Account Linking URL was successfully set, you will get the following
response:

    
    
    {
      "result": "Account linking url added"
    }    

##  Delete

In order to delete the Account Linking URL send a ` DELETE ` request:

    
    
    curl -X DELETE -H "Content-Type: application/json" -d '{
      "setting_type":"account_linking"
    }' "https://graph.facebook.com/v2.6/me/thread_settings?access_token=PAGE_ACCESS_TOKEN"    

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

