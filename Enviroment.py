import cv2
from mss import mss
import numpy as np


class Environment:
    def __init__(self, agent=None):
        self.agent = agent

    def screenshot(self):
        with mss() as sct:
            return sct.shot()

    def send(self, action):
        if action == ">":
            return np.array(self.screenshot())

    def show_picture(self, img):
        cv2.imshow("OpenCV/Numpy normal", img)


# class Racist_Agent:
#     def __init__(self):


if __name__ == "__main__":
    e = Environment()
    e.show_picture(e.send(e.screenshot()))
