import RPi.GPIO as GPIO
import time

#class that represents single locker

class Locker:
    def __init__(self, locker_id, locker_pin, reed_switch):
        self.locker_id = locker_id
        self.status = 0    #0 - locker is closed at the moment, 1 - opened
        self.locker_pin = locker_pin
        self.reed_switch = reed_switch

    def open(self):
        GPIO.output(self.locker_pin, GPIO.HIGH)
        time.sleep(2)
        GPIO.output(self.locker_pin, GPIO.LOW)
        self.status = 1

    def is_opened(self):
        if GPIO.input(self.reed_switch): #returns True if HIGH
            return 1 #TODO set good value
        else:
            return 0