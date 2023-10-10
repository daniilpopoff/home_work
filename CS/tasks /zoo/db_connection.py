# в базе у меня есть 2 таблицы с животными и с шоу и связь между ними вроде
# как one to many от в одном шоу могут учавствовать много животных 
# мне интересно как args записывается в базе данных 
import sqlite3
conn = sqlite3.connect("zoo.db")

cursor = conn.cursor()
# в первый раз
# почему я не могу добавь сюда еще одно поле
# само шоу в котором будут учавстввать животные


cursor.execute('''
    CREATE TABLE IF NOT EXISTS birds(
    id INTEGER PRIMARY KEY,
    bird_name TEXT,
    bird_age INTEGER,
    alive INTEGER ,
    area TEXT,
    food TEXT,
    fly INTEGER ,
    show_id INTEGER,
    FOREIGN KEY (show_id) REFERENCES shows (id)
    )
''')



cursor.execute('''
    CREATE TABLE IF NOT EXISTS shows(
    id INTEGER PRIMARY KEY,
    show_name TEXT,
    description_show TEXT,
    price_show REAL,
    process_show TEXT
    )

''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS mammals(
    id INTEGER PRIMARY KEY,
    mammal_name TEXT,
    mammal_age INTEGER, 
    alive INTEGER,
    mammal_area TEXT,
    food TEXT,
    eating_milk INTEGER,
    show_id INTEGER,
    FOREIGN KEY (show_id) REFERENCES shows (id)
    )

''')
# и так походу алгоритм мне надо сначала создать животных потом когда я уже знаю что за животные и в каком они шоу по очереди
# я создаю шоу и придумываю для него действия
# впорос какой тогда смысл имеет свзязь в бд
# как я могу вывести животных не упомянув их в тексте и почему этот метод являеется (какбы нужной для связи вещью





# как мне сделать так чтобы при создании какого либо класса оно все автоматически
# добавлялось в базу данных причем я хочу чтобы все это было в отдельных файлах
#  мне надо создать функцию которая будет вызываться в другом файле и передовать данне в базу

def adding_bird(Bird_object):
    conn = sqlite3.connect("zoo.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO birds (bird_name, bird_age, alive, area, food, fly, show_id) VALUES (?, ?, ?, ?, ?, ?, ?)",
                   (Bird_object.name, Bird_object.age, Bird_object.alive, Bird_object.area, Bird_object.food, Bird_object.fly, Bird_object.show_id ))
    conn.commit()

def adding_mammal(Mammal_object):
    conn = sqlite3.connect("zoo.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO mammals (mammal_name, mammal_age, alive, mammal_area, food, show_id) VALUES (?, ?, ?, ?, ?, ?)",
                   (Mammal_object.name, Mammal_object.age, Mammal_object.alive, Mammal_object.area, Mammal_object.food, Mammal_object.show_id ))
    conn.commit()

def adding_show(Show_object):
    conn = sqlite3.connect("zoo.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO shows(id, show_name, description_show, price_show, process_show) VALUES (?, ?, ?, ?, ?)",
                   (Show_object.id, Show_object.show_name,Show_object.description_show, Show_object.price_show, Show_object.process_show))
    conn.commit()

conn.commit()
conn.close()
