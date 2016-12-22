#  Domain Whitelisting

Some features like [ Messenger Extensions ](/docs/messenger-platform/send-api-
reference/webview) and [ Checkbox Plugin ](/docs/messenger-platform/plugin-
reference/checkbox-plugin) require a page to specify a domain whitelist.

##  Creating

    
    
    curl -X POST -H "Content-Type: application/json" -d '{
      "setting_type" : "domain_whitelisting",
      "whitelisted_domains" : ["https://petersfancyapparel.com"],
      "domain_action_type": "add"
    }' "https://graph.facebook.com/v2.6/me/thread_settings?access_token=PAGE_ACCESS_TOKEN"

###  Fields

Property Name  |  Description  |  Type  |  Required  
---|---|---|---  
  
` setting_type `

|

Must be ` domain_whitelisting ` .

|

String

|

Y  
  
` whitelisted_domains `

|

A list of domains being used. All domains must be valid and use https. Up to
10 domains allowed.

|

Array

|

Y  
  
` domain_action_type `

|

Operation when setting domain. Valid values: ` add ` , ` remove `

|

Enum

|

Y  
  
##  Reading

    
    
    curl -i -X GET "https://graph.facebook.com/v2.6/me/thread_settings?fields=whitelisted_domains&access_token=PAGE_ACCESS_TOKEN"

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

