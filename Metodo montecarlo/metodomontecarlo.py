# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 16:28:33 2021

@author: AdrianTR
"""


import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Calcule el valor de pi y separe los puntos dentro y fuera del círculo para dibujar fácilmente
def cal_pi(random_points):
    inCircle_points = []  # Punto interior del círculo
    outCircle_points = []  # Puntos exteriores (y puntos a los lados)

    for point in random_points:
        x = point[0]
        y = point[1]
        if (x - 0.5) ** 2 + (y - 0.5) ** 2 < 0.25:
            inCircle_points.append([x, y])
        else:
            outCircle_points.append([x, y])

    ratio = len(inCircle_points) / len(random_points)
    pi = 4 * ratio

    return pi, inCircle_points, outCircle_points

def plot_data(random_points):
    pi_estimation, inCircle_points, outCircle_points = cal_pi(random_points)
    print('El valor de pi estimado es:', pi_estimation)

    fig1 = plt.figure()
    # Dibuja el contorno del círculo
    ax1 = fig1.add_subplot(111, aspect='equal')
    ax1.add_patch(
        patches.Circle((0.5, 0.5), 0.5, fill=False, lw=2))

    # Dibuja los puntos dentro y fuera del círculo
    ax1.plot(np.array(inCircle_points)[:, 0], np.array(inCircle_points)[:, 1],
             'go', alpha=0.3, markersize=0.5)
    ax1.plot(np.array(outCircle_points)[:, 0], np.array(outCircle_points)[:, 1], 'ro', alpha=0.3, markersize=0.5)

    plt.axis([0, 1, 0, 1])  # Restricción del rango del eje de coordenadas
    plt.title('$\pi\\approx' + str(pi_estimation) + '$')
    plt.show()

n = (100, 1000, 10000, 1000000, 10000000)

for i in n:
     print ("El valor de pi es: {0:2.8f} para n {1}".format((i),i))