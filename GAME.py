import random

rules = ("""
   ROCK PAPER AND SCISSORS IS A SIMPLE GAME \n
   ROCK BEATS SCISSORS \n
   SCISSORS BEATS PAPER AND \n
   PAPER BEATS ROCK 

""")
how_to = ("""
choose from number 1 to 3 \n 1:ROCK \n 2:PAPER \n 3:SCISSORS
""")
play_game = False
play_state = ""

while play_state != "no":
    play_state = str(input("Would you like to play our game ? \n >>> "))
    play_state = play_state.lower()

    if play_state == "yes":
        play_game = True
        break
    else:
        print("wrong input\n")


def get_player_input():
    user_options = int(input("select your choice in numbers:\n >>> "))
    if user_options == 1:
        print("your choice is rock \n")
    elif user_options == 2:
        print("your choice is paper \n")
    elif user_options == 3:
        print("your choice is scissors\n")
    elif user_options >= 4:
        print("Number too large. Not in choices \n Try again")
        user_options = get_player_input()
    else:
        print("")
      

    return user_options


def get_computer_guess():
    if comp_guess == 1:
        print("computer choice is rock \n")
    elif comp_guess == 2:
        print("computer choice is paper \n")
    elif comp_guess == 3:
        print("computer choice is scissors \n")
    else:
        print(" ")
    return


def comparison():
    if (comp_guess == 1) and (user_options == 1):
        print("it is a tie \n")
    elif (comp_guess == 1) and (user_options == 3):
        print("computer wins \n")
    elif (comp_guess == 1) and (user_options == 2):
        print("You win \n")
    elif (comp_guess == 2) and (user_options == 1):
        print("computer wins \n")
    elif (comp_guess == 2) and (user_options == 2):
        print("it is a tie \n")
    elif (comp_guess == 2) and (user_options == 3):
        print("you win \n")
    elif (comp_guess == 3) and (user_options == 1):
        print("you wins \n")
    elif (comp_guess == 3) and (user_options == 2):
        print("computer wins \n")
    elif (comp_guess == 3) and (user_options == 3):
        print("it is a tie \n")


#  where our main code comes to run
while play_game == True:
    print(rules)
    print(how_to)

    user_options = get_player_input()
    comp_guess = random.randrange(1,3)
    while user_options > 4:
        continue
    get_computer_guess()
    comparison()
    prompt = input("would you like to play again? \n yes/no >>> ")
    prompt = prompt.lower()
    
    if prompt == "yes":
        user_options = get_player_input()
        print("\n")
    else:
        print('thanks for playing our game')
       
print("Thank you for playing our game. \nEnjoy your day")

















