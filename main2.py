import requests

TOKEN = '8406375358:AAEMsuxjVsR7EybRyw-pIpXJqCsFAy2e2UE'
TG_BASE_URL = f"https://api.telegram.org/bot{TOKEN}"
KURS_URL = 'https://cbu.uz/uz/arkhiv-kursov-valyut/json/'

def get_last_update():
    url = f"{TG_BASE_URL}/getUpdates"
    r = requests.get(url)
    data = r.json()
    return data["result"][-1]

def send_message(chat_id, text):
    url = f"{TG_BASE_URL}/sendMessage"
    requests.get(url, params={"chat_id": chat_id, "text": text})

def get_usd_rate(summa):
    data = requests.get(KURS_URL).json()
    for item in data:
        if item["Ccy"] == "USD":
            kurs = float(item["Rate"])
            natija = summa / kurs
            return f"{summa:,.0f} so‘m ≈ {natija:.2f} USD "

update = get_last_update()
chat_id = update["message"]["chat"]["id"]
text = update["message"]["text"]

if text == "/start":
    send_message(chat_id, "Salom")
elif text.isdigit():
    summa = float(text)
    send_message(chat_id, get_usd_rate(summa))
else:
    send_message(chat_id, "Iltimos, faqat raqam yuboring.")
