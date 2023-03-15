from PIL import ImageGrab
from os import getcwd,getlogin,environ,system
from datetime import datetime
from winsound import PlaySound,SND_FILENAME
from pyautogui import hotkey

hotkey("win","down")  # to minimize command prompt

now = datetime.now()  # To get time
date_now = str(now.day)+"."+str(now.month)+"."+str(now.year)+" "+str(now.hour)+"."+str(now.minute)+"."+str(now.second) # To have time as variable as desired format

img = ImageGrab.grabclipboard()  # Get picture from clipboard as variable

if (img is None) or (type(img) is list):  # Control of if item is not picture and handling stiuations (item == text or empty)
    PlaySound("Windows Foreground.wav",SND_FILENAME)  # playing error sound
    exit()
else:  # Easy code reading purposes
    pass


img.save(environ["HOMEPATH"] + "\Desktop\\" + date_now + ".png")  # saving image to desired location. Using environ makes sure to get users homepath
# currently it's set to save image to desktop location.
