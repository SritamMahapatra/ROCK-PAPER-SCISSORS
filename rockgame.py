import random

class choice:
    def __init__(self):
        self.choices = ['rock', 'paper', 'scissors']
        self.user_score = 0
        self.computer_score = 0

    def get_user_choice(self):
        while True:
            user_choice = input("Choose rock, paper, or scissors: ").lower()
            if user_choice in self.choices:
                return user_choice
            else:
                print(" Please choose again.")

    def get_computer_choice(self):
        return random.choice(self.choices)

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            self.user_score += 1
            return "You win!"
        else:
            self.computer_score += 1
            return "Computer wins!"

    def result(self, user_choice, computer_choice, result):
        print(f"You chose {user_choice}.")
        print(f"The computer chose {computer_choice}.")
        print(result)
        print(f"Score: You - {self.user_score}, Computer - {self.computer_score}")

    def play_again(self):
        return input("Do you want to play again? (y/n): ").lower() == 'y'

def main():
    game = choice()

    while True:
        user_choice = game.get_user_choice()
        computer_choice = game.get_computer_choice()
        result = game.determine_winner(user_choice, computer_choice)
        game.result(user_choice, computer_choice, result)

        if not game.play_again():
            print("Thanks playing!")
            break

if __name__ == "__main__":
    main()
