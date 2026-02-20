import cv2
import nodriver as uc
from pyautogui import click
from mss import mss
import numpy as np


class Environment:
    def __init__(self, monitor):
            self.monitor = mss.monitors[1]

    def send(self, action):
        # Si recibimos una acción del agente enviamos una nueva captura de pantalla, también transformamos su color
        if action:
            return cv2.cvtColor(np.array(self.screenshot()), cv2.COLOR_BGRA2BGR)

    def screenshot(self):
        with mss() as sct:
            screenshot1 = sct.grab(self.monitor)
            return screenshot1

    def response(self, action):
        # Si recibimos una acción del agente enviamos una nueva captura de pantalla, también transformamos su color
        if action:
            arrayBGR = cv2.cvtColor(np.array(self.screenshot()), cv2.COLOR_BGRA2BGR)
            return arrayBGR
        else:
            return None

    # Le decimos al ambiente que inicie el navegador y abra la página
    async def iniciar(self):
        browser = await uc.start()
        page = browser.get('https://www.novelgames.com/es/missionaries/pwa/iframe.php?memberID=ng&settingID=gswww&hideMoreGamesButton=true')
        element = await page.select("#splashAdHolder")
#        display = await element.evaluate(
#            "el => window.getComputedStyle(el).display"
#        )
#        if display == "none":
#            click(x=960,540)
