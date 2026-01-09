class InvalidNumberError(Exception):
    pass
class InvalidNumberRangeError(Exception):
    pass
class PositionAlreadyTakenError(Exception):
    pass

position_mapper = {
    1 : (0, 0),
    2: (0, 1),
    3: (0, 2),
    4: (1, 0),
    5: (1, 1),
    6: (1, 2),
    7: (2, 0),
    8: (2, 1),
    9: (2, 2),
}
board = [[" ", " ", " "] for _ in range(3)]

def read_players_data() -> tuple[tuple[str, str], tuple[str, str]]:
    player_one_name = input("Player 1 name:")
    player_two_name = input("Player 2 name:")

    player_one_sign = input(f"{player_one_name} would you like to play with 'X' or 'O'?").upper()
    while player_one_sign not in ["X", "O"]:
        print("Invalid choice. Choose between X and O!")
        player_one_sign = input(f"{player_one_name} would you like to play with 'X' or 'O'?").upper()

    player_two_sign = "X" if player_one_sign == 'O' else "O"
    print(f'{player_one_name} starts first!')
    return (player_one_name, player_one_sign), (player_two_name, player_two_sign)

def print_board_numeration():
    print("This is the numeration of the board")
    print('| 1 | 2 | 3 |')
    print('| 4 | 5 | 6 |')
    print('| 7 | 8 | 9 |')


def check_position(position:str, board: list[list[str]]) -> tuple[int, int]:
    try:
        position = int(position)
    except ValueError:
        raise InvalidNumberError

    if position < 1 or position > 9:
        raise InvalidNumberRangeError

    row_index, col_index = position_mapper[position]
    if board[row_index][col_index] != " ":
        raise PositionAlreadyTakenError

    return row_index,col_index

def print_game_board(board: list[list[str]]):
    for row in board:
        print("| " + " | ".join(row) + " |")

def is_row_winner(board : list[list[str]], current_sign : str) -> bool:
    for row in board:
        if row.count(current_sign) == 3:
            return True
    return False

def is_col_winner(board : list[list[str]], current_sign : str) -> bool:
    for col in range(len(board)):
        col_count = 0
        for row in range(3):
            if board[row][col] == current_sign:
                col_count += 1
        if col_count == 3:
            return True

    return False

def is_diagonal_winner(board: list[list[str]], current_sign: str) -> bool:
    if all(board[i][i] == current_sign for i in range(3)):
        return True
    if all(board[i][2 - i] == current_sign for i in range(3)):
        return True
    return False

def is_winner(board: list[list[str]], current_sign: str) -> bool:
    return (
        is_row_winner(board, current_sign)
        or is_col_winner(board, current_sign)
        or is_diagonal_winner(board, current_sign)
    )

player1_data, player2_data = read_players_data()
turn = 1
print_board_numeration()

while True:
    current_player_name, current_player_sign = player1_data if turn % 2 != 0 else player2_data
    position = input(f"{current_player_name} select position between 1 and 9!")
    try:
        row_index,col_index = check_position(position,board)
    except (InvalidNumberError, InvalidNumberRangeError):
        print(f"Invalid number!")
    except PositionAlreadyTakenError:
        print(f'{current_player_name} please select a valid position')
    else:
        board[row_index][col_index] = current_player_sign
        print_game_board(board)
        if turn >= 5:
            if is_winner(board, current_player_sign):
                print(f"{current_player_name} won!")
                break
        if turn == 9:
            print("No one won!")
            break

        turn += 1

