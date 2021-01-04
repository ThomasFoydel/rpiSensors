import RPi.GPIO as GPIO
import time
import pygame

pygame.mixer.init()
pygame.mixer.music.load("../sounds/ding.mp3")

vib_pin = 21
buz_pin = 26
def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(vib_pin, GPIO.IN)
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(vib_pin,GPIO.IN)
    GPIO.setup(buz_pin,GPIO.OUT)
    
    def buzzer():
        while GPIO.input(vib_pin):
            GPIO.output(buz_pin,GPIO.LOW)
            pygame.mixer.music.play()
            time.sleep(0.1)
            GPIO.output(buz_pin,GPIO.HIGH)
            time.sleep(0.1)

    def callback(vib_pin):
        print("Movement Detected!")
        buzzer()
        
    GPIO.add_event_detect(vib_pin, GPIO.BOTH, bouncetime=300)
    GPIO.add_event_callback(vib_pin, callback)

    while True:
        time.sleep(3)

if __name__ == '__main__':
  try:
    main()
  except KeyboardInterrupt:
    pass
