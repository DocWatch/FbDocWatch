#  Quick Start

This is a walkthrough to see the basics of the platform in action. Read the [
Complete Guide ](/docs/messenger-platform/product-overview/setup) to learn
about the platform in more detail.

##  Sample App

Download the [ sample app from Github
](https://l.facebook.com/l.php?u=https%3A%2F%2Fgithub.com%2Ffbsamples%2Fmessenger-
platform-samples&h=ATOifRe-aFgcgiqfSC7xv6Q_Ia5rNFhnn-
OqdGBRa7orzY00izwj9CrixWPEceDyIqugQC9NjudHVcV4BocBAR2pK-
rMTolZ88GaLBEYRtgdA-4X4-EWkXI9_XzHlXlhB2JI&s=1) to follow along with this
tutorial. You can run the sample app to see it in action.

[ Get Sample App
](https://l.facebook.com/l.php?u=https%3A%2F%2Fgithub.com%2Ffbsamples%2Fmessenger-
platform-samples&h=ATNsWK9ZYsfBgmhc8s03Nqj3iJO-
RtllX2c1iPySgb0IBEbhhvmnQvndM3gh4t24zbJ41Fs7O14l_dabQn1Yb2oZjRXUzGAK7Gsql64K3pTa7Ks2Hn59mI9anJNSmL2GqTd9&s=1)

_ _

##  Steps

###  1\. Create a Facebook App and Page

Create a new [ Facebook App ](https://developers.facebook.com/apps) and [ Page
](https://www.facebook.com/pages/create) or use existing ones. Go to the App
Dashboard and under Product Settings click "Add Product" and select
"Messenger."

![](https://scontent.xx.fbcdn.net/t39.2178-6/12995587_195576307494663_824949235_n.png)

###  2\. Setup Webhook

In the Webhooks section, click "Setup Webhooks."

![](https://scontent.xx.fbcdn.net/t39.2178-6/13331609_660771177408445_306127577_n.png)

Enter a URL for a webhook, enter a Verify Token and select ` messages ` and `
messaging_postbacks ` under Subscription Fields.

![](https://scontent.xx.fbcdn.net/t39.2178-6/12057143_211110782612505_894181129_n.png)

At your webhook URL, add code for verification. Your code should look for the
Verify Token and respond with the ` challenge ` sent in the verification
request. Click Verify and Save in the New Page Subscription to call your
webhook with a ` GET ` request.

In the sample app, this method is defined in ` app.js ` :

    
    
    app.get('/webhook', function(req, res) {
      if (req.query['hub.mode'] === 'subscribe' &&
          req.query['hub.verify_token'] === <VERIFY_TOKEN>) {
        console.log("Validating webhook");
        res.status(200).send(req.query['hub.challenge']);
      } else {
        console.error("Failed validation. Make sure the validation tokens match.");
        res.sendStatus(403);          
      }  
    });

###  3\. Get a Page Access Token

In the Token Generation section, select your Page. A Page Access Token will be
generated for you. Copy this Page Access Token. Note: The generated token will
NOT be saved in this UI. Each time you select that Page a new token will be
generated. However, any previous tokens created will continue to function.

![](https://scontent.xx.fbcdn.net/t39.2178-6/12995543_1164810200226522_2093336718_n.png)

###  4\. Subscribe the App to the Page

In the Webhooks section, you can subscribe the webhook for a specific page.

![](https://scontent.xx.fbcdn.net/t39.2178-6/13421551_1702530599996541_471321650_n.png)

###  5\. Receive Messages

Now that the subscription is completed, we need to listen for ` POST ` calls
at our webhook. All callbacks will be made to this webhook.

In our sample app, we handle the all of them. For receiving messages, we look
for the ` messagingEvent.message ` field and call the ` receivedMessage `
function.

    
    
    app.post('/webhook', function (req, res) {
      var data = req.body;
    
      // Make sure this is a page subscription
      if (data.object === 'page') {
    
        // Iterate over each entry - there may be multiple if batched
        data.entry.forEach(function(entry) {
          var pageID = entry.id;
          var timeOfEvent = entry.time;
    
          // Iterate over each messaging event
          entry.messaging.forEach(function(event) {
            if (event.message) {
              receivedMessage(event);
            } else {
              console.log("Webhook received unknown event: ", event);
            }
          });
        });
    
        // Assume all went well.
        //
        // You must send back a 200, within 20 seconds, to let us know
        // you've successfully received the callback. Otherwise, the request
        // will time out and we will keep trying to resend.
        res.sendStatus(200);
      }
    });
      
    function receivedMessage(event) {
      // Putting a stub for now, we'll expand it in the following steps
      console.log("Message data: ", event.message);
    }

###  6\. Send a Text Message

In ` receivedMessage ` , we've made logic to send a message back to the user.
The default behavior is to echo back the text that was received.

    
    
    function receivedMessage(event) {
      var senderID = event.sender.id;
      var recipientID = event.recipient.id;
      var timeOfMessage = event.timestamp;
      var message = event.message;
    
      console.log("Received message for user %d and page %d at %d with message:", 
        senderID, recipientID, timeOfMessage);
      console.log(JSON.stringify(message));
    
      var messageId = message.mid;
    
      var messageText = message.text;
      var messageAttachments = message.attachments;
    
      if (messageText) {
    
        // If we receive a text message, check to see if it matches a keyword
        // and send back the example. Otherwise, just echo the text we received.
        switch (messageText) {
          case 'generic':
            sendGenericMessage(senderID);
            break;
    
          default:
            sendTextMessage(senderID, messageText);
        }
      } else if (messageAttachments) {
        sendTextMessage(senderID, "Message with attachment received");
      }
    }

Put a stub for ` sendGenericMessage ` for now, we'll get to it later:

    
    
    function sendGenericMessage(recipientId, messageText) {
      // To be expanded in later sections
    }

` sendTextMessage ` formats the data in the request:

    
    
    function sendTextMessage(recipientId, messageText) {
      var messageData = {
        recipient: {
          id: recipientId
        },
        message: {
          text: messageText
        }
      };
    
      callSendAPI(messageData);
    }

` callSendAPI ` calls the Send API:

    
    
    function callSendAPI(messageData) {
      request({
        uri: 'https://graph.facebook.com/v2.6/me/messages',
        qs: { access_token: PAGE_ACCESS_TOKEN },
        method: 'POST',
        json: messageData
    
      }, function (error, response, body) {
        if (!error && response.statusCode == 200) {
          var recipientId = body.recipient_id;
          var messageId = body.message_id;
    
          console.log("Successfully sent generic message with id %s to recipient %s", 
            messageId, recipientId);
        } else {
          console.error("Unable to send message.");
          console.error(response);
          console.error(error);
        }
      });  
    }

Go to your Facebook Page and send a message to it. You should see the message
echoed back to you along with output to the logs.

![](https://scontent.xx.fbcdn.net/t39.2178-6/13331537_288414224831849_853132949_n.png)

###  7\. Send a Structured Message

` receivedMessage ` also sends back other kinds of messages for certain
keywords. If you send the message 'generic', it will call ` sendGenericMessage
` which sends back a Structured Message with a generic template.

    
    
    function sendGenericMessage(recipientId) {
      var messageData = {
        recipient: {
          id: recipientId
        },
        message: {
          attachment: {
            type: "template",
            payload: {
              template_type: "generic",
              elements: [{
                title: "rift",
                subtitle: "Next-generation virtual reality",
                item_url: "https://www.oculus.com/en-us/rift/",               
                image_url: "http://messengerdemo.parseapp.com/img/rift.png",
                buttons: [{
                  type: "web_url",
                  url: "https://www.oculus.com/en-us/rift/",
                  title: "Open Web URL"
                }, {
                  type: "postback",
                  title: "Call Postback",
                  payload: "Payload for first bubble",
                }],
              }, {
                title: "touch",
                subtitle: "Your Hands, Now in VR",
                item_url: "https://www.oculus.com/en-us/touch/",               
                image_url: "http://messengerdemo.parseapp.com/img/touch.png",
                buttons: [{
                  type: "web_url",
                  url: "https://www.oculus.com/en-us/touch/",
                  title: "Open Web URL"
                }, {
                  type: "postback",
                  title: "Call Postback",
                  payload: "Payload for second bubble",
                }]
              }]
            }
          }
        }
      };  
    
      callSendAPI(messageData);
    }

![](https://scontent.xx.fbcdn.net/t39.2178-6/13331576_291859617816127_1434046125_n.png)

###  8\. Handle Postbacks

In the last step, the Structured Message that is sent has postbacks. Postbacks
are back end calls to your webhook when buttons are tapped. These calls
contain the ` payload ` that is set for the button. Buttons on Structured
Messages support opening URLs and postbacks.

In our webhook handler, we handle the postback by calling ` receivedPostback `
:

    
    
    ...
            } else if (messagingEvent.postback) {
              receivedPostback(messagingEvent);          
    ...          

Which sends a message back saying that hte postback was called:

    
    
    function receivedPostback(event) {
      var senderID = event.sender.id;
      var recipientID = event.recipient.id;
      var timeOfPostback = event.timestamp;
    
      // The 'payload' param is a developer-defined field which is set in a postback 
      // button for Structured Messages. 
      var payload = event.postback.payload;
    
      console.log("Received postback for user %d and page %d with payload '%s' " + 
        "at %d", senderID, recipientID, payload, timeOfPostback);
    
      // When a postback is called, we'll send a message back to the sender to 
      // let them know it was successful
      sendTextMessage(senderID, "Postback called");
    }

_ _

##  Next Steps

Great! You've complete the walkthrough. The sample app contains more
functionality that you can explore, including the other Structured Message
templates and example of how to use the web plugins.

The [ Complete Guide ](/docs/messenger-platform/product-overview/setup) goes
into all the features in much more detail.

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

