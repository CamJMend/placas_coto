### whatsapp.py
import requests

def send_whatsapp_message(phone, message):
    url = "https://api.callmebot.com/whatsapp.php"
    params = {
        "phone": phone,
        "text": message,
        "apikey": "TU_API_KEY"
    }
    requests.get(url, params=params)