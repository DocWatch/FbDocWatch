#  Video Attachment

You can send videos by uploading them or sharing a URL using the [ Send API
](/docs/messenger-platform/send-api-reference#request) .

![](https://scontent.xx.fbcdn.net/t39.2365-6/13509239_1608341092811398_289173120_n.png)

##  Examples

URL send

    
    
    curl -X POST -H "Content-Type: application/json" -d '{
      "recipient":{
        "id":"USER_ID"
      },
      "message":{
        "attachment":{
          "type":"video",
          "payload":{
            "url":"https://petersapparel.com/bin/clip.mp4"
          }
        }
      }
    }' "https://graph.facebook.com/v2.6/me/messages?access_token=PAGE_ACCESS_TOKEN"    

File upload

    
    
    curl  \
      -F 'recipient={"id":"USER_ID"}' \
      -F 'message={"attachment":{"type":"video", "payload":{}}}' \
      -F 'filedata=@/tmp/clip.mp4;type=video/mp4' \
      "https://graph.facebook.com/v2.6/me/messages?access_token=PAGE_ACCESS_TOKEN"    

##  Fields

###  ` attachment ` object

Property Name  |  Description  |  Required  
---|---|---  
  
` type `

|

` video `

|

Y  
  
` payload.url `

|

URL of video binary

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

