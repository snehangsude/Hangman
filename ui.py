import random
from data import words
from tkinter import *
from game_model import HangMan
import time

THEME = '#444444'


class HangmanInterface:

    def __init__(self):
        """Initializes the interface window along with setting a random word to guess.
         Call this method to create the game"""
        self.pressed = False
        self.word = HangMan(random.choice(words))
        self.window = Tk()
        self.window.title('Hangman')
        self.window.bind("<KeyPress>", self.key_press)
        self.window.config(bg=THEME, padx=50, pady=50)
        self.canvas = Canvas(width=100, height=200, bg='grey90')
        self.text = self.canvas.create_text(65, 100, text="", font=("Lucida Sans Typewriter", 17,), width=270, )
        self.canvas.grid(row=2, column=2, rowspan=2, padx=15, pady=15)

        # --------------- Labels----------------#
        self.welcome = Label(text="The Hangman Game",
                             font=("Lucida Fax", 18, "bold underline"),
                             bg=THEME, fg='#B2B1B9', )
        self.welcome.grid(row=1, column=1, columnspan=3, pady=15)

        self.blanks = Label(text=f'{self.word.partial_guess}',
                            font=("Tahoma", 15, "bold"),
                            bg=THEME, fg='#F48B29', )
        self.blanks.grid(row=4, column=1, columnspan=3, pady=15)

        self.info = Label(text="", font=("Helvetica Neue", 12, "italic"),
                          bg=THEME, fg='#F48B29', )
        self.info.grid(row=6, column=1, columnspan=3, pady=15)

        # ---------- Buttons ------------- #
        # Easy
        self.easy = Button(bd=-2, highlightthickness=0, text='Easy', bg=THEME, padx=2, pady=2,
                           font=("Tw Cen MT", 17, "bold"), command=self.easy, fg='#50CB93')
        self.easy.grid(row=5, column=1)
        # Normal
        self.normal = Button(bd=-2, highlightthickness=0, text='Normal', bg=THEME, padx=2, pady=2,
                             font=("Tw Cen MT", 17, "bold"), command=self.normal, fg='#E0C097')
        self.normal.grid(row=5, column=2)
        # Hard
        self.hard = Button(bd=-2, highlightthickness=0, text='Hard', bg=THEME, padx=2, pady=2,
                           font=("Tw Cen MT", 17, "bold"), command=self.hard, fg='#D54C4C')
        self.hard.grid(row=5, column=3)

        self.window.mainloop()

    def easy(self):
        """Button function for the 'Easy' key"""
        self.word.hang = 9
        self.welcome.config(text=f"Guess the word\nLength: {len(self.word.word)}")
        self.blanks.config(text=self.word.partial_guess)
        self.easy.config(state="disabled")
        self.normal.config(state="disabled")
        self.hard.config(state="disabled")
        self.pressed = True

    def normal(self):
        """Button function for the 'Normal' key"""
        self.word.hang = 6
        self.welcome.config(text=f"Guess the word\nLength: {len(self.word.word)}")
        self.blanks.config(text=self.word.partial_guess)
        self.normal.config(state="disabled")
        self.easy.config(state="disabled")
        self.hard.config(state="disabled")
        self.pressed = True

    def hard(self):
        """Button function for the 'Hard' key"""
        self.word.hang = 4
        self.welcome.config(text=f"Guess the word\nLength: {len(self.word.word)}")
        self.blanks.config(text=self.word.partial_guess)
        self.hard.config(state="disabled")
        self.easy.config(state="disabled")
        self.normal.config(state="disabled")
        self.pressed = True

    def key_press(self, event):
        """Captures the key pressed on the keyboard as an 'event' parameter and passes that as the guessed
        letter in the game model"""
        if self.pressed:
            key = event.char
            result = self.word.logic(key)
            self.canvas.itemconfig(self.text, text=self.word.result)
            self.welcome.config(text=result)
            self.blanks.config(text=self.word.partial_guess)
            if self.word.word == self.word.partial_guess:
                self.welcome.config(text='Good Job!\nYou guessed it!')
                self.info.config(text='Press any key to restart')
                self.window.bind("<KeyPress>", self.restart)
            elif self.word.hang < 0:
                self.welcome.config(text=f'The word was:\n{self.word.word}')
                self.info.config(text='Press any key to restart')
                self.window.bind("<KeyPress>", self.restart)
        else:
            self.welcome.config(text='Please choose from:\nEasy/Normal/Hard')

    def restart(self, event):
        """Captures any key input and initializes the __init__ class after a delay of 1 second"""
        time.sleep(1)
        self.window.destroy()
        HangmanInterface()
