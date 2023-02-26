from .animal import Animal
#импортируем функции
#создаем класс с наследством и личными характеристиками
class Dog(Animal):
    def __init__(self, name: str, age: int, breed: str, fed_check):
        super().__init__(f'Собака {name}', {'трава', 'мясо', 'корм'}, age,fed_check,)
        self.say_word = 'Гав'

    def treat(self) -> str:
        print(f'Вы ухаживаете за {self.name} и вам становится приятно!')
        return 'Махает хвостиком!'