from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# стартовая клавиатура

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Проверить IMEI устройства')
        ]
    ], resize_keyboard=True
)

# клавиатура для остановки машины состояний

stop_fsm_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='В главное меню')
        ]
    ], resize_keyboard=True
)
