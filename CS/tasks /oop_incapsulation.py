class Animal:
    def __init__(self, name, age, alive, area, food, vehicle ):

            self.name = name
            self.age = age
            self.alive = alive
            self.area = area
            self.food = food
            self.vehicle = vehicle


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
    def __init__(self, name, age, alive, area, food, vehicle, eating_milk):
        super().__init__(name, age, alive, area, food, vehicle)
        self.eating_milk = eating_milk

    def __str__(self):
        return f'в детстве я ел только молоко ведь я млекопитающее @{self.name}\n'

    def eating_milk_as_child(self):
        return print(f"то чем я питаюсь сейчас -это {self.food}")

    #      в дет саду для млекопитающих меня дразнять и просят доказать что
    #      я носноящее млекопитающее, и что я действительно прошел подготовку

    def go_to_kindergarten_for_mammals(self):
        if self.eating_milk == True:
            return (f"я настоящее млекопитающее даже когда был совсем маленьким ходил в детский сад \n"
                    f"для млекопитающих, там мама учила меня как надо жить на этой планете")

    def moving(self):
        return "тут я тоже двигаюсь и обычно бысреее чем просто animal ведь я mammal "


class Person(Mammals):
    def __init__(self, name, age,  alive, area, food, vehicle, eating_milk, car, hobby, work,):
        super().__init__(name, age, alive, area, food, vehicle, eating_milk)
        self.car = car
        self.hobby = hobby
        self.work = work

    def __str__(self):
        return (f"я обычный чел :"
                f'имя  - {self.name}\n'
                f'работа - {self.work}\n'
                f'хобби - {self.hobby}')


    def go_to_work(self):
        return f"я еду  на работу моя работа это {self.work}, моя машина это {self.car}"

    def do_hobbie(self):
        return f"я обожаю свое хобби это -{self.hobby}"
    def moving(self):
        return f"я могу передвигаться много на чем от моих ног до моей {self.car}"
    def __str__(self):
        return f"я обычный чел "


class Proger(Person):
    def __init__(self, name, age, alive, area, food, vehicle, eating_milk, car, hobby, work, laptop):
        super().__init__(name, age, alive, area, food, vehicle,  eating_milk, car, hobby, work)
        # self.__loan = loan
        self._laptop = laptop

    def get_laptop(self):
        return self._laptop

    def set_laptop(self, new_laptop):
        if new_laptop == "apple mackbook m2":
            self.__private_variable = new_laptop
    def moving(self):
        return "я же вообще предпочитаю не двгать ни чем короме пальцев и мышки"
    def __str__(self):
        return f"я прогер "
#

# в общем немного погуголив я узнал что оказывается не может быть класса абстракции так как она делается только
# для наследования ведь в мире не может существовать такого объекта который будет австакцией


# animal_abstr = Animal(name="живое существо", age= 0, alive=False , area="Земля",food="еда " )
ej = Mammals(name = "ежик", age=2, alive=True, area="russia", food="яблоки", vehicle="лапы 4WD", eating_milk=True)
mean_man = Person(name= "ivan",age= 30, alive= True, area="Russia", food="fast food", vehicle="ноги или машина ",  eating_milk=True,
                  car="lada", hobby="no hobby", work="стандартный_офис")
programmer  = Proger(name= " Евгений",age=20, alive= True, area="Russia", food="ПП", vehicle="машина и самолет  ", eating_milk=True,
                  car="lam", hobby="no hobby", work="", laptop="xaiomy")

list_of_objects= [ej, mean_man, programmer]

for object in list_of_objects:
    print(object, object.moving())