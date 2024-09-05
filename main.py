from game import game_board, control, player1_choose, player2_choose

game_list = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
while True:
    game_board(game_list)
    if game_list.count(" ") != 0:
        player1_choose(game_list)
        if control(game_list) == "X":
            print("Player1 Won!")
            game_board(game_list)
            break
        elif game_list.count(" ") == 0:
            print("It's a draw.")
            game_board(game_list)
            break
        game_board(game_list)
        player2_choose(game_list)
        if control(game_list) == "Y":
            print("Player2 Won!")
            game_board(game_list)
            break


