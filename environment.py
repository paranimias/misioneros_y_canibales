import time
import cv2
import webbrowser
from pyautogui import click
from mss import mss
import numpy as np


class Environment:
    def __init__(self):
        # Estas son las reglas para iniciar el juego
        self.rules = [
            ((465, 905), (102, 205, 255), lambda: click(x=540, y=960), False),
            ((210, 978), (0, 56, 223), lambda: click(x=946, y=658), False),
            ((200, 943), (0, 255, 255), lambda: click(x=945, y=891), True),
        ]

    def screenshot(self):
        with mss() as sct:
            screenshot1 = sct.grab(sct.monitors[1])
            arrayBGR = cv2.cvtColor(np.array(screenshot1), cv2.COLOR_BGRA2BGR)
            return arrayBGR

    def response(self, action):
        if action == "*":
            respuesta = self.screenshot()
            return respuesta
        else:
            return False

    def start_browser(self):
        webbrowser.open(
            "https://www.novelgames.com/es/missionaries/pwa/iframe.php?memberID=ng&settingID=gswww&hideMoreGamesButton=true"
        )

    def start_game(self, capture):
        # Primero recorremos los colores del inicio del juego
        for (row, column), color, action, is_final in self.rules:
            if tuple(capture[row][column]) == color:
                action()
                return is_final
        return False
