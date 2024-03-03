from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def create_keyboard(func):
    def wrapper():
        keyboard = InlineKeyboardBuilder()
        func(keyboard)
        return keyboard.as_markup()

    return wrapper


@create_keyboard
def start(keyboard: InlineKeyboardBuilder):
    keyboard.row(InlineKeyboardButton(text='Русский язык 🇷🇺', callback_data='lang_choice:ru'))
    keyboard.row(InlineKeyboardButton(text='Қазақ тілі 🇰🇿', callback_data='lang_choice:kz'))


@create_keyboard
def get_doc(keyboard: InlineKeyboardBuilder):
    keyboard.row(InlineKeyboardButton(text='Изменить свою жизнь!', url='https://t.me/sultan_avi'))
    keyboard.row(InlineKeyboardButton(text='Доказательства ✅', callback_data='doc'))


@create_keyboard
def end(keyboard: InlineKeyboardBuilder):
    keyboard.row(InlineKeyboardButton(text='НАЧАТЬ РАБОТАТЬ!', url='https://t.me/sultan_avi'))


@create_keyboard
def bienvenido(keyboard: InlineKeyboardBuilder):
    keyboard.row(InlineKeyboardButton(text='Ejemplo de cómo funciona el programa', callback_data='get_video_notes'))
    keyboard.row(
        InlineKeyboardButton(text='Escríbeme ✍️', url='https://t.me/alvrz_jogo'),
        InlineKeyboardButton(text='Comentarios 👍', callback_data='get_comments')
    )
    keyboard.row(InlineKeyboardButton(text='📲 Descargar 📲', callback_data="choose_phones"))


@create_keyboard
def phones_select(keyboard: InlineKeyboardBuilder):
    keyboard.row(InlineKeyboardButton(text='Android', callback_data='get_phone:android'))
    keyboard.row(InlineKeyboardButton(text='iOS', callback_data='get_phone:ios'))


@create_keyboard
def get_me(keyboard: InlineKeyboardBuilder):
    keyboard.row(InlineKeyboardButton(text='✅ Obtener la aplicación ✅', url='https://t.me/alvrz_jogo'))


@create_keyboard
def get_stories_keyboard(keyboard: InlineKeyboardBuilder):
    keyboard.row(InlineKeyboardButton(text='📲 Descargar📲', callback_data="choose_phones"))


@create_keyboard
def todos(keyboard: InlineKeyboardBuilder):
    keyboard.row(InlineKeyboardButton(text="📲 Obtener la aplicación 📲", callback_data='choose_phones'))


admins = InlineKeyboardBuilder()
admins.row(InlineKeyboardButton(text="Начать рассылку", callback_data='start_sender'))
admins.row(InlineKeyboardButton(text="Получить статистику", callback_data='get_stat'))


note_or_video = InlineKeyboardBuilder()
note_or_video.row(InlineKeyboardButton(text="Видео", callback_data="admin_sender_choice:video"))
note_or_video.row(InlineKeyboardButton(text="Кружок", callback_data="admin_sender_choice:video_note"))


start_sender_or_not = InlineKeyboardBuilder()
start_sender_or_not.row(InlineKeyboardButton(text="✅", callback_data="sender_start:yes"))
start_sender_or_not.row(InlineKeyboardButton(text="❌", callback_data="sender_start:no"))


type_of_push = InlineKeyboardBuilder()
type_of_push.row(InlineKeyboardButton(text="Мгновенный пуш", callback_data="instant_push"))
# type_of_push.row(InlineKeyboardButton(text="Ежедневный пуш", callback_data="every_day_push"))
# type_of_push.row(InlineKeyboardButton(text="Отложенный пуш", callback_data="time_push"))


sender_example_urls = InlineKeyboardBuilder()
sender_example_urls.row(InlineKeyboardButton(text="🔥 Стратегия 🔥", url='https://example.com'))
sender_example_urls.row(InlineKeyboardButton(text="💰 Лучшие выигрыши 💰", url='https://example1.com'))

no_buttons = InlineKeyboardBuilder()
no_buttons.row(InlineKeyboardButton(text="В этой рассылке не нужны кнопки", callback_data="no_buttons"))