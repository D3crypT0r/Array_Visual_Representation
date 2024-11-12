import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def visualize_3d_array(arr):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    x, y, z = np.indices(arr.shape)
    
    x = x.flatten()
    y = y.flatten()
    z = z.flatten()
    values = arr.flatten()
    
    color_map = plt.cm.viridis(values / float(values.max()))  
    size_map = (values / values.max()) * 100  
    
    sc = ax.scatter(x, y, z, c=color_map, s=size_map, edgecolor="k", alpha=0.7)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.set_title("3D Array Visualization - By D3crypT0r")
    
    plt.show()

arr_3d = np.random.randint(0, 20, size=(5, 5, 5))  
visualize_3d_array(arr_3d)
