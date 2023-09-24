import random
# importing random.
# it will be the key feature to the computer choosing it's hand.

def Computer_choice():
    choicelist = ["Rock", "Paper", "Scissors"]; # Lists of possible options
    choice = random.choice(choicelist); # the computer chooses between it's options
    return choice; # returns computer's choice.
    
def User_choice():
    choice = input('\nEnter "Rock" to play Rock.\n'
                   'Enter "Paper" to play Paper\n' # the way the user inputs their choice
                   'Enter "Scissors" to play Scissors\n'
                   '\tChoice : ');
    choice = choice.title();
    return choice; # returns user's choice.
    
    
def Determine_Winner(user, comp):
    winner = "None" # initialising and setting winner to 0
    print("\n");
    
    # this is how the game decides the winner.
    if user=="Rock" and comp=="Paper":
        winner = "Computer"; 
        print(f"User played {user} and Computer played {comp}\n" f"{winner} Wins.");
    elif user=="Paper" and comp=="Rock":
        winner = "User";
        print(f"User played {user} and Computer played {comp}\n"
              f"{winner} Wins.");
        
    elif user=="Paper" and comp=="Scissors":
        winner = "Computer";
        print(f"User played {user} and Computer played {comp}\n"
              f"{winner} Wins!");
    elif user=="Scissors" and comp=="Paper":
        winner = "User";
        print(f"User played {user} and Computer played {comp}\n"
              f"{winner} Wins.");
        
    elif user=="Scissors" and comp=="Rock":
        winner = "Computer";
        print(f"User played {user} and Computer played {comp}\n"
              f"{winner} Wins.");
    elif user=="Rock" and comp=="Scissors":
        winner = "User";
        print(f"User played {user} and Computer played {comp}\n"
              f"{winner} Wins.");
    elif user == comp:
        print(f"User played {user} and Computer played {comp}\n"
              f"It's a tie.");
    else :
        print(f"Sorry User, That's not an option!");
        

def RockPaperScissors():
    # Runs through the functions in the correct order.
    play = True;
    while play == True:
        player_choice = input(' \nWould you like to play "RockPaperScissors" with me, User ? (Yes/No)\n : ');
        player_choice = player_choice.title();
        if player_choice == "Yes":
            ComputerChoice = Computer_choice();
            UserChoice = User_choice();
            Determine_Winner(UserChoice, ComputerChoice);
            print(f"Thanks for playing.\n\n");
        else:
            print("Oh, come play some other time, Okay ?");
            break;
    
# Start game.
RockPaperScissors();

