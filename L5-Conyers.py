import random

guesses = 0

difficulty = input("Would you like to do Easy, Medium, or Hard Mode: ")
if difficulty == 'Easy':
    num = random.randint(1, 10)
    print("Choose a number between 1 and 10")
if difficulty == 'Medium':
    num = random.randint(1, 20)
    print("Choose a number between 1 and 20")
if difficulty == 'Hard':
    num = random.randint(1, 50)
    print("Choose a number between 1 and 50")
while guesses < 5:
    guess = int(input("Guess a number: "))
    guesses = guesses + 1
    if guess < num:
        print("Too Low")
    if guess > num:
        print("Too High")
    if guess == num:
        print("You Win")
    if guess == num:
        break
    if guesses > 5:
        print("Too Many Tries, You Lose")
        break
    if guess == 0:
        break
