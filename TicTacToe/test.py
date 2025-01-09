# Tic Tac Toe ( X and O ) - Ioana Marc

def show_table(table):
    for i, row in enumerate(table):
        print(" | ".join(row))
        if i < 2:
            print("-" * 9)

def initalize_game():
    table = [[" " for _ in range(3)] for _ in range(3)]
    score = {"X": 0, "O": 0}
    return table, score

def move(table, player):
    positions = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2)
    }

    while True:
        try:
            
            choice = int(input(f"{player}, choose a position (1-9): "))
            if choice not in positions:
                print("Not valid! Try again!")
                continue

            row, column = positions[choice]

            if table[row][column] == " ":
                table[row][column] = player
                return
            else:
                print("Not available! Try again!")
        except ValueError:
            print("Try a valid number between 1 and 9.")

def check_winner(table):
    for row in table:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]

    for col in range(3):
        if table[0][col] == table[1][col] == table[2][col] and table[0][col] != " ":
            return table[0][col]

    if table[0][0] == table[1][1] == table[2][2] and table[0][0] != " ":
        return table[0][0]
    if table[0][2] == table[1][1] == table[2][0] and table[0][2] != " ":
        return table[0][2]

    return None

def tic_tac_toe():
    table, score = initalize_game()
    player = "X"

    while True:
        show_table(table)
        print(f"Score: X - {score['X']}, O - {score['O']}")

        move(table, player)

        winner = check_winner(table)
        if winner:
            print(f"Player {winner} wins!")
            score[winner] += 1
            break

        if all(cell != " " for row in table for cell in row):
            print("It's a draw!")
            break

        player = "O" if player == "X" else "X"

    replay = input("Do you want to play again? (yes/no): ").lower()
    if replay == "yes":
        table = [[" " for _ in range(3)] for _ in range(3)]
        tic_tac_toe()
    else:
        print("Thanks for playing!")

if __name__ == "__main__":
    tic_tac_toe()
