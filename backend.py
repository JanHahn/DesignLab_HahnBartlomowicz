import RPi.GPIO as GPIO
import time

#here is the file that initialize hardware and stores main backend loop that control application


#ustaw tutaj piny na raspberry odpoweidnie
REED_SWITCH_INPUT = 1
LOCK_OUTPUT = 2

def set_gpio():
    #setting pins numeration type to BCM
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(LOCK_OUTPUT, GPIO.OUT)
    GPIO.output(LOCK_OUTPUT, GPIO.LOW)
    print(f"Pin {LOCK_OUTPUT} ustawiony na niski stan.")

    GPIO.setup(REED_SWITCH_INPUT, GPIO.IN)
    print(f"Pin {REED_SWITCH_INPUT} ustawiono jako wejscie")

#TODO funkcja sprawdzająca czy skrytka jest zamknięta (odczyt z pliku)
def is_closed(locker_number):
    pass

#backend loop
def application():
    while True:
        if is_closed(1) != True:
            continue
        else:
            start_time_1 = time.time()

        if is_closed(2) != True:
            continue
        else:
            start_time_2 = time.time()

# Przykład użycia funkcji
#try:
#    set_gpio()
#finally:
#    GPIO.cleanup()
