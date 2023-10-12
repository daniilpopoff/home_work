class Animal:
    def __init__(self, name, age, alive, area, food):

            self.name = name
            self.age = age
            self.alive = alive
            self.area = area
            self.food = food


    def __str__(self):
        return (f'Имя - {self.name}\n')

    def eat(self, food):
        if food == "еда":
            return "мм как вкусно"
        else:
            return 'я такое не ем'


    def moving(self):
        return f"обычно я передвигаюсь по вот этой площади"


class Mammals(Animal):
    def __init__(self, name, age, alive, area, food, eating_milk):
        super().__init__(name, age, alive, area, food)
        self.eating_milk = eating_milk

    def __str__(self):
        return f'в детстве я ел только молоко @{self.name}\n'

    def eating_milk_as_child(self):
        return print(f"то чем я питаюсь сейчас -это {self.food}")

    #      в дет саду для млекопитающих меня дразнять и просят доказать что
    #      я носноящее млекопитающее, и что я действительно прошел подготовку


    def go_to_kindergarten_for_mammals(self):
        if self.eating_milk == True:
            return (f"я настоящее млекопитающее даже когда был совсем маленьким ходил в детский сад \n"
                    f"для млекопитающих, там мама учила меня как надо жить на этой планете")



class Person(Mammals):
    def __init__(self, name, age,  alive, area, food, eating_milk, car, hobby, work,):
        super().__init__(name, age, alive, area, food, eating_milk)
        self.car = car
        self.hobby = hobby
        self.work = work

    def __str__(self):
        return (f'имя  - {self.name}\n'
                f'работа - {self.work}\n'
                f'хобби - {self.hobby}')


    def go_to_work(self):
        return f"я еду  на работу моя работа это {self.work}, моя машина это {self.car}"

    def do_hobbie(self):
        return f"я обожаю свое хобби это -{self.hobby}"

class Proger(Person):
    def __init__(self, name, age, alive, area, food, eating_milk, car, hobby, work, laptop):
        super().__init__(name, age, alive, area, food, eating_milk, car, hobby, work)
        # self.__loan = loan
        self._laptop = laptop

    def get_laptop(self):
        return self._laptop

    def set_laptop(self, new_laptop):
        if new_laptop == "apple mackbook m2":
            self.__private_variable = new_laptop
#
animal_abstr = Animal(name="живое существо", age= 0, alive=False , area="Земля",food="еда " )
ej = Mammals(name = "ежик", age=2, alive=True, area="russia", food="яблоки", eating_milk=True)
mean_man = Person(name= "ivan",age= 30, alive= True, area="Russia", food="fast food", eating_milk=True,
                  car="lada", hobby="no hobby", work="офис")
mean_man = Proger(name= " Евгений",age=20, alive= True, area="Russia", food="ПП", eating_milk=True,
                  car="lam", hobby="no hobby", work="офис", laptop="xaiomy")