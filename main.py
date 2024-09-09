from pyrogram import Client, filters

app = Client("crypto_exchange_bot", api_id="ВАШ_API_ID", api_hash="ВАШ_API_HASH", bot_token="7278576205:AAH0iW-ftAvjlnaIv0QrRasbAP6WG-09gd4")

# Приветственное сообщение
@app.on_message(filters.command("start"))
def start(client, message):
    message.reply("Добро пожаловать в наш крипто-обменник! Используйте команду /exchange для обмена валют.")

# Пример команды для обмена валют
@app.on_message(filters.command("exchange"))
def exchange(client, message):
    message.reply("Введите сумму и валюту, которую хотите обменять.")

app.run()