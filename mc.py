import random as rd
import numpy as np
import matplotlib as mlp
import matplotlib.pyplot as plt
import matplotlib.patches as patch
import time
start_time = time.time()
from math import pi

inside = 0
outside = 0
coords = []
# ----Plotting the circle and the rectangle-------
x = np.linspace(0, 1, 200)
y = np.sqrt((0.5 ** 2) - ((x - 0.5) ** 2)) + 0.5  # Upper half of circle
neg_y = -np.sqrt(0.25 - ((x - 0.5) ** 2)) + 0.5  # Lower half of circle
fig, ax = plt.subplots()
ax.plot(x, y, 'blue')
ax.plot(x, neg_y, 'blue')
rect = patch.Rectangle((0, 0), 1, 1, linewidth=1, fill=False)
ax.add_patch(rect)
ax.axis('equal')
ax.axis('off')
# ---------Loop that creates each frame for animation--------
N=100
for i in range(1, N):
    x_rand = rd.random()  # Random x coordinate
    y_rand = rd.random()  # Random y coordinate
    if (x_rand - 0.5) ** 2 + (y_rand - 0.5) ** 2 < (1 / 4):  # If the (x,y) coordinate falls inside the circle
        ax.plot(x_rand, y_rand, 'go', markersize=1)
        inside += 1
    else:
        ax.plot(x_rand, y_rand, 'ko', markersize=1)
        outside += 1
    pi_mc = 4 * (inside / (inside + outside))
    ax.set_title("$\pi$ = " + str(format(pi_mc ,'.7f'))+" "+str(i))  # Show 7 decimal places of Pi
    
    if i < 10:  
        plt.savefig("000000" + str(i))
    if i >= 10 and i <100:
        plt.savefig("00000" + str(i))
    if i >= 100 and i < 1000:
        plt.savefig("0000"+ str(i))
    if i >= 1000 and i < 10000:
        plt.savefig("000"+ str(i))
    if i >= 10000 and i < 100000:
        plt.savefig("00"+ str(i))

    print(i)

import cv2
import numpy as np
import glob

img_array = []
for filename in sorted(glob.glob('C:/Users/jack7/Documents/pi/*.png')):
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width,height)
    img_array.append(img)

out = cv2.VideoWriter('project.mp4',cv2.VideoWriter_fourcc(*'DIVX'), 30, size)
 
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()

#delete pngs at end

print(time.time() - start_time)

#add subplot for error

