#  Audio Attachment

You can send sounds by uploading them or sharing a URL using the [ Send API
](/docs/messenger-platform/send-api-reference#request) .

![](https://scontent.xx.fbcdn.net/t39.2365-6/13503473_1584526905179825_88080075_n.png)

##  Examples

URL send

    
    
    curl -X POST -H "Content-Type: application/json" -d '{
      "recipient":{
        "id":"USER_ID"
      },
      "message":{
        "attachment":{
          "type":"audio",
          "payload":{
            "url":"https://petersapparel.com/bin/clip.mp3"
          }
        }
      }
    }' "https://graph.facebook.com/v2.6/me/messages?access_token=PAGE_ACCESS_TOKEN"    

File upload

    
    
    curl  \
      -F 'recipient={"id":"USER_ID"}' \
      -F 'message={"attachment":{"type":"audio", "payload":{}}}' \
      -F 'filedata=@/tmp/clip.mp3;type=audio/mp3' \
      "https://graph.facebook.com/v2.6/me/messages?access_token=PAGE_ACCESS_TOKEN"    

##  Fields

###  ` attachment ` object

Property Name  |  Description  |  Required  
---|---|---  
  
` type `

|

` audio `

|

Y  
  
` payload.url `

|

URL of audio

|

Y  
  
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

