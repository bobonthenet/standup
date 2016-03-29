import ctypes
import time

def showPopup(message):
    ctypes.windll.user32.MessageBoxW(0, message, "Do this", 0)

loops = 0

print("Press ctrl-C to stop the program early (runs about 8ish hours)")

while loops < 8:
    showPopup("You should stand up now.")
    print("You should be standing.")
    time.sleep(5)  # Delay for 30 minutes (1800 seconds)
    ctypes.windll.user32.MessageBoxW(0, "Sit down now.", "Do this", 0)
    print("You should sit be sitting.")
    time.sleep(5)  # Delay for 30 minutes (1800 seconds)
    loops += 1
