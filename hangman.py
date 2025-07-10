import tkinter as tk
import random

def start_game():
    global word, hint, guessed, tries
    word, hint = random.choice(list(word_list.items()))
    guessed = []
    tries = 6
    for b in buttons:
        b.config(state=tk.NORMAL)
    hint_btn.config(state=tk.NORMAL)
    entry_label.config(text="_ " * len(word))
    guess_label.config(text=f"Tries Left: {tries}")
    hint_label.config(text="")
    result_label.config(text="")
    play_btn.config(state=tk.DISABLED)

def update_display():
    display = " ".join([l if l in guessed else "_" for l in word])
    entry_label.config(text=display)
    guess_label.config(text=f"Tries Left: {tries}")
    if "_" not in display.replace(" ", ""):
        result_label.config(text="You Win!")
        disable_all()
    elif tries == 0:
        result_label.config(text=f"You Lose! Word was: {word}")
        disable_all()

def guess_letter(letter):
    global tries
    if letter in guessed or tries == 0:
        return
    guessed.append(letter)
    if letter not in word:
        tries -= 1
    update_display()

def disable_all():
    for b in buttons:
        b.config(state=tk.DISABLED)
    hint_btn.config(state=tk.DISABLED)
    play_btn.config(state=tk.NORMAL)

def show_hint():
    hint_label.config(text="Hint: " + hint)

root = tk.Tk()
root.title("Hangman Game")
root.geometry("420x500")

word_list = {
    "apple": "A fruit that keeps the doctor away",
    "robot": "A machine that can act like a human",
    "plane": "It flies in the sky",
    "light": "Opposite of dark",
    "bread": "Basic baked food made from flour"
}

entry_label = tk.Label(root, font=("Arial", 24))
entry_label.pack(pady=20)

guess_label = tk.Label(root, font=("Arial", 14))
guess_label.pack()

hint_btn = tk.Button(root, text="Show Hint", command=show_hint)
hint_btn.pack(pady=5)

hint_label = tk.Label(root, font=("Arial", 12), fg="gray")
hint_label.pack()

result_label = tk.Label(root, font=("Arial", 16))
result_label.pack(pady=10)

frame = tk.Frame(root)
frame.pack()

buttons = []
for i, letter in enumerate("abcdefghijklmnopqrstuvwxyz"):
    b = tk.Button(frame, text=letter.upper(), width=4, command=lambda l=letter: guess_letter(l))
    b.grid(row=i // 9, column=i % 9, padx=2, pady=2)
    buttons.append(b)

play_btn = tk.Button(root, text="Play Again", state=tk.DISABLED, command=start_game)
play_btn.pack(pady=10)

start_game()
root.mainloop()
