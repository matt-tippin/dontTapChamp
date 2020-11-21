#Author: Matt Tippin
#Date: Nov 21, 2020
#Note: I got bored on a rainy day and made this to beat a game that was frustrating me

#REQUIREMENTS:
#I based this program on the assumption that donttap.com will be open in a chrome window covering the screen on 1980x1080 res.

#TO USE:
#Start your don't tap game, start this file, and enjoy.

import numpy as np
from PIL import ImageGrab
import cv2
import time
import pyautogui
import array as arr
from datetime import datetime

def process_img(original_image):
    processed_img = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    gray = cv2.cvtColor(original_image,cv2.COLOR_BGR2GRAY)
    processed_img = (cv2.threshold, 15, 255, cv2.THRESH_BINARY_INV)

    return processed_img

def click(x,y):
	pyautogui.click(x,y)

def clickBlock(x,y):
	newX=(x*164)+617+82
	newY=(y*164)+240+82
	pyautogui.click(newX,newY)

def clickBlack(screen):
	for x in range(0,4):
		for y in range(0,4):
			color=screen[(x*165)+82][(y*165)+80]
			if color[0]==0 and color[1]==0 and color[2]==0:
				clickBlock(y,x)
				x=4;
				y=4;
				break

def main():
   last_time = time.time()
   start_time=time.time()
   while(start_time-last_time<10):
        screen =  np.array(ImageGrab.grab(bbox=(617,240,1250,900)))
        process_img(screen);
        clickBlack(screen);
        last_time = time.time()
        cv2.namedWindow("Output", cv2.WINDOW_NORMAL)
        screen = cv2.cvtColor(screen,cv2.COLOR_BGR2GRAY)
        cv2.imshow('Output', screen)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

main()