import RPi.GPIO as GPIO

#ustaw tutaj piny na raspberry odpoweidnie
REED_SWITCH_INPUT = 1
LOCK_OUTPUT = 2

def set_gpio():
    # Ustawienie trybu numeracji pinów na BCM
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(LOCK_OUTPUT, GPIO.OUT)
    GPIO.output(LOCK_OUTPUT, GPIO.LOW)
    print(f"Pin {LOCK_OUTPUT} ustawiony na niski stan.")

    GPIO.setup(REED_SWITCH_INPUT, GPIO.IN)
    print(f"Pin {REED_SWITCH_INPUT} ustawiono jako wejscie")


# Przykład użycia funkcji
#try:
#    set_gpio()
#finally:
#    GPIO.cleanup()
