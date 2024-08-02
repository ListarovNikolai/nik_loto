
from unittest import result
from keg import Keg
from game import find_winners, game_over
from player import HumanPlayer, ComputerPlayer


if __name__ == '__main__':
    my_keg = Keg()
    print(f"Новый мешок: \n{my_keg}")
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


    while not game_over(players):
        next_number = my_keg.get_keg()
        for player in players:
            print(f"Ход делает: {player}")
            player.move(next_number)
            if player.is_looser:
                #print(f" ====+++++**\n Начнем удаление игрока: {players}")
                players.remove(player)
                #print(f"Успешно удалили игрока: {player}\n Остались: {players} \n ====+++++**")

    find_winners(players)

print("Игра окончена")