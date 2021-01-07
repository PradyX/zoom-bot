import subprocess
import pyautogui
import time
import pandas as pd
from datetime import datetime   

def openZoom():
    # uncomment for Windows
    subprocess.Popen(r"C:\Users\prady\AppData\Roaming\Zoom\bin\Zoom.exe") # Change username here

    # uncomment for Linux
    #subprocess.call(["zoom"])

    time.sleep(15)
    
openZoom()
