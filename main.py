import requests
import time
import os
import random

BOT_TOKEN = os.getenv("BOT_TOKEN", "8928951011:AAG6D0Jv-C5FZNQqyVwWnaac9Dyyd8J3eBc")
CHAT_ID = "8673506776"

API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

messages = [
    "Teri Maa Ki Chut",
    "1600 rupay dede wapas address leak kr duga tera cyber me report kar dunga",
    "teri bot ki maa chod di hai",
    "tumari maa chhod dunga",
]

# While loop

while True:
    msg = random.choices(messages)[0]
    payload = {
        "chat_id": CHAT_ID,
        "text": msg
    }

    response = requests.post(
        API_URL,
        json=payload,
        timeout=15
    )

    if response.ok:
        print(f"Sent: {msg}")
    else:
        print("Error:", response.text)
        break
    time.sleep(2)

print("All messages processed!")
