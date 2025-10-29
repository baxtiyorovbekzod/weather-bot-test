import requests

TOKEN = '8024406467:AAGt2mfZudKBRZcS8qBwuwD-narPbw-RbbA'
TG_BASE_URL = f"https://api.telegram.org/bot{TOKEN}"
WEATHER_URL = "http://api.weatherapi.com/v1"

def get_last_update():
    url = f"{TG_BASE_URL}/getUpdates"
    response = requests.get(url)
    data = response.json()
    return data["result"][-1] 

def send_message(chat_id, text):
    url = f"{TG_BASE_URL}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    requests.get(url, params=payload)

def get_weather(city):
    url = f"{WEATHER_URL}/current.json"
    payload = {"key": "c852ebca46f148469f3172212250707", "q": city}
    response = requests.get(url, params=payload)
    data = response.json()
    return data["current"]["feelslike_c"]



last_update = get_last_update()
chat_id = last_update["message"]["chat"]["id"]
text = last_update["message"]["text"].lower()

if text == "/start":
    send_message(chat_id, "Salom 👋")
elif text:
    try:
        weather = get_weather(text)
        send_message(chat_id, f"Hozir {text.title()}da {weather}°C harorat ")
    except:
        send_message(chat_id, " Ob-havo topilmadi. Shahar nomini to‘g‘ri yozing.")