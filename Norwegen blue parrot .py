# John Heitz
# 10/18/2017
# Norwegian Blue Guessing Game
# A guessing game
import random

#displays the title
print ("Welcome to the dead parrot guessing game")
print("""You walk into an old smelly pet shop.
You see a butiful parrot who has 4 identical twins
 MM    
/OO\\
\\   >
/  /
\\ / 
 mm

 MM
/OO\\
\\   >
/  /
\\ / 
 mm

 MM
/OO\\
\\   >
/  /
\\ / 
 mm

 MM
/OO\\
\\   >
/  /
\\ / 
 mm

 MM
/OO\\
\\   >
/  /
\\ / 
 mm
 
and a sign says if you guess the age of Davey you can keep all of them along with enough parrot food for life.
The age is between 1 and 20
You get 5 guesses""")
#sets guesses to 0 and makes the age
guesses=0
age=random.randint(1,20)
# check
while guesses<5:
    # Get a guess
    guess = input("Choose an age: ")
    guess=int(guess)
    if guess==age:
        print ("You win")
        break
    else:
        if guess < age:
            print("Too low")
        else:
            print("Too high")
        print ("You duckish ducky duck you will never get it right")
        guesses=guesses+1
print("Good job whats your face")
print("The answer was " , age)
