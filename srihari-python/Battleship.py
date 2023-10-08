import tkinter as tk
import random

# Create the main window
root = tk.Tk()
root.title("Battleship Game")

# Increase the overall size of the UI
root.geometry("500x500")

# Create a 4x4 grid to represent the game board
board_size = 4
board = [['O' for _ in range(board_size)] for _ in range(board_size)]

# Function to update the game board display
def update_board():
    for i in range(board_size):
        for j in range(board_size):
            text = board[i][j]
            color = "lightgray" if text == 'O' else ("green" if text == 'X' else ("red" if text == 'C' else "blue"))
            label = tk.Button(root, text=text, width=7, height=3, font=("Arial", 14), bg=color, command=lambda row=i, col=j: user_guess(row, col))
            label.grid(row=i + 2, column=j, padx=5, pady=5)

# Function to handle user's guess
def user_guess(guess_row, guess_col):
    if game_over:
        return

    if user_ship_row == -1:
        set_user_ship(guess_row, guess_col)
    elif board[guess_row][guess_col] in ['X', 'C']:
        result_label.config(text="You already guessed there.")
    elif (guess_row == comp_ship_row) and (guess_col == comp_ship_col):
        result_label.config(text="Congratulations! You sank the computer's battleship!")
        board[guess_row][guess_col] = 'C'
        update_board()
        end_game(True)
    else:
        result_label.config(text="You missed the computer's battleship.")
        board[guess_row][guess_col] = 'X'
        update_board()
        computer_guess()

# Function to handle computer's guess
def computer_guess():
    if game_over:
        return

    comp_guess_row = random.randint(0, board_size - 1)
    comp_guess_col = random.randint(0, board_size - 1)

    if board[comp_guess_row][comp_guess_col] in ['X', 'C']:
        computer_guess()
    else:
        if (comp_guess_row == user_ship_row) and (comp_guess_col == user_ship_col):
            result_label.config(text="Oh no! The computer sank your battleship!")
            board[comp_guess_row][comp_guess_col] = 'U'
            update_board()
            end_game(False)
        else:
            result_label.config(text="The computer missed your battleship.")
            board[comp_guess_row][comp_guess_col] = 'C'
            update_board()

# Function to set the user's battleship position
def set_user_ship(row, col):
    global user_ship_row, user_ship_col
    user_ship_row = row
    user_ship_col = col
    user_ship_button.config(state="disabled")
    result_label.config(text="Computer's turn...")
    computer_guess()

# Function to end the game
def end_game(user_won):
    global game_over
    game_over = True
    if user_won:
        result_label.config(text="Game over! You won!")
    else:
        result_label.config(text="Game over! Computer won!")

# Initialize variables for user and computer ship positions
user_ship_row, user_ship_col = -1, -1
comp_ship_row = random.randint(0, board_size - 1)
comp_ship_col = random.randint(0, board_size - 1)

# Label for game instructions
instructions_label = tk.Label(root, text="Click on a position to set your battleship or take a shot:", font=("Arial", 14))
instructions_label.grid(row=0, column=0, columnspan=board_size, padx=5, pady=5)

# Create a 4x4 grid of buttons for user to set their battleship or take a shot
for i in range(board_size):
    for j in range(board_size):
        user_ship_button = tk.Button(root, text="", width=7, height=3, font=("Arial", 14), bg="blue", command=lambda row=i, col=j: user_guess(row, col))
        user_ship_button.grid(row=i + 2, column=j, padx=5, pady=5)

# Variable to track game state
game_over = False

# Label to display game result
result_label = tk.Label(root, text="", font=("Helvetica", 16))
result_label.grid(row=board_size + 2, column=0, columnspan=board_size, padx=5, pady=10)

# Start the GUI main loop
root.mainloop()

