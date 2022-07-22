import random as rd
import os
import time

def read():
    with open("./files/data.txt","r",encoding="utf-8") as f:
        words = [i.strip("\n") for i in f]
        word = rd.choice(words)
        return word.upper()

def intro():
    print()
    print("¡Welcome to the HANGMAN game!")
    print("Im your host Oscar")
    print("¿Are you ready to start?")
    print("¡Let's go!")
    print()


def game(arg):

    life = 5
    switch = False
    mistake = []

    print()
    word_list = list(arg)
    print("Guess the word:")
    for i in range(len(word_list)):
        word_list[i] = "_"
        print(word_list[i], end=" ")
    print()

    while True:
        # if switch:
        #     time.sleep(2)
        #     os.system("cls")
        
        if life <= 0:
            print("The game is over. ¡You lost!")
            print(f"The word you were looking for was: {arg}")
            break
        print()

        if word_list == list(arg):
            print("¡You Won! Congratulations :D:D")
            break
        print()

        try:
            guess = input("Type a letter: ").upper()
            if guess in ["1","2","3","4","5","6","7","8","9","0"]:
                raise ValueError
            print(guess)
        except ValueError:
            print()
            print("The characters must be letters from the alphabet")
        print()

        if guess in arg:
            for i, j in enumerate(arg):
                if guess == j:
                    word_list[i] = j
        else:
            if guess not in ["1","2","3","4","5","6","7","8","9","0"]:
                mistake.append(guess)
            life -= 1
            print()
            print("List of the letters you alredy tried:")
            print(sorted(mistake))
            print(f"You have {life} chances left")
        print()

        for i in range(len(word_list)):
            print(word_list[i], end=" ")
        print()    
        switch = True
    
        


def run():
    word = read()
    intro()
    game(word)

if __name__ == "__main__":
    run()