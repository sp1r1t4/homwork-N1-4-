# импортируем все классы для старта
from animals import Cat
from animals import Hen
from animals import Cow
from animals import Dog
import random
from datetime import datetime, timedelta

# создаем блок с характеристиками и едой
if __name__ == '__main__':
    animals = [
        Cat('Дымок', 3, 'дворовая',True),
        Hen(1,True),
        Cow('Бурёнка', 4, True),
        Dog('Рок', 1, 'питбуль',True)
    ]
    last_vet_check = datetime.now()
    food_variants = [
        'трава',
        'сено',
        'пшено',
        'зерно',
        'рыба',
        'мясо',
        'молоко',
        "корм"
    ]
    last_vet_check -= timedelta(days=30)


# создаем два списка для просмотра что получили, а что потратили
    what_we_get = list()
    what_they_get = list()

#создаем циклы для проверок и некоторых функций
    for animal in animals:
        animal.say(3)
        for food in random.choices(food_variants, k=3):
            animal.eat(food)
            what_they_get.append(food)
        what_we_get.append(animal.treat())
    for animal in animals:
        print(animal)
    for animal in animals:
        print(f'Проверяем всё ли хорошо с {animal}')
    for animal in animals:
        if not animal.fed_check:
            print(f'Warning! {animal.name} голоден/голодна!')
        elif animal.fed_check:
            print(f"{animal.name} сыто")
    for animal in animals:
        if not animal.vet_check:
            print(f'Warning! {animal.name} давно не проверялась/проверялся у ветеринара!')
        elif animal.vet_check:
            print(f"С {animal.name} все отлично! ")


    print(f'What we lost: {what_they_get}')
    print(f'What we got: {what_we_get}')
#