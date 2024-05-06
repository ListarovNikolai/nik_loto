import random


class Keg:
    def __init__(self) -> None:
        self.numbers = list(range(1, 91))

    def __str__(self) -> str:
        return ' '.join(map(str, self.numbers))
    
    def get_keg(self) -> int:
        result = random.sample(self.numbers, 1)[0]
        self.numbers.remove(result)
        return result


from abc import ABC, abstractmethod

class Player(ABC):
    @abstractmethod
    def play(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def pause(self):
        pass

    @abstractmethod
    def resume(self):
        pass

# Пример реализации класса, наследующего абстрактный класс Player
class MusicPlayer(Player):
    def play(self):
        print("Playing music...")

    def stop(self):
        print("Stopping music...")

    def pause(self):
        print("Pausing music...")

    def resume(self):
        print("Resuming music...")

class HumanPlayer(Player):
    def __init__(self, name):
        self.name = name
        self.is_playing = False

    def play(self):
        if not self.is_playing:
            print(f"{self.name} is playing.")
            self.is_playing = True
        else:
            print(f"{self.name} is already playing.")

    def stop(self):
        if self.is_playing:
            print(f"{self.name} stopped playing.")
            self.is_playing = False
        else:
            print(f"{self.name} is not playing.")

    def pause(self):
        if self.is_playing:
            print(f"{self.name} paused the game.")
        else:
            print(f"{self.name} cannot pause because not playing.")

    def resume(self):
        if self.is_playing:
            print(f"{self.name} resumed playing.")
        else:
            print(f"{self.name} cannot resume because not playing.")



class ComputerPlayer(Player):
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.is_playing = False

    def play(self):
        if not self.is_playing:
            print(f"Computer player with difficulty {self.difficulty} is playing.")
            self.is_playing = True
        else:
            print("Computer player is already playing.")

    def stop(self):
        if self.is_playing:
            print("Computer player stopped playing.")
            self.is_playing = False
        else:
            print("Computer player is not playing.")

    def pause(self):
        if self.is_playing:
            print("Computer player paused the game.")
        else:
            print("Computer player cannot pause because not playing.")

    def resume(self):
        if self.is_playing:
            print("Computer player resumed playing.")
        else:
            print("Computer player cannot resume because not playing.")





if __name__ == '__main__':
    my_keg = Keg()
    print(my_keg)

    print(f"Вы вытянули боченок: {my_keg.get_keg()}")
    print(f"Вы вытянули боченок: {my_keg.get_keg()}")
    print(f"Вы вытянули боченок: {my_keg.get_keg()}")
    print(f"Вы вытянули боченок: {my_keg.get_keg()}")
    print(f"Вы вытянули боченок: {my_keg.get_keg()}")
    print(my_keg)
    