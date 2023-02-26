from .animal import Animal


class Dog(Animal):
    def __init__(self, name: str, age: int, breed: str):
        """
        :param name:
        :param age:
        :param breed:
        """
        super().__init__(f'Собака {name}', {'трава', 'мясо', 'корм'}, age)
        self.say_word = 'Гав'

    def treat(self) -> str:
        """
        Уделяем время животному, ухаживаем за ним
        :return: гладим кошку и настроение улучшается :)
        """
        print(f'Вы ухаживаете за {self.name} и вам становится приятно!')
        return 'Махает хвостиком!'