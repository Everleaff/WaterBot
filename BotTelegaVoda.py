# Импорт необходимых библиотек и модулей.
# Для написания данного бота была использована версия aiogram 2.25.1
from aiogram import Bot,Dispatcher,types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import Message


import random
import sqlite3
import time

################################################################################################

API_TOKEN = '6876194258:AAG__pxBh9dTJ0gBc9LKdFvMA5Wrneemr4U'
# Задание токена бота и создание объектов Bot и Dispatcher для работы с Telegram API.
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

################################################################################################

# ------------------------------------------------------------------------------------------------------ #
# Обработчик команды /start, который формирует клавиатуру с вариантами действий для пользователя.
@dp.message_handler(commands=['start'])
async def rabotaem(message: types.Message):
    user_id = message.from_user.id
    kb = [
            [types.KeyboardButton(text="Виды воды которые имееются в наличии")],
            [types.KeyboardButton(text="Прочие товары")],
            [types.KeyboardButton(text="Я хочу сделать заказ")]
         ]
    if user_id == 876197281:
         kb.append([types.KeyboardButton(text="Доставка")])
    
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("Приветсвую вас, выберите интересующую вас услугу.", reply_markup=keyboard)
# ------------------------------------------------------------------------------------------------------ #
# Обработчик текстовых сообщений пользователя, который реагирует на определенные ключевые слова и выполняет соответствующие действия.
@dp.message_handler(content_types=['text'])
async def text_otvet(message: types.Message):
    
    try:
        if (message.text).lower() == 'виды воды которые имееются в наличии':
            await message.answer('Запрос принят. Пожалуйста, подождите...')
            conn = sqlite3.connect('water_delivery.db')
            result = conn.execute('SELECT id, name, type, description, price FROM base_clinets')
            output = ''
            for row in result.fetchall():
                output += f'—————————ID:{row[0]}—————————\n\n'
                output += f'Название:\n{row[1]}\n\n'
                output += f'Тип:\n{row[2]}\n\n'
                output += f'Описание:\n{row[3]}\n\n'
                output += f'Цена:\n{row[4]}\n\n'
                output += '————————————————————\n\n'
            time.sleep(2)
            await message.answer(output)
            conn.close()
            
        if (message.text).lower() == 'прочие товары':
            await message.answer('Запрос принят. Пожалуйста, подождите...')
            conn = sqlite3.connect('water_delivery.db')
            result = conn.execute('SELECT * FROM base_items')
            output = ''
            for row in result.fetchall():
                output += f'—————————ID:{row[0]}—————————\n\n'
                output += f'Название:\n{row[1]}\n\n'
                output += f'Описание:\n{row[2]}\n\n'
                output += f'Цена:\n{row[3]}\n\n'
                output += 'По всем вопросам звоните: +7 914 555 55 55\n\n'
                output += '————————————————————\n\n'
            time.sleep(2)
            await message.answer(output)
            conn.close()
            
        if (message.text).lower() == 'доставка':
            await message.answer('Запрос принят. Пожалуйста, подождите...')
            conn = sqlite3.connect('water_delivery.db')
            result = conn.execute('SELECT * FROM base_orders')
            output = ''
            for row in result.fetchall():
                output += f'—————————ID:{row[0]}—————————\n\n'
                output += f'Имя:\n{row[1]}\n\n'
                output += f'Адрес:\n{row[2]}\n\n'
                output += f'Вид воды:\n{row[3]}\n\n'
                output += f'Количество булылей:\n{row[4]}\n\n'
                output += f'Подъезд:\n{row[5]}\n\n'
                output += f'Этаж:\n{row[6]}\n\n'
                output += f'Квартира:\n{row[7]}\n\n'
                output += f'Комментарий к заказу:\n{row[8]}\n\n'
                output += '————————————————————\n\n'
            time.sleep(2)
            await message.answer(output)
            conn.close()

        if (message.text).lower() == 'я хочу сделать заказ':
            await message.answer("Принято. Обработка запроса...")
            time.sleep(2)
            await message.answer("Введите ваше имя")
            await State.get_client_name.set()
        else:
            message.text
    except:
        await message.answer("Ошибка запроса.") 
        
# ------------------------------------------------------------------------------------------------------ #        
################################## ДОБАВЛЕНИЕ НОВОГО ЗАКАЗА ##############################################################
# Обозначаем переменные
class State(StatesGroup):
    get_client_name = State()
    get_address = State()
    get_name_of_water = State()
    get_count_of_water = State()
    get_housedoor = State()
    get_floor = State()
    get_flat = State()
    get_recomendation = State()
    
    
    
    

# ------------------------------------------------------------------------------------------------------ #
# Обработчик текстовых сообщений пользователя, который реагирует на определенные ключевые слова и выполняет соответствующие действия.
@dp.message_handler(state=State.get_client_name)
async def process_client_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['client_name'] = message.text
        await message.answer(f"Укажите адрес доставки - {data['client_name']}")
    await State.get_address.set()
# ------------------------------------------------------------------------------------------------------ #
@dp.message_handler(state=State.get_address)
async def process_address(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['address'] = message.text
    await message.reply(f"Укажите название воды - {data['client_name']}\n\nУ нас имеется:\nАртезианская вода\nРодниковая вода\nФильтрованная вода")
    await State.get_name_of_water.set()
# ------------------------------------------------------------------------------------------------------ #
@dp.message_handler(state=State.get_name_of_water)
async def process_name_of_water(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name_of_water'] = message.text
    await message.reply(f"Укажите количество требуемых бутылей - {data['client_name']}")
    await State.get_count_of_water.set()
# ------------------------------------------------------------------------------------------------------ #
@dp.message_handler(state=State.get_count_of_water)
async def process_get_count_of_water(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['count_of_water'] = message.text
    await message.reply(f"Укажите подъезд - {data['client_name']}")
    await State.get_housedoor.set()
# ------------------------------------------------------------------------------------------------------ #
@dp.message_handler(state=State.get_housedoor)
async def process_get_housedoor(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['housedoor'] = message.text
    await message.reply(f"Укажи этаж - {data['client_name']}")
    await State.get_floor.set()
# ------------------------------------------------------------------------------------------------------ #
@dp.message_handler(state=State.get_floor)
async def process_get_floor(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['floor'] = message.text
    await message.reply(f"Укажи квартиру - {data['client_name']}")
    await State.get_flat.set()   

 # ------------------------------------------------------------------------------------------------------ #
@dp.message_handler(state=State.get_flat)
async def process_get_flat(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['flat'] = message.text
    await message.reply(f"Напишите если у вас имеются примечания к заказу - {data['client_name']} (если их нет напишите -)")
    await State.get_recomendation.set()
 # ------------------------------------------------------------------------------------------------------ #
@dp.message_handler(state=State.get_recomendation)
async def process_get_recomendation(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['recomendation'] = message.text
   



    client_name = data['client_name']
    address = data['address']
    name_of_water = data['name_of_water']
    count_of_water = data['count_of_water']
    housedoor = data['housedoor']
    floor = data['floor']
    flat = data['flat']
    recomendation = data['recomendation']
    

    conn = sqlite3.connect('water_delivery.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO base_orders (client_name, address, name_of_water, count_of_water, housedoor, floor, flat, recomendation) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
    (client_name, address, name_of_water, count_of_water, housedoor, floor, flat, recomendation))
    conn.commit()
    conn.close()
    

    conn = sqlite3.connect('water_delivery.db')
    result = conn.execute(f'SELECT price FROM base_clinets WHERE name == "{name_of_water}"')
    await message.reply(f"Заказ успешно принят!\nВыбран товар: {name_of_water}, количество - {count_of_water}.\n")
    await state.finish()
    conn.close()
    user_id = message.from_user.id
    kb = [
            [types.KeyboardButton(text="Виды воды которые имееются в наличии")],
            [types.KeyboardButton(text="Прочие товары")],
            [types.KeyboardButton(text="Я хочу сделать заказ")]
         ]

    if user_id == 876197281:
        kb.append([types.KeyboardButton(text="Доставка")])
    
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("Ожидайте. По всем вопросам звоните +7 914 555 55 55", reply_markup=keyboard)

# ------------------------------------------------------------------------------------------------------ #
####################################### КОНЕЦ ДОБАВЛЕНИЯ НОВОГО ЗАКАЗА #########################################################

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
