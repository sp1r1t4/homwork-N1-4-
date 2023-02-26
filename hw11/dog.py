# импортируем дату
from datetime import datetime
# создаем класс собаки
class Dog:
    #создаем эти чтучки для логики поведения и подробного раскрытия класса
    def __init__(self, name:str, age:int, breed: str, gender: str,  preferable_meal: set, last_vet_check: datetime = None):
        self.name = name
        self.age = age
        self.gender = gender
        self.breed = breed
        self.preferable_meal = preferable_meal
        self.is_walked = False
        self.vet_check = True
        if isinstance(last_vet_check, datetime):
            month_difference = (datetime.now() - last_vet_check).days // 30
            if month_difference > 6:
                self.vet_check = False
            else:
                self.vet_check = True
#создаем функции для резюме пса, для сна и для еды и ее проверки
    def __str__(self) -> str:
        return f'{self.gender.capitalize()} породы {self.breed} по имени {self.name}, возраст {self.age} лет, обычно кушает {", ".join(self.preferable_meal)}'
    def sleep(self, hours:int):
        if self.age > 2:
            hours += 3

        elif self.age > 5:
            hours += 6
        print(f'{self.name} спит {hours} часов')
    def eat(self, food: str):
        if food in self.preferable_meal:
            print(f'{self.name} кушает {food} с удовольствием')
            self.fed_check = True
        else:
            print(f'{self.name} проходит мимо {food} и ни о чём не жалеет')
            self.bark(3)
            self.fed_check = False
  # создаем функции для лая и прогулки
    def bark(self, count: int):
        for i in range(count):
            print(f'{self.name} гавкает')

    def walk(self, count: int):
        for i in range(count):
            print(f"{self.name} гуляет")
            self.is_walked = True