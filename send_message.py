import requests
from datetime import datetime

BOT_ID = "fa77ac4c89ecda732bb0356aab"
URL = "https://api.groupme.com/v3/bots/post"

# You can change this message anytime
message = "🙏 Reminder: Prayer meeting is coming this Monday at 7am!"

payload = {
    "bot_id": BOT_ID,
    "text": message
}

response = requests.post(URL, json=payload)

if response.status_code == 202:
    print(f"[SUCCESS] Message sent at {datetime.now()}")
else:
    print(f"[ERROR] Status: {response.status_code}")
    print(response.text)