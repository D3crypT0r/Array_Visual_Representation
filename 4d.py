import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

arr = np.arange(1, 82).reshape(3, 3, 3, 3)

colors = ['red', 'green', 'black']

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')
ax.set_box_aspect([1,1,1])

ax.set_xlim(0, 2)
ax.set_ylim(0, 2)
ax.set_zlim(0, 2)

def update(frame):
    ax.cla()  

    w_layer = frame % arr.shape[0]
    current_3d_slice = arr[w_layer, :, :, :]

    for x in range(current_3d_slice.shape[0]):
        for y in range(current_3d_slice.shape[1]):
            for z in range(current_3d_slice.shape[2]):
                value = current_3d_slice[x, y, z]
                ax.scatter(x, y, z, color=colors[w_layer], s=100)
                ax.text(x, y, z, f'{value}', color='white', ha='center', va='center')

    ax.view_init(elev=20, azim=frame * 10)

    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')
    ax.set_title(f'4D Array Visualization -D3crypT0r -  W Layer {w_layer}', fontsize=14)

ani = FuncAnimation(fig, update, frames=36, interval=500, repeat=True)

plt.show()
