import pydirectinput
import time
import threading

def waitSpawnAnotherRock(): 
    pydirectinput.press('s')
    pydirectinput.press('s')
    pydirectinput.press('s')
    time.sleep(25)
    pydirectinput.press('w')
    pydirectinput.press('w')
    pydirectinput.press('w')

while True:

    total_time = 5
    end_time = time.time() + total_time

    while time.time() < end_time:
        pydirectinput.press('g')

    waitSpawnAnotherRock()
