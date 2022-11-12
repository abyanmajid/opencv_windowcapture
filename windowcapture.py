from turtle import title
import numpy as np
import win32gui
import win32ui
import win32con

class WindowCapture:
    
    # PROPERTIES
    w = 0 # Width of window
    h = 0 # Height of window
    hwnd = None # Which window to capture
    cropped_x = 0
    cropped_y = 0
    
    # CONSTRUCTOR
    def __init__(self, window_name):
        # Find window
        self.hwnd = win32gui.FindWindow(None, window_name)
        if not self.hwnd:
            raise Exception('Window not found: {}'.format(window_name))
        
        # Get window size
        window_rect = win32gui.GetWindowRect(self.hwnd)
        self.w = window_rect[2] - window_rect[0]
        self.h = window_rect[3] - window_rect[1]
        
        # Removing window border and titlebar
        border_pixels = 8
        titlebar_pixels = 30
        self.w -= (border_pixels*2)
        self.h -= titlebar_pixels - border_pixels
        self.cropped_x = border_pixels
        self.cropped_y = titlebar_pixels
    
    # METHODS
    def get_screenshot(self):
        
        # Get window image data
        wDC = win32gui.GetWindowDC(self.hwnd)
        dcObj=win32ui.CreateDCFromHandle(wDC)
        cDC=dcObj.CreateCompatibleDC()
        dataBitMap = win32ui.CreateBitmap()
        dataBitMap.CreateCompatibleBitmap(dcObj, self.w, self.h)
        cDC.SelectObject(dataBitMap)
        cDC.BitBlt((0,0),(self.w, self.h) , dcObj, (self.cropped_x, self.cropped_y), win32con.SRCCOPY)
        
        # saving the screenshot as bmp file
        # bmpfilenamename = 'debug.bmp'
        # dataBitMap.SaveBitmapFile(cDC, bmpfilenamename)
        signedIntsArray = dataBitMap.GetBitmapBits(True)
        img = np.fromstring(signedIntsArray, dtype='uint8')
        img.shape = (self.h, self.w, 4)
        
        # Free Resources
        dcObj.DeleteDC()
        cDC.DeleteDC()
        win32gui.ReleaseDC(self.hwnd, wDC)
        win32gui.DeleteObject(dataBitMap.GetHandle())
        
        # done without img slicing
        
        return img # return object
    
    # For finding name of a window
    def list_window_names(self):
        def winEnumHandler(hwnd, ctx):
            if win32gui.IsWindowVisible(hwnd):
                print(hex(hwnd), win32gui.GetWindowText(hwnd))
        win32gui.EnumWindows(winEnumHandler, None)