import tkinter as tk
import time
import math

# -------- GLOBALS --------
board = [" " for _ in range(9)]
buttons = []
current_algo = "minimax"  # change to "alphabeta" to test

nodes_minimax = 0
nodes_alpha = 0

# -------- GAME LOGIC --------
def is_winner(player):
    win_states = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    return any(all(board[i] == player for i in combo) for combo in win_states)

def is_full():
    return " " not in board

# -------- MINIMAX --------
def minimax(is_max):
    global nodes_minimax
    nodes_minimax += 1

    if is_winner("X"):
        return -1
    if is_winner("O"):
        return 1
    if is_full():
        return 0

    if is_max:
        best = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                best = max(best, minimax(False))
                board[i] = " "
        return best
    else:
        best = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                best = min(best, minimax(True))
                board[i] = " "
        return best

# -------- ALPHA-BETA --------
def alphabeta(is_max, alpha, beta):
    global nodes_alpha
    nodes_alpha += 1

    if is_winner("X"):
        return -1
    if is_winner("O"):
        return 1
    if is_full():
        return 0

    if is_max:
        best = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                best = max(best, alphabeta(False, alpha, beta))
                board[i] = " "
                alpha = max(alpha, best)
                if beta <= alpha:
                    break
        return best
    else:
        best = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                best = min(best, alphabeta(True, alpha, beta))
                board[i] = " "
                beta = min(beta, best)
                if beta <= alpha:
                    break
        return best

# -------- BEST MOVE --------
def best_move():
    global nodes_minimax, nodes_alpha

    best_val = -math.inf
    move = -1

    nodes_minimax = 0
    nodes_alpha = 0

    start = time.time()

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"

            if current_algo == "minimax":
                val = minimax(False)
            else:
                val = alphabeta(False, -math.inf, math.inf)

            board[i] = " "

            if val > best_val:
                best_val = val
                move = i

    end = time.time()

    # Display stats
    stats_label.config(
        text=f"Algo: {current_algo.upper()} | Time: {round(end-start,5)}s | "
             f"Nodes: {nodes_minimax if current_algo=='minimax' else nodes_alpha}"
    )

    return move

# -------- UI --------
def on_click(i):
    if board[i] == " ":
        board[i] = "X"
        buttons[i].config(text="X")

        if is_winner("X"):
            status_label.config(text="You Win!")
            return

        if is_full():
            status_label.config(text="Draw!")
            return

        ai_move = best_move()
        board[ai_move] = "O"
        buttons[ai_move].config(text="O")

        if is_winner("O"):
            status_label.config(text="AI Wins!")
        elif is_full():
            status_label.config(text="Draw!")

def reset_game():
    global board
    board = [" " for _ in range(9)]
    for b in buttons:
        b.config(text="")
    status_label.config(text="Your Turn")
    stats_label.config(text="")

def switch_algo():
    global current_algo
    current_algo = "alphabeta" if current_algo == "minimax" else "minimax"
    algo_label.config(text=f"Current: {current_algo.upper()}")

# -------- TKINTER SETUP --------
root = tk.Tk()
root.title("Tic-Tac-Toe AI")

frame = tk.Frame(root)
frame.pack()

for i in range(9):
    btn = tk.Button(frame, text="", font=("Arial", 20), width=5, height=2,
                    command=lambda i=i: on_click(i))
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)

status_label = tk.Label(root, text="Your Turn", font=("Arial", 14))
status_label.pack()

stats_label = tk.Label(root, text="", font=("Arial", 10))
stats_label.pack()

algo_label = tk.Label(root, text="Current: MINIMAX", font=("Arial", 12))
algo_label.pack()

tk.Button(root, text="Switch Algorithm", command=switch_algo).pack()
tk.Button(root, text="Restart", command=reset_game).pack()

root.mainloop()