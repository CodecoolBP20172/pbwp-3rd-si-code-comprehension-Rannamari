# the code below is a game where the comptures generates a number between 1 to 19 and the player has 5 guesses to take
import random # imports pseudo-random number generator named random module

guessesTaken = 0 # assigs 0 to global variable named guessesTaken 

print('Hello! What is your name?') # prints out a message to the console
myName = input() # assigning input value (str) to myName variable

number = random.randint(1, 20) # assigns random integer to variable named number within the range of 1 to 19
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.') # printing out a message

while guessesTaken < 6: # iterating through the indented code while guessesTaken variable is lower than 6
    print('Take a guess.') # printing out the message to the console,requesting user input
    guess = input() # assigns user input to variable named guess
    guess = int(guess) # converts str input to integer

    guessesTaken += 1 # increases the guessesTaken variable's value by one

    if guess < number: # decides whether the guess variable is lower than the number variable, if yes, executes the indented code below
        print('Your guess is too low.') # prints out the str in the parentheses to the console

    if guess > number: # decides whether the guess variable is higher than the number variable, if yes, executes the indented code below
        print('Your guess is too high.') # prints out the str in the parentheses to the console

    if guess == number: # decides whether the guess variable is equal to the number variable, if yes, executes the indented code below
        break # breaks out from the while loop

if guess == number: # decides whether the guess variable is equal to the number variable, if yes, executes the indented code below
    guessesTaken = str(guessesTaken) # converts the int type guessesTaken to a str type variable
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!') # prints out the str in the parentheses and the variable named guessesTaken to the console

if guess != number: # decides whether the guess variable is equal to the number variable, if not, executes the indented code below
    number = str(number) # converts the int type guessesTaken to a str type variable
    print('Nope. The number I was thinking of was ' + number) # prints out the str in the parentheses and the variable named number to the console
