import cv2
from mss import mss
import numpy as np


class Environment:
    def __init__(self, monitor):
            self.monitor = mss.monitors[1]

    def screenshot(self):
        with mss() as sct:
            return sct.grab(self.monitor)

    def send(self, action):
        # Si recibimos una acción del agente enviamos una nueva captura de pantalla, también transformamos su color
        if action:
            return cv2.cvtColor(np.array(self.screenshot()), cv2.COLOR_BGRA2BGR)