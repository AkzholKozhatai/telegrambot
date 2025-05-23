from telethon import TelegramClient
import asyncio
from flask import Flask
import os
from threading import Thread

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

async def send_trip_message():
    chat_id = 1266771326  # ID вашего чата
    message = ".отн приятные воспоминания"

    while True:
        try:
            await client.send_message(chat_id, message)
            print(f"Сообщение отправлено в чат {chat_id}: {message}")
        except Exception as e:
            print(f"Ошибка отправки сообщения: {e}")
        await asyncio.sleep(4800)  # Ожидание 46 минут (2760 секунд)

async def send_farm_message():
    chat_id = 1266771326  # ID вашего чата
    message = "ферма"

    while True:
        try:
            await client.send_message(chat_id, message)
            print(f"Сообщение отправлено в чат {chat_id}: {message}")
        except Exception as e:
            print(f"Ошибка отправки сообщения: {e}")
        await asyncio.sleep(14700)  # Ожидание 245 минут (14700 секунд)

async def main():
    # Автоматический вход с использованием существующей сессии
    await client.start()
    print("Telegram клиент запущен.")
    # Параллельное выполнение двух задач
    task1 = asyncio.create_task(send_trip_message())
    task2 = asyncio.create_task(send_farm_message())
    
    # Следим за выполнением задач
    await asyncio.gather(task1, task2)

# Запуск Flask в отдельном потоке
def run_flask():
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

# Запуск приложения
if __name__ == "__main__":
    # Запуск Flask в фоновом режиме
    thread = Thread(target=run_flask)
    thread.daemon = True
    thread.start()

    # Запуск Telegram клиента
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
