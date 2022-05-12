# -*- coding: utf-8 -*-
# import logging.config
# from settings import logger_config

# logging.config.dictConfig(logger_config)
# logger = logging.getLogger('app_logger')
from keyboard import press_and_release
from time import sleep
import pyautogui, pyperclip

def paste(text: str):
    pyperclip.copy(text)
    press_and_release('ctrl + v')


def type(text: str, interval=0.0):
    buffer = pyperclip.paste()
    if not interval:
        paste(text)
    else:
        for char in text:
            paste(char)
            sleep(interval)
    pyperclip.copy(buffer)




pyautogui.hotkey('Win')
type('блокнот', 0.2)
pyautogui.keyDown('Enter')
sleep(5)
type('hello world', 0.2)
press_and_release('ctrl + a')
press_and_release('ctrl + c')
pyautogui.keyDown('Down')
pyautogui.keyDown('Enter')
pyautogui.keyDown('Enter')
press_and_release('ctrl + v')


# keyboard.press_and_release('ctrl + v')
# import pyautogui, pyperclip, keyboard

# def paste(text: str):
#     buffer = pyperclip.paste()
#     pyperclip.copy(text)
#     keyboard.press_and_release('ctrl + v')
#     pyperclip.copy(buffer)


# pyautogui.hotkey('Win')
# paste("Привет мир!")

# ***********************************************************************
# -----------------------------------------------------------------------
#
def main():
    pass
    # logger.info("Start ")
    #
    # logger.info("End")


# -----------------------------------------------------------------------
if __name__ == '__main__':
    main()
