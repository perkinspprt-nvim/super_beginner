import random

# computer generates random number and the user gueses it.
def guess(x):
    randnum = random.randint(1, x);
    guess = 0
    while guess != randnum:
        guess = int(input(f"\nGuess a number between 1 and {x}\n\t: "));
        if guess < randnum:
            print("Whoops you're guess is a bit low.\n")
        elif guess > randnum:
            print("Oooh, your'e guess is a bit high.\n")
        else:
            print("Congragulations, your'e guess is correct!\n\n")

 
#User generates number and computer tried to guess it.
def computer_guess(x):
    low = 1;
    high = x;
    feedback = " "
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high);
        else:
            guess = high;
        feedback = input(f"is {guess} too high(H), too low(L) or correct(C)?").lower();
        if feedback == "h":
            high = guess-1;
        elif feedback == "l":
            low = guess+1; 
        
    print(f"Yay, i guessed the number.");
            
        
computer_guess(10);   