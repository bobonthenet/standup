import ctypes
import time
import sys

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

loops = 0
interval = [1800,1800] #defaults to 30 minutes.
i = 0

for timeFrame in sys.argv[1:]:
    interval[i] = intTryParse(timeFrame)
    i += 1

print("Press ctrl-C to stop the program early (runs about 8ish hours)")

while loops < 8:
    showPopup("You should stand up now.")
    time.sleep(interval[0])
    showPopup("Sit down now.")
    time.sleep(interval[1])

    loops += 1
