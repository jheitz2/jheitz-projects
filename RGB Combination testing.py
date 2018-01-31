#John Heitz
#1/3/2017
#RGB Combinations
#Green+blue=cyan
#Full Red+green=red
#Full Red+blue=Red
#50 Red+Green=Yellow
#50 Red+Blue=Magenta
#75 Red+Green=Orange
#50 Red+70 green+Full Blue=Pink
#40 Red+green=Neon yellow/green
#50 red+5 green+ 60 blue=Hot pink
import RPi.GPIO as GPIO                                                                                   
import time


LED_pin_red=21
LED_pin_green=22
LED_pin_blue=23
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_pin_red, GPIO.OUT)
GPIO.setup(LED_pin_green, GPIO.OUT) 
GPIO.setup(LED_pin_blue, GPIO.OUT)



pwm_red=GPIO.PWM(LED_pin_red,100)
pwm_green=GPIO.PWM(LED_pin_green,100)
pwm_blue=GPIO.PWM(LED_pin_blue,100)
pwm_red.start(40)
pwm_green.start(100)
pwm_blue.start(0)
time.sleep(5)
pwm_blue.stop()
GPIO.cleanup()
