from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import os
from scripingc_weather import json_text

app=Flask(__name__)

# Get environment variables
YOUR_CHANNEL_ACCESS_TOKEN = "YOUR_CHANNEL_ACCESS_TOKEN"
YOUR_CHANNEL_SECRET = "YOUR_CHANNEL_SECRET"
line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)

@app.route("/callback", methods=["POST"])
def callback():
    signature=request.headers["X-Line-Signature"]

    body=request.get_data(as_text=True)
    app.logger.info("Request body"+body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return "OK"

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):

    # Storage of the entered character string
    push_text = event.message.text

    # String to reply
    if push_text == "天気":
        reply_text = json_text
    else:
        reply_text = push_text

    # Description of reply part
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=reply_text))

if __name__=="__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)