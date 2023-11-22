import random
from tkinter import *
import pandas


BACKGROUND_COLOR = "#B1DDC6"
card = {}
word_to_learn = {}

WHITE_COLOR = "white"
BLACK_COLOR = "black"

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    print(original_data)
    word_to_learn = original_data.to_dict(orient="records")
else:
    word_to_learn = data.to_dict(orient="records")

# data = pd.read_csv("data/french_words.csv")
# # creates a Pandas DataFrame from a Python
# df = pd.DataFrame(data)
# # Convert the DataFrame to a list of dictionaries with "records" orientation
# records = df.to_dict(orient="records")


def generate_random_word():
    global card, flip_timer
    window.after_cancel(flip_timer)
    card = random.choice(word_to_learn)
    canvas.itemconfig(card_title, text="French", font=("Ariel", 40, "italic"),fill = BLACK_COLOR)
    canvas.itemconfig(card_text, text=card["French"], font=("Ariel", 60, "bold"),fill = BLACK_COLOR)
    canvas.itemconfig(card_background, image=card_white)
    # Schedule the function to run after 3000 milliseconds (1 second)
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", font=("Ariel", 40, "italic"),fill = WHITE_COLOR)
    canvas.itemconfig(card_text, text=card["English"], font=("Ariel", 60, "bold"),fill = WHITE_COLOR)
    canvas.itemconfig(card_background, image=card_blue)


def is_known():
    global data
    word_to_learn.remove(card)
    data = pandas.DataFrame(word_to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    generate_random_word()

# Create the User Interface (UI) with Tkinter

window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_white = PhotoImage(file="images/card_front.png")
card_blue = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_white)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_text = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

tick_image = PhotoImage(file="images/right.png")
tick_button = Button(image=tick_image, highlightthickness=0, command=is_known)
tick_button.grid(row=1, column=1)

x_image = PhotoImage(file="images/wrong.png")
x_button = Button(image=x_image, highlightthickness=0, command=generate_random_word)
x_button.grid(row=1, column=0)

generate_random_word()

window.mainloop()
