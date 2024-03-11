import RPi.GPIO as GPIO
from time import sleep
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(3, GPIO.OUT)
 
while True:
    GPIO.output(3, GPIO.LOW)
    sleep(0.5)

GPIO.cleanup()