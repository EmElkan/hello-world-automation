import pyautogui
import time

def windows_search(text):
    search = None
    time_end = time.time() + 10
    while search is None and time.time() < time_end:
        try:
            search = pyautogui.locateCenterOnScreen('Images//WindowsSearchBar.PNG')
            time.sleep(0.5)  
        except TypeError:
            print('Looking for Search Bar')
    if search is None and time.time() > time_end:
        print('Could not find Search Bar')
        exit()
    print('Found Search Bar')
    pyautogui.click(search)
    pyautogui.typewrite(text) 
        
        
def windows_open():
    open = None
    time_end = time.time() + 10
    while open is None and time.time() < time_end:
        try:
            open = pyautogui.locateCenterOnScreen('Images//OpenProgram.PNG')
        except TypeError:
            print('Looking for Open')
    if open is None and time.time() > time_end:
        print('Could not find Open')
        exit()
    print('Found Open') 
    pyautogui.click(open) 

        
def paint_blue():
    blue = None
    time_end = time.time() + 10
    while blue is None and time.time() < time_end:
        try:
            blue = pyautogui.locateCenterOnScreen('Images//PaintBlue.PNG')       
        except TypeError:
            print('Looking for blue')
    if blue is None and time.time() > time_end:
        print('Could not find blue')
        exit()
    print('Found blue')
    pyautogui.click(blue)
    
    
def hello_h():
    pyautogui.moveTo(243, 350)
    pyautogui.dragTo(276, 350)
    pyautogui.dragTo(276, 386)
    pyautogui.dragTo(308, 386)
    pyautogui.dragTo(308, 350)
    pyautogui.dragTo(341, 350)
    pyautogui.dragTo(341, 453)
    pyautogui.dragTo(308, 453)
    pyautogui.dragTo(308, 411)
    pyautogui.dragTo(276, 411)
    pyautogui.dragTo(276, 453)
    pyautogui.dragTo(243, 453)
    pyautogui.dragTo(243, 350)
    print('Completed letter h')
    

def hello_e():
    pyautogui.moveTo(363, 350)
    pyautogui.dragTo(448, 350)
    pyautogui.dragTo(448, 372)
    pyautogui.dragTo(393, 372)
    pyautogui.dragTo(393, 388)
    pyautogui.dragTo(444, 388)
    pyautogui.dragTo(444, 409)
    pyautogui.dragTo(393, 409)
    pyautogui.dragTo(393, 430)
    pyautogui.dragTo(448, 430)
    pyautogui.dragTo(448, 453)
    pyautogui.dragTo(363, 453)
    pyautogui.dragTo(363, 350)
    print('Completed letter e')
    
    
def hello_l1():
    pyautogui.moveTo(467, 350)
    pyautogui.dragTo(499, 350)
    pyautogui.dragTo(499, 430)
    pyautogui.dragTo(548, 430)
    pyautogui.dragTo(548, 453)
    pyautogui.dragTo(467, 453)
    pyautogui.dragTo(467, 350)
    print('Completed letter l1')
    

def hello_l2():
    pyautogui.moveTo(562, 350)
    pyautogui.dragTo(594, 350)
    pyautogui.dragTo(594, 430)
    pyautogui.dragTo(644, 430)
    pyautogui.dragTo(644, 453)
    pyautogui.dragTo(562, 453)
    pyautogui.dragTo(562, 350)
    print('Completed letter l2')
    

def hello_o():
    pyautogui.moveTo(695, 350)
    pyautogui.dragTo(721, 350)
    pyautogui.dragTo(758, 376)
    pyautogui.dragTo(758, 429)
    pyautogui.dragTo(721, 453)
    pyautogui.dragTo(695, 453)
    pyautogui.dragTo(658, 429)
    pyautogui.dragTo(658, 376)
    pyautogui.dragTo(695, 350)
    pyautogui.moveTo(695, 376)
    pyautogui.dragTo(721, 376)
    pyautogui.dragTo(721, 429)
    pyautogui.dragTo(695, 429)
    pyautogui.dragTo(695, 376)
    print('Completed letter o')
    
    
def paint_text():
    text_icon = None
    time_end = time.time() + 10
    while text_icon is None and time.time() < time_end:
        try:
            text_icon = pyautogui.locateCenterOnScreen('Images//PaintText.PNG')       
        except TypeError:
            print('Looking for paint text')
    if text_icon is None and time.time() > time_end:
        print('Could not find paint text')
        exit()
    print('Found paint text')
    pyautogui.click(text_icon)
    

def text_box_world():
    pyautogui.moveTo(244, 509)
    pyautogui.dragTo(846, 742)
    pyautogui.typewrite('World', 0.5)
    
    
def windows_close():
    close = None
    time_end = time.time() + 10
    while close is None and time.time() < time_end:
        try:
            close = pyautogui.locateCenterOnScreen('Images//CloseProgram.PNG')       
        except TypeError:
            print('Looking for x')
    if close is None and time.time() > time_end:
        print('Could not find x')
        exit()
    print('Found paint x')
    pyautogui.click(close)


def windows_dont_save():
    no_save = None
    time_end = time.time() + 10
    while no_save is None and time.time() < time_end:
        try:
            no_save = pyautogui.locateCenterOnScreen('Images//WindowsDontSave.PNG')       
        except TypeError:
            print('Looking for Don\'t Save')
    if no_save is None and time.time() > time_end:
        print('Could not find Don\'t Save')
        exit()
    print('Found paint Don\'t Save')
    pyautogui.click(no_save)