import matplotlib.pyplot as plt
import time
import random
import statistics as st
import local_common as lc
import numpy as np
import params as pa
from collections import deque


v1 = deque([0]*100)
plt.subplot(211)
plt.ylim([pa.minrssi,pa.maxrssi])
plt.ion()
line1, = plt.plot(v1)
plt.show(block=False)
plt.plot()

def plot_data(value1):
    plt.subplot(211)
    plt.title('%f' % value1)
    v1.appendleft(value1)
    datatoplot = v1.pop()
    print(v1)
    print(datatoplot)
    line1.set_ydata(v1)

    plt.draw()
    plt.pause(0.0001)


if __name__=='__main__':

    while pa.run:
        plot_data(lc.fetch().rssi)
        time.sleep(pa.delay)
