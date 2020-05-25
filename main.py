import pyautogui
import time
import logging


def windows_search(text):
    search = None
    time_end = time.time() + 10
    logging.debug('Looking for Windows search bar')
    while search is None and time.time() < time_end:
        try:
            search = pyautogui.locateCenterOnScreen(r'Images/WindowsSearchBar.PNG', grayscale=False, confidence=.9)
            time.sleep(0.5)
        except TypeError:
            print('Waiting for Search Bar')
    if search is None and time.time() > time_end:
        print('Could not find Search Bar')
        logging.error('Could not find Search Bar')
        pyautogui.screenshot(r'Screenshots/CouldNotFindWindowsSearchBar.png')
        exit()
    print('Found Search Bar')
    logging.debug('Found Windows Search Bar')
    pyautogui.click(search)
    pyautogui.typewrite(text)


def windows_open():
    open_program = None
    time_end = time.time() + 10
    logging.debug('Looking for Open')
    while open_program is None and time.time() < time_end:
        try:
            open_program = pyautogui.locateCenterOnScreen(r'Images/OpenProgram.PNG', grayscale=False, confidence=.9)
        except TypeError:
            print('Waiting for Open')
    if open_program is None and time.time() > time_end:
        print('Could not find Open')
        logging.error('Could not find Open')
        pyautogui.screenshot(r'Screenshots/CouldNotFindOpen.png')
        exit()
    print('Found Open')
    logging.debug('Found Open')
    pyautogui.click(open_program)


def paint_blue():
    blue = None
    time_end = time.time() + 10
    logging.debug('Looking for blue')
    while blue is None and time.time() < time_end:
        try:
            blue = pyautogui.locateCenterOnScreen(r'Images/PaintBlue.PNG', grayscale=False, confidence=.9)
        except TypeError:
            print('Waiting for blue')
    if blue is None and time.time() > time_end:
        print('Could not find blue')
        logging.error('Could not find blue')
        pyautogui.screenshot(r'Screenshots/CouldNotFindBlue.png')
        exit()
    print('Found blue')
    logging.debug('Found blue')
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
    logging.debug('Completed letter h')


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
    logging.debug('Completed letter e')


def hello_l1():
    pyautogui.moveTo(467, 350)
    pyautogui.dragTo(499, 350)
    pyautogui.dragTo(499, 430)
    pyautogui.dragTo(548, 430)
    pyautogui.dragTo(548, 453)
    pyautogui.dragTo(467, 453)
    pyautogui.dragTo(467, 350)
    print('Completed letter l1')
    logging.debug('Completed letter l1')


def hello_l2():
    pyautogui.moveTo(562, 350)
    pyautogui.dragTo(594, 350)
    pyautogui.dragTo(594, 430)
    pyautogui.dragTo(644, 430)
    pyautogui.dragTo(644, 453)
    pyautogui.dragTo(562, 453)
    pyautogui.dragTo(562, 350)
    print('Completed letter l2')
    logging.debug('Completed letter l2')


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
    logging.debug('Completed letter o')


def paint_text():
    text_icon = None
    time_end = time.time() + 10
    logging.debug('Looking for Paint textbox')
    while text_icon is None and time.time() < time_end:
        try:
            text_icon = pyautogui.locateCenterOnScreen(r'Images/PaintText.PNG', grayscale=False, confidence=.9)
        except TypeError:
            print('Waiting for Paint textbox')
    if text_icon is None and time.time() > time_end:
        print('Could not find Paint textbox')
        logging.error('Could not Paint textbox')
        pyautogui.screenshot(r'Screenshots/CouldNotFindPaintText.png')
        exit()
    print('Found Paint textbox')
    logging.debug('Found Paint textbox')
    pyautogui.click(text_icon)


def text_box_world():
    pyautogui.moveTo(244, 509)
    pyautogui.dragTo(846, 742)
    pyautogui.typewrite('World', 0.5)


def windows_close():
    close = None
    time_end = time.time() + 10
    logging.debug('Looking for x to close program')
    while close is None and time.time() < time_end:
        try:
            close = pyautogui.locateCenterOnScreen(r'Images/CloseProgram.PNG', grayscale=False, confidence=.9)
        except TypeError:
            print('Waiting for x')
    if close is None and time.time() > time_end:
        print('Could not find x')
        logging.error('Could not find x')
        pyautogui.screenshot(r'Screenshots/CouldNotFindX.png')
        exit()
    print('Found x')
    logging.debug('Found x')
    pyautogui.click(close)


def windows_dont_save():
    no_save = None
    time_end = time.time() + 10
    logging.debug('Looking for Don\'t Save')
    while no_save is None and time.time() < time_end:
        try:
            no_save = pyautogui.locateCenterOnScreen(r'Images/WindowsDontSave.PNG', grayscale=False, confidence=.9)
        except TypeError:
            print('Waiting for Don\'t Save')
    if no_save is None and time.time() > time_end:
        print('Could not find Don\'t Save')
        logging.error('Could not find Don\'t Save')
        pyautogui.screenshot(r'Screenshots/CouldNotFindDontSave.png')
        exit()
    print('Found paint Don\'t Save')
    logging.debug('Found paint Don\'t Save')
    pyautogui.click(no_save)

