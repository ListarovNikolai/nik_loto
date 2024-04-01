"""
Это модуль класса для карточек в игре лото
"""
import random

def init_card_numbers(count:int):
    numbers = set()
    while len(numbers) < count: 
        numbers.add(random.randint(1, 91))
    list_numbers = list(numbers)
    return list_numbers


class Card:
    def __init__(self) -> None:
        """
        Этот метод случайным образом формирует карточку а также они должны распологаться тоже случайно.
        Свойства карточки:
        self.lines - количество строк
        self.positions - количество позиций,
        self.number_in_line - количество чисел в одной строке,
        self.count - количество чисел в карточке,
        self.symbols - список списков всех символов
        """
        self.lines = 3
        self.positions = 9
        self.number_in_line = 5
        self.count = self.lines * self.number_in_line
        self.symbols = []
        card_numbers = set()
        


    if __name__ == '__main__':
        print(init_card_numbers(15))