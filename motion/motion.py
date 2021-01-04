import RPi.GPIO as GPIO
import time
import pygame

pygame.mixer.init()
pygame.mixer.music.load("../sounds/ding.mp3")

motion_pin = 18 #select the pin for motionsensor
buz_pin = 26 #select the pin for buzzer

def init():
         GPIO.setwarnings(False)
         GPIO.setmode(GPIO.BCM)
         GPIO.setup(motion_pin,GPIO.IN)
         GPIO.setup(buz_pin,GPIO.OUT)
         pass

def buzzer():
         while GPIO.input(motion_pin):
                  #GPIO.output(buz_pin,GPIO.LOW)
                  pygame.mixer.music.play()
                  time.sleep(0.1)
                  #GPIO.output(buz_pin,GPIO.HIGH)
                  time.sleep(1.9)

def detect():
#          for i in range(101):
    while True:
        if GPIO.input(motion_pin):
               print ("Motion detected!")
               buzzer()
        else:
               #GPIO.output(buz_pin,GPIO.HIGH)
               print ("Nothin!")
        time.sleep(2)

time.sleep(5)
init()
detect()

# GPIO.cleanup()