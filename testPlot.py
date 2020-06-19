import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

plt.ion()
fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')


counter = 0
while True:
    ax.cla()
    if counter % 2 == 0:
        ax.add_patch(
            patches.Rectangle(
                (0.1, 0.1),
                0.5,
                0.5,
                fill=False      # remove background
            ) ) 
    else:
        ax.add_patch(
            patches.Rectangle(
                (0.3, 0.3),
                0.7,
                0.7,
                fill=False      # remove background
            ) ) 
    counter += 1
    fig.canvas.draw()
    fig.canvas.flush_events()