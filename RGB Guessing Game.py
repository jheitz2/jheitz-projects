#John Heitz
#1/3/2018
#RGB Guessing Game
import RPi.GPIO as GPIO                                                                                   
import time
import random
play_again="YES"
LED_pin_red=21
LED_pin_green=22
LED_pin_blue=23
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_pin_red, GPIO.OUT)
GPIO.setup(LED_pin_green, GPIO.OUT) 
GPIO.setup(LED_pin_blue, GPIO.OUT)
def easter_egg():
    print("YOU BE PRO GAMR. PRTE TIM")
    while 1<2:
        high_or_low(50,5,60)
        high_or_low(50,0,100)
        high_or_low(100,0,0)
        high_or_low(0,0,100)
        high_or_low(0,100,0)
        high_or_low(50,100,0)
        high_or_low(0,100,100)
def high_or_low(red,green,blue):
    pwm_red=GPIO.PWM(LED_pin_red,100)
    pwm_green=GPIO.PWM(LED_pin_green,100)
    pwm_blue=GPIO.PWM(LED_pin_blue,100)
    pwm_red.start(red)
    pwm_green.start(green)
    pwm_blue.start(blue)
    time.sleep(5)
    pwm_blue.stop()
    pwm_red.stop()
    pwm_green.stop()
while play_again=="YES":
    guesses=0
    number=random.randint(1,100)
    print("THIS IS A GUESSING GAME WHERE YOU NEED TO GUESS A NUMBER IN FIVE GUESSES. YOU NEED TO GUESS NUMBERS !_!)). SORRY I MEANT 1-100. IT WILL BLINK CYAN IF TO LOW, IT WILL BLINK YELLOW IF TO HIGH, GREEN IF JUST RIGHT")
    while guesses< 5:
        guess=input("WHAT IS THE NUMBER YOU ARE GUESSING:")
        if guess=="Up Up Down Down Left Left Right B A":
            easter_egg()
        else:
            guess=int(guess)
            if guess==number:
                print("YOU WIN")
                break
            elif guess<number:
                high_or_low(0,100,100)
                guesses=guesses+1
            else:
                high_or_low(50,100,0)
            guesses=guesses+1
    play_again=input("Do you want to play again?").upper()
