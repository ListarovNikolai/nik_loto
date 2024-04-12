"""
Это модуль класса для карточек в игре лото
"""
import random

def init_card_numbers(count:int):
    numbers = set()
    while len(numbers) < count: 
        numbers.add(random.randint(1, 91))
    list_numbers = list(numbers)
    list_numbers.sort() 
    return list_numbers

   

def create_card(lines, positions, card_numbers, number_in_line):
    card_symbals = []
    for line in range(lines):
        line_symbals = ["   " for _ in range(positions)]
        set_position = set()   

        #Выберем случайные позиции для чисел в строке:          
        while len(set_position) < number_in_line:
            set_position.add(random.randint(1, number_in_line + 1))
        print(f"{set_position = }")

        #Заполним линию числами из карточки:
        for i in range(number_in_line):
            line_symbals[i] = str(card_numbers.pop(0))
            print(f"{card_numbers = }")

def print_card(self):
        for row in self.card_numbers:
            print(row)


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
        self.card_numbers = init_card_numbers(self.count)
    

    def __str__(self) -> str:
         return str(self.card_numbers)


if __name__ == '__main__':
    #print(init_card_numbers(15))
    my_card = Card()
    print(f"{my_card = }")
    create_card(my_card.lines, my_card.positions, my_card.card_numbers, my_card.number_in_line)