#импортируем дату
from datetime import datetime
#создаем класс и его внутриности
class Animal:
    def __init__(self, name: str, allowed_meal: set, age: int,  last_vet_check: datetime = None):
        self.name = name
        self.allowed_meal = allowed_meal
        self.age = age
        self.say_word = '???'
        self.fed_check = True
        self.vet_check = True
        if isinstance(last_vet_check, datetime):
            month_difference = (datetime.now() - last_vet_check).days // 30
            if month_difference > 6:
                self.vet_check = False
            else:
                self.vet_check = True
#создаем общие фунцкии
    def eat(self, food: str):

        if food in self.allowed_meal:
            print(f'{self.name} кушает {food}')
            self.fed_check = True
        else:
            print(f'{self.name} не понимает что можно делать с {food}')
            self.fed_check = False
            self.say(2)

    def say(self, count: int):
        for i in range(count):
            print(f'{self.name} привлекает ваше внимание: {self.say_word}')

    def treat(self):
        print(f'Вы ухаживаете за {self.name}')