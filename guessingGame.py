import random
randomNumber= random.randint(1,9)
chances=0
print("Guess the number between 1 to 9")
while chances<5:
    guess=int(input("Enter your guess"))
    if guess == randomNumber:
        print("Congratulations, You won !")
        break
    elif guess<randomNumber:
        print("Your guess was too Low, Guess a no. high")
    elif guess>randomNumber:
        print("your guess is too High, Guess a no. low")
    chances=chances+1
if not chances<5:
    print("You lost the game")            