import cv2
from mss import mss
import numpy as np


class Environment:
    def __init__(self, agent=None):
        self.agent = agent

    def screenshot(self):
        with mss() as sct:
            monitor = sct.monitors[1]
            return sct.grab(monitor)

    def send(self, action):
        # Si recibimos una acción del agente enviamos una nueva captura de pantalla, también transformamos su color
        if action:
            return cv2.cvtColor(np.array(self.screenshot()), cv2.COLOR_BGRA2BGR)

    def show_picture(self, img):
        cv2.imshow("OpenCV/Numpy normal", img)

if __name__ == "__main__":
    e = Environment()
    imagen_transformada = e.send(e.screenshot())
    # print(type(imagen_transformada[1079][950]))
    e.show_picture(imagen_transformada)
    while True:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()