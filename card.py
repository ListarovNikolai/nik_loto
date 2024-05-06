import random

def init_card_numbers(count:int):
    numbers = set()
    while len(numbers) < count: 
        numbers.add(random.randint(1, 91))
    list_numbers = list(numbers)
    #list_numbers.sort() 
    return list_numbers

def create_card(lines, positions, card_numbers, number_in_line):
    card_symbols = []
    for line in range(lines):
        line_symbols = ["   " for _ in range(positions)]
        set_position = set()   
        #print(f"{line}: {line_symbols}")
        
        # Выберем случайные позиции для чисел в строке:          
        while len(set_position) < number_in_line:
            set_position.add(random.randint(0, positions - 1))
            #print(f"{number_in_line = }, {set_position = }")
        #print(f"{set_position = }")        
        
        # Заполним линию числами из карточки:
        for i in set_position:
            line_symbols[i] = str(card_numbers.pop(0))

        card_symbols.append(line_symbols)
    return card_symbols

class Card:
    def __init__(self) -> None:
        """
        Этот метод случайным образом формирует карточку а также они должны располагаться тоже случайно.
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
        self.symbols = create_card(self.lines, self.positions, self.card_numbers, self.number_in_line)

    def __str__(self) -> str:
         # Преобразуем список списков символов в строку, чтобы вернуть её
         card_str = '\n'.join(' '.join(row) for row in self.symbols)
         separator = "\n" + "-" * 30 + "\n"
         return separator + card_str + separator
        
    

if __name__ == '__main__':
    my_card = Card()
    print(my_card)  # Теперь метод __str__ будет возвращать строковое представление всей карточки 
