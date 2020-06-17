from matplotlib import pyplot as plt
import os
import numpy as np

def checkFolder():
    if not os.path.exists('Plots'):
        os.makedirs('Plots')

def plotGraph(pickleArr):
    checkFolder()
    plt.xlabel('Frames')
    plt.ylabel('Pickles')
    plt.plot(pickleArr)
    plt.savefig('Plots/fp32Plt.png')
    plt.show()