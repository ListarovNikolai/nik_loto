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
        self.is_winner = False  

        
    def __str__(self):
        return f"Player: {self.name}"


class HumanPlayer(Player):
    
    def __init__(self, is_computer=False):
        super().__init__(is_computer)


class ComputerPlayer(Player):
    
    def __init__(self, is_computer=True):
        self.is_playing = False
        super().__init__(is_computer)


if __name__ == '__main__':
    player1 = HumanPlayer()
    print(f"Имя игрока: {player1}, {player1.is_computer =}")
    print(f"Карточка: {player1.card}")
    player2 = ComputerPlayer()
    print(f"Компьюторный игрок: {player2}, {player2.is_computer =}")
    print(f"Карточка: {player2.card}")
