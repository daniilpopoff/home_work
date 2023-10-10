from db_connection import adding_show, adding_bird, adding_mammal
import sqlite3
class Animal:
    def __init__(self, name, age,  alive, area, food):


        if isinstance(name, str):
            self.name = name
        else:
            raise ValueError('Пиши тут тип str')

        if isinstance(age, int):
            self.age = age
        else:
            raise ValueError('Пиши тут только int')

        if isinstance(alive, bool):
            self.alive = alive
        else:
            raise ValueError('Пиши тут только float')

        if isinstance(area, str):
            self.area = area
        else:
            raise ValueError('Пиши только bool')
        
        if isinstance(food, str):
            self.food = food 
        else:
            raise ValueError('Пиши только bool')

    def __str__(self):
        return (f'Имя - {self.name}\n')
    
    def eat(self, food):
        if food == "еда":
            return "мм как вкусно"
        else:
            return 'я такое не ем'
        

class Mammals(Animal):
    def __init__(self, name, age,  alive, area, food, eating_milk, show_id):
        super().__init__(name, age,  alive, area, food)
        if isinstance(eating_milk, bool):
            self.eating_milk = eating_milk
        else:
            raise ValueError('Пиши только bool')

        if isinstance(show_id, int):
            self.show_id = show_id
        else:
            raise ValueError("Пиши только числа")
        adding_mammal(self)
    

        
    def __str__(self):
        return f'в детстве я ел только молоко @{self.name}\n'
    
    def eating(self, food):
        return print(f"то чем я питаюсь сейчас -это {food}")

# мне надо как то от животного сделать так чтобы оно принадлежало к какому нибудь шоу только к одному
class Bird(Animal):
    def __init__(self, name, age,  alive, area, food, fly, show_id):
        super().__init__(name, age,  alive, area, food)
        if isinstance(fly, bool):
            self.fly = fly 
        else:
            raise ValueError('Пиши только bool')
        if isinstance(show_id, int):
            self.show_id = show_id
        else:
            raise ValueError("Пиши только числа")
        adding_bird(self)

        
    def __str__(self):
        return super().__str__()
        
    def flying(self, fly):
       if fly:
           return print('вау я настоящая птица')
       else:
           return print('походу я пингвин')
    

muravied = Mammals(name = "Муравьед женя", age=22, alive=True, area="Africa", food="muravi", eating_milk=True, show_id= 1)
# print(vermilingua.food)
# vermilingua.eating(vermilingua.food)

pelikan = Bird(name="Кеша", age=20, alive=True, area="Atlantic Ocean",food="fish", fly=True, show_id=1 )

# pelikan.flying(pelikan.fly)

medved = Mammals(name="МИХА", age=3, alive=True, area= "Russia", food= "все",  eating_milk=True, show_id=2)

men = Mammals(name="Khabib", age=8, alive=True,area= "Russia", food="ПП", eating_milk=False, show_id=2)

class ZooShow:
    def __init__(self, id, show_name, description_show, price_show, process_show):
        self.id = id
        self.show_name = show_name
        self.description_show = description_show
        self.price_show = price_show
        self.process_show = process_show
        adding_show(self)


        # мне надо чтобы этот класс создавал 1 шоу коорое я захочу с разными живаотными 
        # значит что он должен принимать объекты в шоу описание и стоимость самого шоу

    # этот класс не знает какие животные учавствуют в шоу то есть прописать именно сдесь я не  могу
    # но в моей базе прописано что от животного идет связь к айди шоу
    # вопрос как вывести животных которые будут учавствовать в шоу

    
    def __str__(self) :
        return f""


    def choose_show (self):
        conn = sqlite3.connect('zoo.db')
        cursor = conn.cursor()

        # мне надо провписать так чтобы оно 2 раза брало данные из базы или 1 раз но выводило не все

        cursor.execute(f"SELECT * FROM shows")
        for row in cursor.fetchall():
            id, show_name, description_show, price_show, process_show = row
            print(f"ID: {id}")
            print(f"Название шоу: {show_name}")
            print(f"Описание: {description_show}")
            print(f"Цена билета: {price_show}")

        user_choice = int(input("выбирай что по душе или что по карману"))

        if user_choice == 1:
            cursor.execute("SELECT * FROM shows WHERE id = 1 ")
            show_data = cursor.fetchone()
            if show_data:
                process_show = show_data
                print(f"Процесс шоу: {process_show}")
        elif user_choice == 2:
            # Вывод информации о втором варианте
            cursor.execute("SELECT * FROM shows WHERE id = 2 ")
            show_data = cursor.fetchone()
            if show_data:
                process_show = show_data
                print(f"Процесс шоу: {process_show}")

        else:
            return "Выбрана неверная опция."
        conn.close()







#         животные знают что они учавсвуют в этом шоу но тот кто состаляет шоу не знает кто учасник
#         вопрос как узнать участников шоу из базы данных
# мне надо сделать джоин


spezoperation= ZooShow( id=1, show_name="спецоперация", description_show="пеликан и муравьед отравляются на спец операциию по добыче муравьиных рыб",
                       price_show=400, process_show='https://lovitut.ru/content/muravei')

borba=ZooShow(id= 2, show_name="Борьба", description_show="встретились как-то медведь и хабиб...",
              price_show=0, process_show="https://www.youtube.com/watch?v=1nfCYAKopdU")


ZooShow.choose_show(self=None)

        



