import tkinter as tk
import random

root = tk.Tk()
root.title("Tic-Tac-Toe")
players = ["X", "O"]
root.geometry("600x600")
player = random.choice(players)
buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

x_wins = 0
o_wins = 0
ties = 0

def next_move(row, column):
    global player

    if buttons[row][column]['text'] == "" and check_winner() is False:
        buttons[row][column]['text'] = player

        if check_winner() is False:
            player = players[1] if player == players[0] else players[0]
            label.config(text=(player + " move"))
        elif check_winner() is True:
            label.config(text=(player + " wins"))
        elif check_winner() == "Tie":
            label.config(text="Tie!")

def check_winner():
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            return True
    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            return True
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        return True
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        return True
    elif not empty_place():
        return "Tie"
    else:
        return False

def empty_place():
    places = 9
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                places -= 1
    if places == 0:
        return False
    else:
        return True

def new_game():
    global player
    player = random.choice(players)
    label.config(text=player + " move")
    for row in range(3):
        for column in range(3):
            buttons[row][column]['text'] = ""

def update_win_labels():
    x_win_label.config(text="X wins: " + str(x_wins))
    o_win_label.config(text="O wins: " + str(o_wins))
    tie_label.config(text="Ties: " + str(ties))

label = tk.Label(text=player + " move", font=('Helvetica', 30))
label.pack(side="top")

resetButton = tk.Button(text="Restart", command=new_game)
resetButton.pack(side="top")

frame = tk.Frame(root)
for row in range(3):
    for column in range(3):
        buttons[row][column] = tk.Button(frame, text="", font=('Helvetica', 24),
                                          command=lambda row=row, column=column: next_move(row, column))
        buttons[row][column].config(height=2, width=4, relief=tk.RIDGE, borderwidth=5, padx=10, pady=10)
        if player == "X":
            buttons[row][column].configure(fg="blue")
        else:
            buttons[row][column].configure(fg="red")
        buttons[row][column].grid(row=row, column=column)

frame.pack()


x_win_label = tk.Label(root, text="X wins: " + str(x_wins), font=('Helvetica', 12))
x_win_label.pack(side="bottom")

o_win_label = tk.Label(root, text="O wins: " + str(o_wins), font=('Helvetica', 12))
o_win_label.pack(side="bottom")

tie_label = tk.Label(root, text="Ties: " + str(ties), font=('Helvetica', 12))
tie_label.pack(side="bottom")

root.mainloop()
