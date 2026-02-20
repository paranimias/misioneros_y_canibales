import time
import cv2
import webbrowser
from pyautogui import click
from mss import mss
import numpy as np


class Environment:
    def screenshot(self):
        with mss() as sct:
            screenshot1 = sct.grab(sct.monitors[1])
            return screenshot1

    def response(self, action):
        if action:
            arrayBGR = cv2.cvtColor(np.array(self.screenshot()), cv2.COLOR_BGRA2BGR)
            return arrayBGR
        else:
            return None

    def start_browser(self):
        webbrowser.open("https://www.novelgames.com/es/missionaries/pwa/iframe.php?memberID=ng&settingID=gswww&hideMoreGamesButton=true")