from data import stages


class HangMan:

    def __init__(self, word):
        """Initializes the Hangman class with the word and the difficulty.
        Params: word=("The word to be guessed")
                difficulty=("The number of lives the user would have")"""
        self.word = word
        self.display = ["_" for _ in self.word]
        self.partial_guess = "".join(self.display)
        self.hang = 0
        self.result = ""

    def logic(self, key):
        """The Hangman Game logic, checks the word with the guess and penalizes in case it's a wrong guess"""
        guess = key
        if guess in self.partial_guess:
            return f"Already Checked '{guess}'"
        for letter_pos in range(len(self.word)):
            letter = self.word[letter_pos]
            if guess in self.word and letter == guess:
                self.display[letter_pos] = guess
                self.partial_guess = "".join(self.display)
            elif guess not in self.word:
                self.result = stages[self.hang]
                self.hang -= 1
                if self.hang < 0:
                    return f"The word was:\n{self.word}"
                elif self.hang < 1:
                    return "Final Chance"
                return "Uh-oh!"
        return
