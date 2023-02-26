from animals import Cat
from animals import Hen
from animals import Cow
from animals import Dog
import random
from datetime import datetime, timedelta


if __name__ == '__main__':
    animals = [
        Cat('Дымок', 3, 'дворовая'),
        Hen(1),
        Cow('Бурёнка', 4),
        Dog('Рок', 1, 'питбуль')
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



    what_we_get = list()
    what_they_get = list()


    for a in animals:
        a.say(3)
        for food in random.choices(food_variants, k=3):
            a.eat(food)

            what_they_get.append(food)
        what_we_get.append(a.treat())
    for animal in animals:
        print(animal)
    for animal in animals:
        print(f'Проверяем всё ли хорошо с {animal}')
        if not animal.fed_check:
            print(f'Warning! {animal.name} голоден/голодна!')
        elif animal.fed_check:
            print(f"{animal.name} сыто")
        #if not dog.is_walked:
            #print(f'Warning! {dog.name} может нагадить:), поэтому надо срочно выгулять!')
        if not animal.vet_check:
            print(f'Warning! {animal.name} давно не проверялась/проверялся у ветеринара!')
        elif animal.vet_check:
            print(f"С {animal.name} все отлично! ")


    print(f'What we lost: {what_they_get}')
    print(f'What we got: {what_we_get}')