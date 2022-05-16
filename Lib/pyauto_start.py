# -*- coding: utf-8 -*-
# import logging.config
# from settings import logger_config

# logging.config.dictConfig(logger_config)
# logger = logging.getLogger('app_logger')
import keyboard as keyb
from time import sleep
import pyautogui, pyperclip
import win32api
import os
import subprocess
import psutil


def menu_pusk(name_prog):
    pyautogui.hotkey('Win')
    type(name_prog, 0.2)
    sleep(3)
    pyautogui.keyDown('Enter')



def koordinati():
    keyb.wait('space')
    print (win32api.GetCursorPos())

def bloknot():
    pyautogui.keyDown('Down')
    keyb.wait('space')
    pyautogui.leftClick(1066, 258)
    keyb.press('shift')
    pyautogui.leftClick(1129, 600)
    keyb.press_and_release('ctrl + c')
    keyb.release('shift')

    # keyb.press_and_release('ctrl + a')
    # keyb.press_and_release('shift+y')
    # keyb.press('shift +ctrl')
    # keyb.write('ghbdtn')
    # keyb.release('shift+d, space')
    # keyb.press_and_release('shift+end')
    # keyb.send('a')
    # keyb.wait('ctrl')
    # # keyb.release('right shift+end')
    # keyb.press_and_release('ctrl + a')
    # sleep(2)


    # keyb.play(a)
    # a=keyb.record('alt')
    # print(a)
    # pyautogui.leftClick(1912, 1051)
    # sleep(0.5)
    # pyautogui.doubleClick(1339, 860)
    # press_and_release('right shift+down')
    # press_and_release('right shift+down')
    # pyautogui.hotkey('Win')
    # type('блокнот', 0.2)
    # pyautogui.keyDown('Enter')
    # sleep(1)
    # type('hello world', 0.2)
    # # press_and_release('ctrl + a')
    # # press_and_release('ctrl + c')
    # press_and_release('home')
    # sleep(1)
    # press_and_release('shift+right')
    # sleep(1)
    # press_and_release('ctrl + c')
    # press_and_release('enter')
    # pyautogui.keyDown('Down')
    # pyautogui.keyDown('Enter')
    # pyautogui.keyDown('Enter')
    # press_and_release('ctrl + v')
    # # pyautogui.moveTo(1774, 178)
    # sleep(1)
    # pyautogui.click(1774, 178, 1, 0.05, 'left')
    # sleep(1)
    # pyautogui.click(956, 536, 1, 0.05, 'left')



def paste(text: str):
    pyperclip.copy(text)
    keyb.press_and_release('ctrl + v')


def type(text: str, interval=0.0):
    buffer = pyperclip.paste()
    if not interval:
        paste(text)
    else:
        for char in text:
            paste(char)
            sleep(interval)
    pyperclip.copy(buffer)

# def free_commander():
#     os.system('c:\\Users\\Programmer\\Desktop\\tot\\FreeCommander.exe')

def transfer_fanuc():
    pyautogui.leftClick(294, 461)#первая программа
    keyb.press('shift')
    sleep(3)
    pyautogui.leftClick(295, 531)#последняя программа
    keyb.release('shift')
    sleep(1)
    pyautogui.rightClick(295, 531)#контекстн меню
    sleep(1)
    pyautogui.leftClick(354, 550)#uploat
    sleep(1)
    pyautogui.leftClick(374, 654)#yes to all
    sleep(1)
    pyautogui.leftClick(936, 621)# complite
    sleep(6)
    pyautogui.leftClick(1051, 593)
    sleep(3)

def Program_Transfer_Tool():
    # os.startfile('c:\\"Program Files (x86)"\\FANUC\\"Program Transfer Tool"\\Bin\\PttMain.exe')

    os.startfile(r'C:\Program Files (x86)\FANUC\Program Transfer Tool\Bin\PttMain.exe')
    sleep(3)
    pyautogui.leftClick(1851, 261)#full screen
    pyautogui.leftClick(106, 464)#открываем next26
    pyautogui.leftClick(136, 588)#part1
    sleep(3)
    pyautogui.leftClick(1074, 447)#последняя модификация
    sleep(3)
    transfer_fanuc()
    pyautogui.leftClick(136,603) # part2
    sleep(3)
    transfer_fanuc()
    #--------------------------------------
    pyautogui.leftClick(93,623) # hanhwa
    sleep(3)
    pyautogui.leftClick(91, 510) # part1
    sleep(1)
    transfer_fanuc()
    pyautogui.leftClick(92,528) # part2
    sleep(3)
    transfer_fanuc()
    #--------------------------------------
    pyautogui.leftClick(93, 541) # miano
    sleep(3)
    pyautogui.leftClick(88, 525) # part1
    sleep(1)
    transfer_fanuc()
    pyautogui.leftClick(92, 540) # part2
    sleep(3)
    transfer_fanuc()
    #--------------------------------------
    pyautogui.leftClick(94, 559) # colchester
    sleep(3)
    pyautogui.leftClick(92, 541) # part1
    sleep(1)
    transfer_fanuc()
    #--------------------------------------
    pyautogui.leftClick(106, 590) # nexturn12
    sleep(3)
    pyautogui.leftClick(92, 574) # part1
    sleep(1)
    transfer_fanuc()
    pyautogui.leftClick(96, 591) # part2
    sleep(3)
    transfer_fanuc()
    sleep(3)
    for process in (process for process in psutil.process_iter() if process.name() == "PttMain.exe"):
        process.kill()








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
    # koordinati()
    Program_Transfer_Tool()
    # free_commander()
    # bloknot()
    # logger.info("Start ")
    #
    # logger.info("End")


# -----------------------------------------------------------------------
if __name__ == '__main__':
    main()
