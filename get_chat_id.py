from telethon import TelegramClient
import asyncio

# Твои данные для подключения
api_id = 26071362  # Заменить на свой api_id
api_hash = 'c3d12bc02851cde9de371fa1a919bd76'  # Заменить на свой api_hash
phone_number = '+77712388254'  # Твой номер телефона

# Инициализация клиента с сессией
client = TelegramClient('session_name', api_id, api_hash)

async def send_gift_message():
    chat_id = 1266771326  # ID твоего чата

    # Сообщение, которое нужно отправить
    message = ".отн сделать завтрак"

    while True:
        # Отправляем сообщение
        await client.send_message(chat_id, message)

        # Ждем  6минут (360 секунд)
        await asyncio.sleep(360)

async def main():
    # Авторизация
    await client.start(phone_number)

    # Запуск функции отправки сообщений каждые 6 минут
    await send_gift_message()

# Запуск клиента
with client:
    client.loop.run_until_complete(main())
