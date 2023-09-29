movies = {
    "Mstiteli": {
        "John": 10,
        "Jack": 9
    },

    "Spider-Man": {},
}
# 1.Если фильм существует то не добавлять в
#  базу а вывести сообщение такой фильм уже добавлен
# 2.Если вы ставите рейтинг не существующему фильму 
# то вывести сообщение такого фильма нет
# 3.Оценка фильма должна быть от 1 до 10
# 4.Программа работает в бесконечном цикле с возможностью выхода


def show(movies):
        for title, ratings in movies.items():
            if not ratings:
                print(f"Фильм: {title}")
                continue
            
            ratings_sum = sum(ratings.values())
            rating_avg = ratings_sum / len(ratings.values())

            print(f"Фильм: {title}, Рейтинг: {rating_avg}\n ")

def film_rating_validation(movies, person_name, film_name):
    while True:
        try:
            film_rating = int(input("Введите оценку фильма от 1 до 10: "))
            if 1 <= film_rating <= 10:
                movies[film_name] = {person_name : film_rating}
                print("Оценка была успешно добавлена.")
                break
            else:
                print("Оценка должна быть в диапазоне от 1 до 10. Пожалуйста, введите корректную оценку.")
                return film_rating_validation(movies, person_name, film_name)
        except ValueError:
            print("Введите корректную оценку (целое число от 1 до 10).")

def add_movie(movies, person_name, film_name):
        if film_name in movies.keys():
            add_rating= int(input(f"фильм с названием {film_name}, уже существует\n вы можете только дать ему оценку\n дать оценку 1, выйти 0 "))
            if add_rating == 1:
                film_rating_validation(movies, person_name, film_name)
            elif add_rating != 1:
                return print("вы были возвращены в главное меню/n")
        elif film_name not in movies.keys():
            film_rating_validation(movies, person_name, film_name)
        return print("фильм и оцека были успешно добавлены")

def add_rate(movies, person_name, film_name):
        if film_name not in movies.keys():
            print(f"вы нем можете дать рейтинг не существующему фильму\n")
        elif film_name in movies.keys():
            film_rating_validation(movies, person_name, film_name)


        

while True:
    menu = int(input(f"добавить фильм: 1\n \
    добавить рейтинг фильма: 2\n \
    вывести фильмы: 3\n \
    выйти: 4\n \
    Введите число: "))

    if menu == 1:
        try:
            person_name = str(input("введите ваше имя :"))
            film_name = str(input("введите название фильма: "))
            
            add_movie(movies, person_name, film_name)
            
        except:
            print(f"введите число от 1 до 10 ")
           

        

    elif  menu == 2:
        try:
            person_name = str(input("введите ваше имя :"))
            film_name = str(input("введите название фильма: "))
            add_rate(movies, person_name, film_name)
        except:
            print("введите число" )

    elif menu == 3:
         show(movies)
    elif menu == 4:
        break
    






