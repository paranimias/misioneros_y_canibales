import time
import cv2
import webbrowser
from pyautogui import click, moveTo, press
from mss import mss
import numpy as np


class Environment:
    def __init__(self):
        # Estas son las reglas para iniciar el juego

        # self.rules = [
        #    ((465, 905), (102, 205, 255), lambda: click(x=540, y=960), es_final = False),
        #    ((210, 978), (0, 56, 223), lambda: click(x=946, y=658), es_final = False),
        #    ((200, 943), (0, 255, 255), None (Tenemos que ejecutar dos acciones: mover el mouse y hacer click), es_final = True), # ]
        self.rules = [
            ((465, 905), (102, 205, 255), lambda: click(x=540, y=960), False),
            ((210, 978), (0, 56, 223), lambda: click(x=946, y=658), False),
            ((200, 943), (0, 255, 255), None, True),
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
        time.sleep(2)
        press('f11')

    def start_game(self, capture):
        # Primero recorremos los colores del inicio del juego
        for (row, column), color, action, is_final in self.rules:
            if tuple(capture[row][column]) == color and not is_final:
                action()
                return is_final
            elif tuple(capture[row][column]) == color and is_final:
                # Debemos mover primero el mouse, y luego hacer click, sino el programa puede no iniciarse
                moveTo(945, 891)
                click()
                return is_final

