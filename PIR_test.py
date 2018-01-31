# PIR Test
# John Heitz
# 1/24/2018
import RPi.GPIO as GPIO
import time
off="on"
def change_it(off):
    if off=="on":
        off="off"
    else:
        off="on"
    return off
PIR_pin=12
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_pin, GPIO.IN)
Button_pin=6
GPIO.setup(Button_pin, GPIO.IN)
LED_pin=21
GPIO.setup(LED_pin, GPIO.OUT)
off="on"
while 1<2:
    while off=="off":
        if GPIO.input (PIR_pin):
            print("HI FRIEND!")
            GPIO.output(LED_pin, GPIO.HIGH)
            time.sleep(0.5)
        else:
            GPIO.output(LED_pin, GPIO.LOW)
            time.sleep(0.5)
    if GPIO.input(Button_pin):
        off = change_it(off)

