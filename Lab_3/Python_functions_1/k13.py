import random

def GTN():
    print("Hello! What is your name?")
    a = input()
    print(f"Well, {a}, I am thinking of a number between 1 and 20.")
    b = random.randint(1, 20)
    n = 0
    while True:
        print("Take a guess.")
        c = int(input())
        if c == b:
            n += 1
            print(f"\nGood job, {a}! You guessed my number in {n} guesses!")
            return
        elif c > b:
            n += 1
            print("\nYour guess is too high.")
        else:
            n +=1
            print("\nYour guess is too low.")
        

GTN()
    