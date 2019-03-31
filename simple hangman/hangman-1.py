import time
hWord = ''
x = None

def hIntro():
    print("Welcome to Hang Man!")
    print("You will have 7 guesses to complete the word, otherwise you will end up a hanged man!")

def hangGame(hWord):
    hIntro()
    global x
    x = len(hWord)
    guesses = 0
    guessesRemaining = 7
    lettersGuessed = ""
    wordline = ['_']*x
    print(wordline)
    while guesses < 6:
        hangmanGraphic(guesses)
        guess = input("Please guess a letter: ")
        if len(guess)<2 and not guess.isnumeric():
            if guess in hWord and guess not in lettersGuessed:
                print("You guessed the letter correctly!")
                progressReport(guess, hWord, wordline)
                lettersGuessed += guess
                print("Guessed letters to date: " + lettersGuessed)
                if '_' not in wordline:
                    print("YOU WON! Congratulations! The noose falls away from your neck and you are free to walk!")
                    break


            elif guess in lettersGuessed:
                print("You already guessed that letter! Try again!")
                print("Guessed letters to date: " + lettersGuessed)

            elif guess not in hWord and guess not in lettersGuessed:
                guesses += 1
                print("You guessed the incorrect letter! The noose tightened!")
                lettersGuessed += guess
                print("Guessed letters to date: " + lettersGuessed)
                if guesses == 6:
                    hangmanGraphic(6)
                    break

        elif len(guess) >= 2:
            print("Please guess only a single letter character. No numbers or multiple characters")
        elif guess.isnumeric():
            print("Please only guess a single letter character. No numbers or multiple characters")

def hangmanGraphic(guesses):
    if guesses == 0:
        print("  ______")
        print(" |     |")
        print(" |     ")
        print(" |     ")
        print(" |     ")
        print(" |     ")
        print("------------")
    elif guesses == 1:
        print("  ______")
        print(" |     |")
        print(" |     O")
        print(" |     ")
        print(" |     ")
        print(" |     ")
        print("------------")
    elif guesses == 2:
        print("  ______")
        print(" |     |")
        print(" |     O")
        print(" |    /")
        print(" |     ")
        print(" |     ")
        print("------------")
    elif guesses == 3:
        print("  ______")
        print(" |     |")
        print(" |     O")
        print(" |    /|")
        print(" |     ")
        print(" |     ")
        print("------------")
    elif guesses == 4:
        print("  ______")
        print(" |     |")
        print(" |     O")
        print(" |    /|\\")
        print(" |     ")
        print(" |     ")
        print("------------")
    elif guesses == 5:
        print("  ______")
        print(" |     |")
        print(" |     O")
        print(" |    /|\\")
        print(" |    / ")
        print(" |     ")
        print("------------")
    elif guesses == 6:
        print("  ______")
        print(" |     |")
        print(" |     O")
        print(" |    /|\\")
        print(" |    / \\")
        print(" |     ")
        print("------------")
        print("\n\nYOU DIED!!\nYou ran out of guesses!")

def progressReport(guess, hWord, wordline):
    i = 0
    while i < len(hWord):
        if guess == hWord[i]:
            wordline[i] = guess
            i += 1
        else:
            i += 1
    print(wordline)
    return "".join(wordline)

hangGame('Hangman')
