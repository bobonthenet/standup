import ctypes
import time

loops = 0

while loops < 8:
    ctypes.windll.user32.MessageBoxW(0, "You should stand up now.", "Do this", 0)
    time.sleep(1800)  # Delay for 30 minutes (1800 seconds)
    ctypes.windll.user32.MessageBoxW(0, "Sit down now.", "Do this", 0)
    time.sleep(1800)  # Delay for 30 minutes (1800 seconds)
    loops += 1
