class GuessingGame():
    def __init__(self, answer_number):
        self.answer_number = answer_number
    def guess(self, user_guess):
        self.user_guess = user_guess
        if user_guess > self.answer_number:   
            return 'high'
        elif user_guess < self.answer_number:
            return 'low'
        else: 
            return 'correct'
    def solved(self):
        if game.user_guess == game.answer_number:
            return True
        else:
            return False
game = GuessingGame(10) #10 is the answer 
print(game.guess(5)) #5 is the user's guess -> returns low
print(game.solved()) # whether the user was correct or incorrect -> returns false
