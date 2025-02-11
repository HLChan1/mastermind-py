class MastermindGame:
    def __init__(self, code_length=4, num_colors=6):
        self.code_length = code_length
        self.num_colors = num_colors
        self.secret_code = self.generate_code()
        self.guesses = []
        self.max_attempts = 10

    def generate_code(self):
        import random
        return [random.randint(1, self.num_colors) for _ in range(self.code_length)]

    def make_guess(self, guess):
        if len(guess) != self.code_length:
            raise ValueError("Guess must be of length {}".format(self.code_length))
        if len(self.guesses) >= self.max_attempts:
            raise Exception("Maximum attempts reached")
        self.guesses.append(guess)
        return self.check_guess(guess)

    def check_guess(self, guess):
        correct_position = sum(1 for i in range(self.code_length) if guess[i] == self.secret_code[i])
        correct_color = sum(min(guess.count(color), self.secret_code.count(color)) for color in set(guess)) - correct_position
        return correct_position, correct_color

    def is_game_over(self):
        return len(self.guesses) >= self.max_attempts or self.secret_code in self.guesses

    def get_secret_code(self):
        return self.secret_code

    def get_guesses(self):
        return self.guesses