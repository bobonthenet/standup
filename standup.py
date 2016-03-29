import ctypes
import time
import sys

def showPopup(message):
    if(sys.version_info >= (3,0)):
        ctypes.windll.user32.MessageBoxW(0, message, "Do this", 0)
    else:
        ctypes.windll.user32.MessageBoxA(0, message, "Do this", 0)
    print(message)


loops = 0

print("Press ctrl-C to stop the program early (runs about 8ish hours)")

while loops < 8:
    showPopup("You should stand up now.")
    time.sleep(1800)  # Delay for 30 minutes (1800 seconds)
    showPopup("Sit down now.")
    time.sleep(1800)  # Delay for 30 minutes (1800 seconds)
    loops += 1
