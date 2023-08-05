import tkinter as tk
import pandas as pd
import random

# ---------------------------- CONSTANTS ------------------------------- #
known_words = []
to_learn_words = []
current_card = {}
BACKGROUND_COLOR = "#B1DDC6"
# ---------------------------- WORDS ------------------------------- #
try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/dictionary.csv")
    to_learn_words = original_data.to_dict(orient="records")
else:
    to_learn_words = data.to_dict(orient="records")

# ---------------------------- FUNCTIONS ------------------------------- #
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn_words)
    canvas.itemconfig(card_title, text="Brazil", fill="black")
    canvas.itemconfig(card_word, text=current_card["BR"], fill="black")
    canvas.itemconfig(card_back, image=card_front_image)
    flip_timer = window.after(3000, func=flip_card)
def is_known():
    to_learn_words.remove(current_card)
    data = pd.DataFrame(to_learn_words)
    data.to_csv("data/words_to_learn_words.csv", index=False)
    next_card()
def flip_card():
    global current_card, flip_timer
    canvas.itemconfig(card_back, image=card_back_image)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["En"], fill="white")
def to_learn():
    global current_card, flip_timer
    canvas.itemconfig(card_back, image=card_back_image)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["En"], fill="white")
    is_known()
# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)
canvas = tk.Canvas(width=800, height=526)
card_front_image = tk.PhotoImage(file="images/card_front.png")
card_back_image = tk.PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_image)
card_front = canvas.create_image(400, 263, image=card_front_image)
card_back = canvas.create_image(400, 263, image=card_back_image)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)
# ---------------------------- Labels ------------------------------- #
card_title = canvas.create_text(400, 150, text="Flash", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="Card", font=("Arial", 60, "bold"))
#----------------------------- Buttons ---------------------------------#
button_x_pic = tk.PhotoImage(file="images/wrong.png")
button_y_pic = tk.PhotoImage(file="images/right.png")
button_x = tk.Button(image=button_x_pic, highlightthickness=0,command=next_card)
button_y = tk.Button(image=button_y_pic, highlightthickness=0, command=to_learn)
button_x.grid(column=0, row=1)
button_y.grid(column=1, row=1)

next_card()

window.mainloop()

