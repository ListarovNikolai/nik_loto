from abc import ABC, abstractmethod

from card import Card


class Player(ABC):

    def __init__(self, is_computer=False):
        if is_computer:
            self.name = "computer"
        else:
            self.name = input("Введите имя игрока: ")
        self.is_computer = is_computer
        self.card = Card()
        self.is_looser = False
        self.is_winner = False

    def __str__(self):
        return f"Player: {self.name}\n{self.card}"

    @abstractmethod 
    def move(self, number:int) -> None:
        pass
        

        
    

class HumanPlayer(Player):
    
    def __init__(self, is_computer=False):
        super().__init__(is_computer)

    
    def move(self, number:int) -> None:
        decision = input("Зачеркнуть число?(Y=да, N=нет)").lower()
        if decision == "y":
            #Попробуем вычеркнуть число
            if number in self.card.card_numbers:
                self.card.cross_out(number)
                print(f"Успешно вычеркнули число: {self.card}")
                if len(self.card.card_numbers) == 0:
                    self.is_winner = True
                    print(f"Игрок {self.name} вычеркнул все числа: ")

            else:
                #print(f"Числа нет в карточке: ")
                self.is_looser = True
                print(f"Игрок пройграл: {self}")
        else:
            #Пропускаем ход
            print(f"Не вычеркиваем: ")



class ComputerPlayer(Player):
    
    def __init__(self, is_computer=True):
        super().__init__(is_computer)
        #self.is_playing = False
        

    def move(self, number:int) -> None:
        if number in self.card.card_numbers:
            self.card.cross_out(number)
            if len(self.card.card_numbers) == 0:
                    self.is_winner = True
                    print(f"Игрок {self.name} вычеркнул все числа: ")
            
class Tg_player(Player):
    
    def __init__(self, tg_name, is_computer=False):
        self.name = tg_name
        self.is_computer = is_computer
        self.card = Card()
        self.is_looser = False
        self.is_winner = False

    
    def move(self, number:int) -> None:
        decision = input("Зачеркнуть число?(Y=да, N=нет)").lower()
        if decision == "y":
            #Попробуем вычеркнуть число
            if number in self.card.card_numbers:
                self.card.cross_out(number)
                print(f"Успешно вычеркнули число: {self.card}")
                if len(self.card.card_numbers) == 0:
                    self.is_winner = True
                    print(f"Игрок {self.name} вычеркнул все числа: ")

            else:
                #print(f"Числа нет в карточке: ")
                self.is_looser = True
                print(f"Игрок пройграл: {self}")
        else:
            #Пропускаем ход
            print(f"Не вычеркиваем: ")




if __name__ == '__main__':
    player1 = HumanPlayer()
    print(f"Имя игрока: {player1}, {player1.is_computer =}")
    print(f"Карточка: {player1.card}")
    player2 = ComputerPlayer()
    print(f"Компьюторный игрок: {player2}, {player2.is_computer =}")
    print(f"Карточка: {player2.card}")
