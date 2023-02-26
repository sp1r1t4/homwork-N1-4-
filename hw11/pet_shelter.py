# импортируем класс пса и нужные нам библиотеки
from dog import Dog
import random
from datetime import datetime, timedelta
# создаем данный блок и помещаем в него всю нужную нам информацию о собаках и их еде
if __name__ == '__main__':
    dog_food = [
        "Мясо",
        "Роял Канин",
        "Клуб 4 Лапы",
        "Брит",
        "Вода",
        "Шашлык",
        "Шаурма"

    ]
    last_vet_check = datetime.now()
    dogs = [
        Dog(name='Макс', gender='кабель', age=1, breed='Питбуль', preferable_meal=set(random.choices(dog_food, k=5))),
        Dog(name='Роксалана', gender='сучка',age= 3,breed= 'Амстафф',preferable_meal=set(random.choices(dog_food, k=5))),
        Dog(name='Багги', gender='кабель',age= 8,breed= 'Дворняга',preferable_meal=set(random.choices(dog_food, k=5))),
        Dog(name="Роки", gender="кабель", age= 4, breed="Спаниэль",preferable_meal=set(random.choices(dog_food, k=5))),
        Dog(name="Дейзи",gender= "сучка", age= 2, breed= "Бигль", preferable_meal=set(random.choices(dog_food, k=5))),
        Dog(name="Бейли",gender= "сучка", age= 7, breed= "Пудель",preferable_meal=set(random.choices(dog_food, k=5))),
        Dog(name="Мегги",gender= "сучка",age= 3, breed= "Бульдог",preferable_meal=set(random.choices(dog_food, k=5)))
    ]
    last_vet_check -= timedelta(days=30)
# создаем базовые функции поведения
    for dog in dogs:
        print(dog)
        dog.sleep(4)
        for food in random.choices(dog_food, k=5):
            dog.eat(food)
            #создаем циклы проверок на различные недостатки
    for dog in dogs:
        if dog.fed_check:
            dog.walk(1)
        elif not dog.fed_check:
            print(f"Собака {dog.name} не кушала, поэтому не погуляла")
    for dog in dogs:
        print(f'Проверяем всё ли хорошо с {dog}')
        if not dog.fed_check:
            if dog.gender == 'сучка':
                print(f'Warning! {dog.name} голодна!')
            elif dog.gender == 'кабель':
                print(f'Warning! {dog.name} голоден!')
        if not dog.is_walked:
            print(f'Warning! {dog.name} может нагадить:), поэтому надо срочно выгулять!')
        if not dog.vet_check:
            if dog.gender == 'сучка':
                print(f'Warning! {dog.name} давно не проверялась у ветеринара!')
            elif dog.gender == 'кабель':
                print(f'Warning! {dog.name} давно не проверялся у ветеринара!')

















