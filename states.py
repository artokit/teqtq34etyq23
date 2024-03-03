from aiogram.fsm.state import StatesGroup, State


class SendPhoto(StatesGroup):
    send_photos = State()


class SendSenderMessage(StatesGroup):
    send_message = State()
    enter_urls = State()
    time_for_push = State()


class AdminListManage(StatesGroup):
    add_admin = State()
    delete_admin = State()


class SenderStates(StatesGroup):
    send_media = State()
    send_caption = State()
    send_urls = State()
    final = State()


class EditMessage(StatesGroup):
    edit_content = State()
    edit_attachment = State()
    edit_keyboard = State()


class EditKeyboardMessage(StatesGroup):
    send_buttons = State()
    agree = State()
