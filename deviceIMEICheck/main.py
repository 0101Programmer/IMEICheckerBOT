from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup

from bot_config import API_BOT, WHITE_USES_LIST, API_SANDBOX, SERVICE_ID, BASE_URL
from imei_checker import IMEIChecker
from keyboards import start_kb, stop_fsm_kb

bot = Bot(token=API_BOT)
dp = Dispatcher(bot, storage=MemoryStorage())
imei_checker = IMEIChecker(API_SANDBOX, SERVICE_ID, BASE_URL)


# класс для машины состояний для проверки устройства по IMEI

class IMEICheckState(StatesGroup):
    device_imei = State()


# обработчик коканды start

@dp.message_handler(commands=["start"])
async def start_message(message):
    await message.answer("Выберите действие", reply_markup=start_kb)


# проверка id пользователя на нахождение в белом листе

@dp.message_handler(text="Проверить IMEI устройства")
async def imei_check(message):
    if str(message.from_user.id) not in WHITE_USES_LIST:
        await message.answer("Доступ запрещён")
        print(message.from_user.id)
    else:
        await message.answer("Введите IMEI номер")
        await IMEICheckState.device_imei.set()


# запуск машины состояний, чтобы проверять imei циклично, пока не будет введена команда для её остановки

@dp.message_handler(state=IMEICheckState.device_imei)
async def fsm_handler(message, state):
    if message.text == "В главное меню":
        await state.finish()
        await message.answer("Выберите действие", reply_markup=start_kb)
    else:
        await message.answer(imei_checker.request_maker(message.text), reply_markup=stop_fsm_kb)
        await message.answer("Введите IMEI номер")


# обработчик всех сообщений

@dp.message_handler()
async def all_messages(message):
    await message.answer("Введите команду /start, чтобы проверить устройство по IMEI")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
