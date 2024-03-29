import random

def start_game():
    attempts = 10
    number = random.randint(1,100)
    print("Welcome To Guess The Number Game")
    print("Let's play!!!")
    while True:
        try:
            if attempts == 0:
                print("The actual number is ",number)
                break
                
            guess_num = int(input("\nEnter a number between 1 and 100 : "))
            
            if (guess_num <1 or guess_num > 100):
                raise ValueError
                                  
            if (guess_num > number):
                print("It's higher than the actual number.")
                print(f"You left with {attempts-1} attempts.")    
            elif (guess_num < number):
                print("It's lesser than the actual number.")
                print(f"You left with {attempts-1} attempts.")
            elif (guess_num == number) :
                print("You won!!!")
                print("The number is ",number)
                break
            attempts -= 1        
            
        except ValueError as err:
            print("Enter valid number.")
start_game()