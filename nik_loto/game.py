from nik_loto.player import Player


def game_over(players: list[Player]):
    """
    Функция возвращает True если игра должна быть завершена
    """
    #Если в игре не осталось ни одного игрока то игра завершается:
    if len(players) == 0:
        return True

    for player in players:
        if player.is_looser:
            return True

    #Проверка каждого игрока:
    for player in players:
        if len(player.card.card_numbers) == 0:
            return True

    return False


def find_winners(players: list[Player]) -> list[Player]:
    winners = []
    for player in players:
        if len(player.card.card_numbers) == 0:
            winners.append(player)

    if len(winners) == 0:
        print("Игра завершена, победителей нет")
        return winners

    for winner in winners:
        print(f"{winner}{winner.name} - вы победили")

    return winners
