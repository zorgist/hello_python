import json

def handler(event, context):
    # Telegram шлёт весь update в event['body']
    upd = json.loads(event['body'])
    chat_id = upd["message"]["chat"]["id"]

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({
            "method": "sendMessage",
            "chat_id": chat_id,
            "text": "Привет, cloud!"
        })
    }
