'''functions to draw 10 random circles'''

import numpy as np
import matplotlib.pyplot as plt
import random as ran
 
def draw_circle(ax, x0, y0, R, N):
    theta = np.linspace(0, 2.0*np.pi, int(N))
    x = float(x0) + float(R) * np.cos(theta)
    y = float(y0) + float(R) * np.sin(theta)
    
    ax.set_xlabel(r'x = Rcos($\theta$)')
    ax.set_ylabel(r'x = Rcos($\theta$)')
    ax.plot(x, y)

    return ax

def draw_circles():
    fig = plt.figure()
    ax = fig.add_subplot(111)

    ax.set_aspect('equal')

    for i in range(10):
        draw_circle(ax, ran.uniform(0,1), ran.uniform(0,1), ran.uniform(0,1), 1000)

    fig.set_size_inches(8,8)
    fig

    return fig