import asyncio
import os.path
from aiogram import Router, F
from aiogram.filters import Command, ChatMemberUpdatedFilter, KICKED
from aiogram.types import Message, CallbackQuery, FSInputFile, ChatMemberUpdated
from aiogram.utils.media_group import MediaGroupBuilder
import keyboards
from database.models import Stat, User
from utils import send_video, MEDIA_PATH

router = Router()
TEXTS = {
    'start': {
        'kz': 'Салем алейкум! Менің атым Султан!😎\n\n'
              'Мені бұрын танысаң, несиең мен қарызыңды баяғыда жауып тастар едің! Крутой машина сатып алып, VIP ҚАЗАҚ сияқты өмір сүрер едім!💸\n\n'
              '👇Осы тарихи қатені түзетіңіз, маған «VIP» деп жазыңыз, мен сізге 200% алынатын сигналдарды беремін:',
        'ru': 'Саламалйкум! Я Султан! 😎\n\n'
              'Если бы ты меня знал раньше, то давно закрыл бы все кредиты и долги! Купил бы крутую машину и жил бы как ВИП КАЗАХ! 💸\n\n'
              'Да-да, просто напиши мне, и я тебе помогу!\n'
              'Для старта нужно от 3 000 тенге!\n\n'
              '👇Исправь эту историческую ошибку, напиши мне "ВИП" и дам тебе сигналы с которые заходят 200%:'
    }
}


@router.message(Command('start'))
async def start(message: Message):
    is_new_user = User.add_user(message.chat.id, message.chat.username)
    if is_new_user:
        Stat.increment_stat()

    await message.answer(
        "🇷🇺Выбери нужный язык\n\n"
        "🇰🇿 Қалаған тілді таңдаңыз\n\n"
        "👇",
        reply_markup=keyboards.start()
    )


@router.callback_query(F.data.startswith('lang_choice'))
async def lang_choice(call: CallbackQuery):
    await send_video(call.bot, call.message.chat.id, 'start.mp4')
    lang = call.data.split(':')[1]
    await call.message.answer(TEXTS['start'][lang], reply_markup=keyboards.get_doc())


@router.callback_query(F.data == 'doc')
async def get_doc_text(call: CallbackQuery):
    await call.message.answer(
        'Я понимаю что ты не понимаешь почему я помогаю другим, но поверь, как только ты заработаешь больше 100 тысяч тенге, а ты можешь сделать это уже сегодня, то твои 25% которые ты скинешь мне, будут кормить меня еще очень долго😎\n\n'
        'Лови отзывы👇'
    )

    media = MediaGroupBuilder()
    for i in range(10):
        media.add_photo(
            media=FSInputFile(os.path.join(MEDIA_PATH, 'photos', f'{i}.jpg')),
            caption='Вот отзыв тех, кто уже поднял деньги вместе со мной, а на их месте можешь быть ты.' if i == 0 else None
        )

    await call.bot.send_media_group(call.message.chat.id, media=media.build())
    await asyncio.sleep(1)
    await call.message.answer(
        'Как ты видишь, я работаю честно, ведь чем больше заработаешь ты - тем больше заработаю и я💰\n\n'
        'Пиши мне и начинай работу уже сейчас',
        reply_markup=keyboards.end()
    )


@router.my_chat_member(ChatMemberUpdatedFilter(member_status_changed=KICKED))
async def check_bot(event: ChatMemberUpdated):
    Stat.add_block_user(event.chat.id)
