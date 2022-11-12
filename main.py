# Learning OpenCV Part 2
# WINDOW CAPTURE USING PYWIN32 / BY ACCESSING WINDOWS API

from time import time
import cv2 as cv
import numpy as np
from windowcapture import WindowCapture

# Pixel Worlds Catching Fish Box OPENCV Color Detection by Abyan Majid

# Pixel Worlds: 0x1f04b4 Pixel Worlds

# HSV Color Range for Catching Fish Box
fishbox_lower_range = np.array([126, 83, 53])
fishbox_upper_range = np.array([100, 59, 99])

# HSV Color Range For STRIKE
strike_lower_range = np.array([125, 87, 45])
strike_upper_range = np.array([116, 91, 88])

loop_time = time()

windowcapture = WindowCapture('Pixel Worlds') # Set This to Window Name

# Print names of active windows, use if you can't find your window
# windowcapture.list_window_names()

while(True):
    
    screenshot = windowcapture.get_screenshot()
    screenshot = np.array(screenshot)
    
    cv.imshow('Computer vision', screenshot)
    
    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()
    
    # press 'q' with output window focused to exit loop
    # waits 1 ms to recognise process key presses
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break
    
print('Done')