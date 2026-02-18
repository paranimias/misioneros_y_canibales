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
        if action:
            return cv2.cvtColor(np.array(self.screenshot()), cv2.COLOR_BGRA2BGR)

    def show_picture(self, img):
        cv2.imshow("OpenCV/Numpy normal", img)


# class Racist_Agent:
#     def __init__(self):


if __name__ == "__main__":
    e = Environment()
    while True:
        e.show_picture(e.send(e.screenshot()))

        # REQUIRED for window refresh
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()