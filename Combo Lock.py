import random

print("WELCOME TO COMBOTRON")
print("WE COME UP WITH A 4 DIGIT CODE FOR YOU TO CRACK. YOU GET 5 GUESSES PER NUMBER")
Guesses_dig_1=0
Guesses_dig_2=0
Guesses_dig_3=0
Guesses_dig_4=0
Digit_1=random.randint(0,9)
Digit_2=random.randint(0,9)
Digit_3=random.randint(0,9)
Digit_4=random.randint(0,9)
print("CODE MADE SOLVE NOW")
while Guesses_dig_1<5:
    guess_dig_1 = input("DIGIT ONE NOW:")
    guess_dig_1=int(guess_dig_1)
    Guesses_dig_1=Guesses_dig_1+1
    if guess_dig_1==Digit_1:
        print ("DIGIT ONE SOLVED")
        break
    else:
        if guess_dig_1 < Digit_1:
            print("A LITTLE HIGHER")
        else:
            print("LESS")
        print ("TRY AGAIN")
while Guesses_dig_2<5:
    guess_dig_2 = input("DIGIT TWO NOW:")
    guess_dig_2=int(guess_dig_2)
    Guesses_dig_2=Guesses_dig_2+1
    if guess_dig_2==Digit_2:
        print ("DIGIT TWO SOLVED")
        break
    else:
        if guess_dig_2 < Digit_2:
            print("A LITTLE HIGHER")
        else:
            print("LESS")
        print ("TRY AGAIN")
while Guesses_dig_3<5:
    guess_dig_3 = input("DIGIT THREE NOW:")
    guess_dig_3=int(guess_dig_3)
    Guesses_dig_3=Guesses_dig_3+1
    if guess_dig_3==Digit_3:
        print ("DIGIT THREE SOLVED")
        break
    else:
        if guess_dig_3 < Digit_3:
            print("A LITTLE HIGHER")
        else:
            print("LESS")
        print ("TRY AGAIN")
while Guesses_dig_4<5:
    guess_dig_4 = input("DIGIT FOUR NOW:")
    guess_dig_4=int(guess_dig_4)
    Guesses_dig_4=Guesses_dig_4+1
    if guess_dig_4==Digit_4:
        print ("DIGIT FOUR SOLVED.")
        break
    else:
        if guess_dig_4 < Digit_4:
            print("A LITTLE HIGHER")
        else:
            print("LESS")
        print ("TRY AGAIN")
if (Guesses_dig_1+Guesses_dig_2+Guesses_dig_3+Guesses_dig_4)>19:
    print("YOU LOSE")
else:
    print("GOOD JOB")
