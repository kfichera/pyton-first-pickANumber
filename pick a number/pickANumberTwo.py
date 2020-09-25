import random


print("hello, would you like easy, medium or hard?")
difficulity = int(input("1 for easy, 2 for med. 3 for hard: "))
truePick = False
difference = 0
numberOfGuesses = 0


while truePick == False:
    if difficulity == 1:
        difference = 10
        numberOfGuesses = 3
        truePick = True
    elif difficulity == 2:
        difference = 50
        numberOfGuesses = 5
        truePick = True
    elif difficulity == 3:
        difference = 100
        numberOfGuesses = 10
        truePick = True
    else:
        difficulity = int(input(
            "Please try again, please pick a valid 1, 2 or 3: "))
        if difficulity == 1 or difficulity == 2 or difficulity == 3:
            truePick = False
        else:
            truePick = False


randomNum = random.randint(0, 201)
lower_bound = randomNum - difference
upper_bound = randomNum + difference

while numberOfGuesses != 0:
    user_guess = int(input(
        f'pick a number between {lower_bound} and {upper_bound}: '))
    if user_guess == randomNum:
        print("You won! Thank you for playing")
        numberOfGuesses = 0
    else:
        if user_guess > randomNum:
            print("Too high! Please guess again")
        elif user_guess < randomNum:
            print("Too low! Please Guess again")
        numberOfGuesses -= 1
        print(f'you have {numberOfGuesses} guesses left')
        if numberOfGuesses == 0:
            print(f'Sorry you lost, the correct number was: {randomNum}')
