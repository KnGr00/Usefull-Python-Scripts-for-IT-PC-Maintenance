import os
import glob

files = glob.glob("C:/Windows/System32/Config/SystemProfile/AppData/Local/Microsoft/Windows/INetCache/IE/*")
for f in files:
    try:
        os.remove(f)    # Remove all files in Temp folder
    except:
        print("Error cant delete file: " + f)
        pass
print("Done Cleaning IE Cache")
username = os.getlogin()
files = glob.glob("C:/Users/"+ username +"/AppData/Local/Temp/*")
for f in files:
    try:
        os.remove(f)    # Remove all files in Temp folder
    except:
        print("Error cant delete file: " + f)
        pass
print("Done Cleaning Temp")
