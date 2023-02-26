from .animal import Animal
#импортируем функции
#создаем класс с наследством и личными характеристиками
class Cow(Animal):
    #
    def __init__(self, name: str, age: int, fed_check):
        # вызов метода класса-родителя
        super().__init__(f'Корова {name}', {'трава', 'сено'}, age, fed_check)
        # уточняем методы привлечения внимания для коровы
        self.say_word = 'мууу'
#
    def treat(self) -> str:
        print(f'Вы ухаживаете за {self.name} и корова даёт молоко!')
        return 'Ведро молока'



