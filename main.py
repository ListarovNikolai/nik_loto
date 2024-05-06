
from keg import Keg
from player import HumanPlayer, ComputerPlayer


if __name__ == '__main__':
    my_bug = Keg()
    print(f"Новый мешок: \n{my_bug}")
    count_players = int(input("Сколько будет игроков: "))
    players = []

    for i in range(count_players):
        type_of_player = int(input(f"Введите тип игрока № {i+1} (0-компьютер, 1-человек): "))

        if type_of_player==0:
            player = ComputerPlayer()
        elif type_of_player==1:
            player = HumanPlayer()
        else:
            print(f"Ошибка!!! Выберите правильный тип игрока!!!")
            i=+1
            break

        players.append(player)
        print(player)