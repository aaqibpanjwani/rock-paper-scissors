import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

        if user_input not in options:
            continue

    random_number = random.randint(0, 2)
    # rock: 0 paper: 1 scissors: 2
    computer_pick = options [random_number]
    print("Computer picked", computer_pick + ".")


    if user_input == "rock" and computer_pick == "scissors":
        print("Hey you won! \U0001F929")
        user_wins += 1


    elif user_input == "scissors" and computer_pick == "paper":
        print ("Hey you won! \U0001F929")
        user_wins += 1
    
    elif user_input == "paper" and computer_pick == "rock":
        print ("Hey you won! \U0001F929")
        user_wins += 1
    
    else: print("Womp womp wommmmmp, maybe next time \U0001F972")
    computer_wins += 1
print("Hey you beat the computer", user_wins, "times! \U0001F4AA")
print("The computer won", computer_wins, "times \U0001F64A" )

print("Thank you for playing!")