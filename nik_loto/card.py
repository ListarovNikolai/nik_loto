import random
from tokenize import Number

def init_card_numbers(count:int):
    numbers = set()
    while len(numbers) < count: 
        numbers.add(random.randint(1, 91))
    list_numbers = list(numbers)
    #list_numbers.sort() 
    #print(f"{list_numbers = }")
    return list_numbers

def create_card(lines, positions, card_numbers, number_in_line):
    card_symbols = []
    # Создаем копию списка card_numbers для использования внутри функции
    temp_card_numbers = card_numbers[:]
    for line in range(lines):
        line_symbols = ["   " for _ in range(positions)]
        set_position = set()
        while len(set_position) < number_in_line:
            set_position.add(random.randint(0, positions - 1))
        for i in set_position:
            line_symbols[i] = str(temp_card_numbers.pop(0))
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
        self.card_numbers - список всех чисел в карточке
        """
        self.lines = 3
        self.positions = 9
        self.number_in_line = 5
        self.count = self.lines * self.number_in_line
        #self.symbols = []
        self.card_numbers = init_card_numbers(self.count)
        #print(f"{self.card_numbers = }")
        self.symbols = create_card(self.lines, self.positions, self.card_numbers, self.number_in_line)

    def __str__(self) -> str:
         # Преобразуем список списков символов в строку, чтобы вернуть её
         card_str = '\n'.join(' '.join(row) for row in self.symbols)
         separator = "\n" + "-" * 30 + "\n"
         return separator + card_str + separator
    

    def cross_out(self, number: int) -> None:
        """
        Вычеркиваем из карточки число, заменяя его на соответствующее количество пробелов
        """
        try:
            # Проверяем наличие числа в списке card_numbers
            if number in self.card_numbers:
                # Вычеркиваем число из списка card_numbers
                self.card_numbers.remove(number)
                
                # Заменяем число на пробелы в card_symbols

                number_str = str(number)
                length = len(number_str)
                new_symbols = []
                for line in self.symbols:               # Для каждой строки в карточке
                # Сформируем новую строку:
                    new_line = []
                    for symbol in line:
                        new_line.append(symbol if symbol != number_str else '-'* length)
                    new_symbols.append(new_line)
                self.symbols = list(new_symbols)
                        

        
                # new_symbols = self.symbols.replace(number_str, ' '*length)
                # self.symbols = new_symbols
                # print(f"{new_symbols = }")


                
            else:
                # Если числа нет в списке, выбрасываем исключение
                raise ValueError("Числа в карточке нет")
        except ValueError as e:
            print(e)
    

if __name__ == '__main__':
    my_card = Card()
    print(f"{my_card.card_numbers = }")
    print(my_card)  # Теперь метод __str__ будет возвращать строковое представление всей карточки 
    remove_number = int(input("Какое число вычеркнуть? "))
    my_card.cross_out(remove_number)
    print(my_card)
