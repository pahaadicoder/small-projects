print("welcome to the the number guessing game")
print("I am thinking of a number between 1 and 100")


import random
start=1
end = 100
number_x= random.randint(start,end)

difficulty=input("choose a difficulty. type easy or hard \n")

def easy():
    attempts=8
    while attempts >0:
        print(f"you have {attempts} attempts remaining to guess the correct number.")
        guess=int(input("make a guess? \n"))
        if guess == number_x:
            print("u guessed right ")
            print("u won!!")
        elif guess > number_x:
            print("too high")
            print("guess again")
            attempts-=1
        elif guess < number_x:
            print("too low")
            print("guess again")
            attempts-=1
        if attempts == 0:
            print("GAME OVER! you run out of the guesses. The number was:" , number_x)
              

        
def hard():
    attempts=4
    while attempts >0:
        print(f"you have {attempts} attempts remaining to guess the correct number.")
        guess=int(input("make a guess? \n"))
        if guess == number_x:
            print("u guessed right ")
            print("u won!!")
        elif guess > number_x:
            print("too high")
            print("guess again")
            attempts-=1
        elif guess < number_x:
            print("too low")
            print("guess again")
            attempts-=1
        if attempts == 0:
            print("GAME OVER! you run out of the guesses . The number was:" , number_x)
              

    
if difficulty == "easy":
    easy()
elif difficulty == "hard":
    hard()
    
    