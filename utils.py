import os
from aiogram import Bot
from aiogram.types import FSInputFile

HASHED = {}
MEDIA_PATH = os.path.join(os.path.dirname(__file__), 'media')


async def send_video(bot: Bot, user_id: int, path: str, **kwargs):
    if path in HASHED:
        return await bot.send_video(user_id, HASHED[path], **kwargs)

    message = await bot.send_video(user_id, FSInputFile(os.path.join(MEDIA_PATH, 'videos', path)), **kwargs)
    HASHED[path] = message.video.file_id
