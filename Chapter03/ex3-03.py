import math
import time
import os

width = 60

while True:
    os.system("clear")

    for y in range(20):
        x = int((math.sin(time.time() * 2 + y * 0.5) + 1) * 20)

        print(" " * x + "*")

    time.sleep(0.05)
