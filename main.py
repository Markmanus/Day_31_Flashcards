import tkinter as tk




BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
images = ["card_front.png", "card_back.png"]
canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = tk.PhotoImage(file="images/card_front.png")
card_back_image = tk.PhotoImage(file="images/card_back.png")
card_front = canvas.create_image(400, 263, image=card_front_image)
card_back = canvas.create_image(400, 263, image=card_back_image)
canvas.grid(column=0, row=0, columnspan=2)

# ---------------------------- Labels ------------------------------- #
language_label = tk.Label(text="Portugese", font=("Arial", 40, "italic"))
word_label = tk.Label(text="Word", font=("Arial", 60, "bold"))
language_label.place(x=400, y=150, anchor="center")
word_label.place(x=400, y=263, anchor="center")


#----------------------------- Buttons ---------------------------------#
button_x_pic = tk.PhotoImage(file="images/wrong.png")
button_y_pic = tk.PhotoImage(file="images/right.png")
button_x = tk.Button(image=button_x_pic, highlightthickness=0)
button_y = tk.Button(image=button_y_pic, highlightthickness=0)
button_x.grid(column=0, row=1)
button_y.grid(column=1, row=1)








window.mainloop()

