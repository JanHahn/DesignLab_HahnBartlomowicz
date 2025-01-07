from Locker import Locker
from FileHandler import FileHandler
import time
from multiprocessing import Queue
import RPi.GPIO as GPIO

#here is the file that initialize hardware and stores main backend loop that control application


#ustaw tutaj piny na raspberry odpoweidnie
REED_SWITCH1_INPUT = 1
LOCK1_OUTPUT = 4
REED_SWITCH2_INPUT = 3
LOCK2_OUTPUT = 2
FILE_PATH = "Locker_info.txt"
FILE_PATH2 = "codes.txt"

OPEN_TIMING = 15 #time after locker will open again after closing (in seconds)

def set_gpio():
    #setting pins numeration type to BCM
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(LOCK1_OUTPUT, GPIO.OUT)
    GPIO.output(LOCK1_OUTPUT, GPIO.LOW)
    print(f"Pin {LOCK1_OUTPUT} ustawiony na niski stan.")

    GPIO.setup(LOCK2_OUTPUT, GPIO.OUT)
    GPIO.output(LOCK2_OUTPUT, GPIO.LOW)
    print(f"Pin {LOCK1_OUTPUT} ustawiony na niski stan.")

    GPIO.setup(REED_SWITCH1_INPUT, GPIO.IN)
    print(f"Pin {REED_SWITCH1_INPUT} ustawiono jako wejscie")

#backend loop
def application(request_queue: Queue, queue2):
    set_gpio()
    file_handler = FileHandler(FILE_PATH)
    file_handler2 = FileHandler(FILE_PATH2)
    locker1 = Locker(1, LOCK1_OUTPUT, REED_SWITCH1_INPUT)
    locker2 = Locker(2, LOCK2_OUTPUT, REED_SWITCH2_INPUT)
    locker1_start_time = 0
    locker2_start_time = 0

    while True:
        #TODO add delay to opening while entering e-mail
        #section that opens lockers after OPEN_TIMING variable if no one enter e-mail
        # if locker1.status == 1 and locker1.is_opened() == 0:
        #     locker1_time = time.time() - locker1_start_time
        #     if locker1_time < OPEN_TIMING:
        #         locker1.open()
        #         locker1_start_time = 0
        #
        # if locker2.status == 1 and locker2.is_opened() == 0:
        #     locker2_time = time.time() - locker2_start_time
        #     if locker2_time < OPEN_TIMING:
        #         locker2.open()
        #         locker2_start_time = 0

        if not request_queue.empty():
            message = request_queue.get()
            #TODO add communication with frontend
            if message == "is_free":
                print("odebrano komende: is_free")
                queue2.put("01")
            if message == "new_code":
                print("odebrano new_code")
                info = request_queue.get() #[lockerid + email + new_code]
                file_handler2.change_status(info[0], info[-4:])
            if message == "open":
                print("otworz szafke")
                locker2.open()





# Przykład użycia funkcji
#try:
#    application()
#finally:
#    GPIO.cleanup()
