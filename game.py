from player import Player

def game_over(players: list[Player]):
    for player in players:
        if player.is_winner:
            return True
    return False
    