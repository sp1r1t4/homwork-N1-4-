from .animal import Animal
# импортируем функции
# создаем класс с наследством и личными характеристиками
class Hen(Animal):
    def __init__(self, age: int,fed_check):
        super().__init__('Курица', {'пшено', 'зерно'}, age, fed_check)
        self.say_word = 'Кудах-кудах'

    def treat(self) -> str:
        print(f'Вы ухаживаете за {self.name} и курица несёт яйца!')
        return 'Куриные яйца'