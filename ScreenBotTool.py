import os 
import numpy as np
import pygetwindow as gw
from PIL import Image
import mss
import cv2
import time
import keyboard


class StartUp:

  

    def CheckIfFolder(self):
        folderT, folderF = f"ScreenShotForTrain/True", f"ScreenShotForTrain/False"
        if os.path.exists(folderT):
            print("Ordner True existiert!")
        else:
            print("Der Ordner existiert nicht!")
            os.makedirs(folderT)

        if os.path.exists(folderF):
            print("Ordner False existiert!")
        else:
            print("Der Ordner existiert nicht!")
            os.makedirs(folderF)

# Kann später enfernt werden
time.sleep(2.1)

def TakeSaveIMG():

    while True:
        with mss.mss() as sct:
            
    

            # Get information of monitor 2
            monitor_number = 1
            mon = sct.monitors[monitor_number]

            # The screen part to capture
            monitor = {
                "top": mon["top"],
                "left": mon["left"],
                "width": mon["width"],
                "height": mon["height"],
                "mon": monitor_number,
            }
        # output = "sct-mon{mon}_{top}x{left}_{width}x{height}.png".format(**monitor)

            # Grab the data
        # sct_img = sct.grab(monitor)
        # img = np.array(sct.grab(monitor)) # BGR Image
            

    
            saveLPath = ""

            date_string = time.strftime("%Y-%m-%d-%H-%M-%S")

        
            if keyboard.read_key() == "t":
                print("T got clicked")

                ct_img = sct.grab(monitor)
                img = np.array(sct.grab(monitor)) # BGR Image

                cv2.imwrite(f"ScreenShotForTrain/True/{date_string}.jpeg", img)
                saveLPath = f"ScreenShotForTrain/True/{date_string}.jpeg"

            elif keyboard.read_key() == "f":
                print("F got clicket")

                ct_img = sct.grab(monitor)
                img = np.array(sct.grab(monitor)) # BGR Image

                cv2.imwrite(f"ScreenShotForTrain/False/{date_string}.jpeg", img)
                saveLPath = f"ScreenShotForTrain/True/{date_string}.jpeg"

            else:
                continue
                


            print(saveLPath)
            # Create Function thats used as Overlay on Aplication Window
            # Display the picture

            #imgForWindow = cv2.imread(saveLPath)
            imgForWindowS = cv2.resize(img, (700,700))


            cv2.imshow("CurrentPic", imgForWindowS)
            cv2.resizeWindow("CurrentPic", 700, 700) 
        
            cv2.setWindowProperty("CurrentPic", cv2.WND_PROP_TOPMOST, 1)

            cv2.waitKey(1)








StartUp = StartUp()
StartUp.CheckIfFolder()


TakeSaveIMG()