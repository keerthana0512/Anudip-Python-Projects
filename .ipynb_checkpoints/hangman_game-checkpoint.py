import random

words = ["computer","python","java","programming","coding","data"]
word = random.choice(words)
            
def hangman():
    #initilize variable
    guess= " "
    attempts = 6

    #display word
    while attempts > 0:
        for char in word:
            if char in guess:
                print(char,end=" ")
            else:
                print("_",end=" ")

        #Get user input
        print("\nAttempts left:", attempts)
        guess_letter = input("Guess a letter. ")
        
        #Check if guess letter is right or worong
        if guess_letter in guess:
                print("You already entered that letter.")
            
        elif guess_letter in word:
                guess+=guess_letter
                if all(char in guess for char in word):
                    print("\nCongratulations,You won!!!\n")
                    break
                print("Good!!! \nThe letter is correct.\n")

        else:
                print("Incorrect guess.\n")
                guess+=guess_letter
                attempts-=1
            
        #check if attempts failed
        if attempts == 0:
            print("You ran out of attempts.")
            print("The word was : ",word)

    #Ask if player wants to play again
    play_again = input("\nDo you want to play again? (yes/no): \n")
    if play_again.lower() == "yes":
        hangman()
    else:
        print("Thanks for playing!!!\n")
        
hangman()
