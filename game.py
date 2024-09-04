def game_board(game_list):
    print(f" {game_list[0]} | {game_list[1]} | {game_list[2]}\n-----------\n "
          f"{game_list[3]} | {game_list[4]} | {game_list[5]}\n-----------\n "
          f"{game_list[6]} | {game_list[7]} | {game_list[8]} ")


def control(game_list):
    if game_list[0] == game_list[1] == game_list[2]:
        return game_list[0]
    elif game_list[3] == game_list[4] == game_list[5]:
        return game_list[3]
    elif game_list[6] == game_list[7] == game_list[8]:
        return game_list[6]
    elif game_list[0] == game_list[4] == game_list[8]:
        return game_list[0]
    elif game_list[2] == game_list[4] == game_list[6]:
        return game_list[2]
    elif game_list[0] == game_list[3] == game_list[6]:
        return game_list[0]
    elif game_list[1] == game_list[4] == game_list[7]:
        return game_list[1]
    elif game_list[2] == game_list[5] == game_list[8]:
        return game_list[2]
    else:
        pass


def player1_choose(game_list):
    player1 = int(input("Player1 please write a number between 1-9: ")) - 1
    if game_list[player1] == " ":
        game_list[player1] = "X"
    else:
        print("You have to choose the empty square")
        player1_choose(game_list)


def player2_choose(game_list):
    player2 = int(input("Player2 please write a number between 1-9: ")) - 1
    if game_list[player2] == " ":
        game_list[player2] = "Y"
    else:
        print("You have to choose the empty square")
        player2_choose(game_list)
