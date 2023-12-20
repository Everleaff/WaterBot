import sqlite3

conn = sqlite3.connect('water_delivery.db')
# base_clinets metal_gear_model 
# base_items metal_gear_tth
# base_orders metal_gear_pilot
conn.execute('''
CREATE TABLE IF NOT EXISTS base_clinets 
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    type TEXT,
    description TEXT,
    price TEXT
)
''')

conn.execute('''
CREATE TABLE IF NOT EXISTS base_items
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name_etc TEXT,
    description_etc TEXT,
    price_etc TEXT
    
)
''')

conn.execute('''
CREATE TABLE IF NOT EXISTS base_orders
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_name TEXT,
    address TEXT,
    name_of_water TEXT,
    count_of_water TEXT,
    housedoor TEXT,
    floor TEXT,
    flat TEXT,
    recomendation TEXT
    
)
''')

cur = conn.cursor()

conn.execute('INSERT INTO base_clinets (name, type, description, price) VALUES (?, ?, ?, ?)',
             ('Артезианская вода', 'Питьевая','Известна своим содержанием минералов, которые придают ей уникальный вкус и могут иметь благотворное воздействие на здоровье. Она может быть добыта из подземных источников.', '150₽ за 1 бутыль(1 бутыль = 19л.)',))

conn.execute('INSERT INTO base_clinets (name, type, description, price) VALUES (?, ?, ?, ?)',
             ('Родниковая вода', 'Питьевая','Вода, вытекающая из недр земли, часто в гористых районах. Родниковая вода часто признается своей природной чистотой и может быть питьевой без дополнительной обработки.', '180₽ за 1 бутыль(1 бутыль = 19л.)',))

conn.execute('INSERT INTO base_clinets (name, type, description, price) VALUES (?, ?, ?, ?)',
             ('Фильтрованная вода', 'Питьевая','Вода, прошедшая через систему фильтрации для удаления примесей, бактерий и хлора.', '100₽ за 1 бутыль(1 бутыль = 19л.)',))

conn.execute('INSERT INTO base_items (name_etc, description_etc, price_etc) VALUES (?, ?, ?)',
             ('Механическая помпа', 'Механическая помпа предназначена для бутылей с чистой питьевой водой в кухонных помещениях квартир и жилых домов, в административных и офисных учреждениях. Приспособление подойдет для обычных пластиковых емкостей, а также для контейнеров с резьбовым соединением при дополнительном использовании специального переходника.', '500₽'))

conn.execute('INSERT INTO base_items (name_etc, description_etc, price_etc) VALUES (?, ?, ?)',
             ('Электрическая помпа', 'Автоматическая электрическая помпа для воды на бутылку 19 литров со встроенным водным насосом и аккумулятором, которая устанавливается на бутыль с водой 10 или 15 5 19л литров. Управление с помощью мини кнопки. Электро устройство 12в дозатор выглядит лаконично и презентабельно.', '1 000₽'))

conn.execute('INSERT INTO base_items (name_etc, description_etc, price_etc) VALUES (?, ?, ?)',
             ('Ecocenter A-F519C', 'Полнофункциональный (с нагревом и охлаждением) кулер (диспенсер) для розлива питьевой воды Ecocenter A-F519C, серебристого цвета ! Производительность и температура охлаждения составляет 2 л/ч, с охлаждением до 10 С, что ВДВОЕ больше мощности кулеров с электронным охлаждением (0,7 л/ч) !', '13 000₽'))



conn.commit()

conn.close()
