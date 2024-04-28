from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = Flask(__name__)

line_bot_api = LineBotApi('8ImLXjRsaTvVqjAzllz2ntZbltx1gFn61GNbkQFHHpDkDDfRJH0NLaonlUzuGSZB69k6EFnwhqC4ykH2oeQHQbf6EpfR1wzAbU6LOMfPKZW8lVE5ZAG9em5Ons13XmrxV/MvENBrP/+3q3oNWHhY+gdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('3abb4d91e161ccee1a33c44b7dfbf41d')

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))

if __name__ == "__main__":
    app.run()
