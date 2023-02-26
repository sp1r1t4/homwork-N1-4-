from .animal import Animal
#импортируем функции
#создаем класс с наследством и личными характеристиками
class Cat(Animal):
    def __init__(self, name: str, age: int, breed: str, fed_check):
        super().__init__(f'Кошка/кот {name}', {'рыба', 'мясо', 'молоко'}, age, fed_check)
        self.say_word = 'Мяу'

    def treat(self) -> str:
        print(f'Вы ухаживаете за {self.name} и вам становится приятно!')
        return 'Настроение улучшилось!'