from telethon import TelegramClient
import asyncio
from flask import Flask

# Инициализация Flask
app = Flask(__name__)

# Ваши данные для подключения
api_id = 26071362  # Замените на свой api_id
api_hash = 'c3d12bc02851cde9de371fa1a919bd76'  # Замените на свой api_hash
phone_number = '+77712388254'  # Ваш номер телефона

# Инициализация клиента
client = TelegramClient('session_name', api_id, api_hash)

@app.route('/')
def home():
    return "Telegram Bot is running!"

async def send_gift_message():
    chat_id = 1266771326  # ID вашего чата
    message = ".отн сделать завтрак"

    while True:
        await client.send_message(chat_id, message)
        await asyncio.sleep(540)  # Ожидание 6 минут

async def main():
    await client.start(phone_number)
    await send_gift_message()

# Запуск Flask в отдельном потоке
if __name__ == "__main__":
    from threading import Thread

    # Запуск Flask в фоновом режиме
    thread = Thread(target=app.run)
    thread.daemon = True
    thread.start()

    # Запуск Telegram клиента
    asyncio.run(main())
