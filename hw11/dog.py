from datetime import datetime

class Dog:
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
    def bark(self, count: int):
        for i in range(count):
            print(f'{self.name} гавкает')

    def walk(self, count: int):
        for i in range(count):
            print(f"{self.name} гуляет")
            self.is_walked = True