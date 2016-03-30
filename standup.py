################################################################################
# Running this script with no arguments will use the defaults. 30 minutes of   #
# standing and 30 minutes of sitting with random exercises before you sit.     #
# you can also change the sit stand times by providing standing and sitting    #
# times in seconds. The 3rd argument should be either 1 or 0 and will determine#
# if a random exercise is chosen for you before the prompt to sit.             #
################################################################################

import ctypes
import time
import sys
from random import randint
import math

def showPopup(message):
    if(sys.version_info >= (3,0)):
        ctypes.windll.user32.MessageBoxW(0, message, "Do this", 0)
    else:
        ctypes.windll.user32.MessageBoxA(0, message, "Do this", 0)
    print(message)

def intTryParse(value):
    try:
        return int(value)
    except ValueError:
        return 1800

arguments = [1800,1800,1] #defaults to 30 minutes.
i = 0

randomExercise = [
    "Do 10 squats.",
    "Do a side bend for 10 seconds on each side.",
    "Do a forward bend and hold for 30 seconds.",
    "Do 10 knee lifts for each knee."
]

for timeFrame in sys.argv[1:]:
    arguments[i] = intTryParse(timeFrame)
    i += 1

loops = math.floor(28800 / (arguments[0] + arguments[1]))

print("Press ctrl-C to stop the program early (About 8ish hours for a normal run time.)")

while loops > 0:
    showPopup("You should stand up now.")
    time.sleep(arguments[0])
    if(arguments[2] == 1):
        showPopup(randomExercise[randint(0,len(randomExercise)-1)])
    showPopup("Sit down now.")
    time.sleep(arguments[1])

    loops -= 1
