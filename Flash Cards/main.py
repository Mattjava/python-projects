from tkinter import messagebox
from tkinter import Canvas, Label,  Button, Tk, PhotoImage
import random
import pandas



BACKGROUND_COLOR = "#B1DDC6"

# Methods



def flip_card():
    global canvas

    canvas.itemconfig(word_label, text=french_word["English"], fill="white")
    canvas.itemconfig(french_label, text="English", fill="white")
    canvas.itemconfig(background, image=back)

def got_wrong():
    if french_word["French"] not in words_to_learn["French"]:
        words_to_learn["French"].append(french_word["French"])
        words_to_learn["English"].append(french_word["English"])
    move_to_next_card()
def got_right():
    if len(french_words_dict) > 1:
        french_words_dict.remove(french_word)
    move_to_next_card()
def move_to_next_card():
    global french_word
    global flip_timer

    screen.after_cancel("flip_timer")
    french_word = random.choice(french_words_dict)

    canvas.itemconfig(french_label, text="French", fill="black")
    canvas.itemconfig(word_label, text=french_word["French"], fill="black")
    canvas.itemconfig(background, image=front)
    flip_timer = screen.after(3000, func=flip_card)


# Data

try:
    french_words_data = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    french_words_data = pandas.read_csv("data/french_words.csv")
french_words_dict = french_words_data.to_dict(orient="records")
print(french_words_dict)
french_word = random.choice(french_words_dict)
words_to_learn = {"French": [], "English": []}
# french_words_list = french_words_data["French"].to_list()
#
# english_words_list = french_words_data["English"].to_list()


# Screen
screen = Tk()
screen.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
screen.title("Flashy")

# Images

yes_image = PhotoImage(file="images/right.png")
no_image = PhotoImage(file="images/wrong.png")
front = PhotoImage(file="images/card_front.png")
back = PhotoImage(file="images/card_back.png")

# Timer

flip_timer = screen.after(3000, func=flip_card)

# Canvas

canvas = Canvas( width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
background = canvas.create_image(400, 263, image=front)
canvas.grid(column=0, row=0, columnspan=2)
french_label = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"), fill="black")
word_label = canvas.create_text(400, 263, text=french_word["French"], font=("Ariel", 60, "bold"), fill="black")

# Buttons

yes_button = Button(image=yes_image, command=got_right)
yes_button.grid(column=1, row=1)

no_button = Button(image=no_image, command=got_wrong)
no_button.grid(column=0, row=1)


screen.mainloop()

words_to_learn_DataFrame = pandas.DataFrame(words_to_learn)
words_to_learn_DataFrame.to_csv("words_to_learn.csv", index=True)
