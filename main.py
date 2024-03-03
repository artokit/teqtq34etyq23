import asyncio
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from routers import user, admin, sender

TOKEN = '7031021822:AAFY0OQUncOVoMbYhGtxWMF7eHlb1T7oZUc'
bot = Bot(TOKEN)

dp = Dispatcher(storage=MemoryStorage())
dp.include_routers(user.router, admin.router)
sender.set_bot(dp, bot)
sender.init_handlers()
asyncio.run(dp.start_polling(bot))
