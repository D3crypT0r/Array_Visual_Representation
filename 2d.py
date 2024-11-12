import numpy as np
import matplotlib.pyplot as plt

def visualize_2d_array(arr):
    plt.figure(figsize=(8, 8))
    plt.imshow(arr, cmap="coolwarm", aspect="auto")  
    plt.colorbar()  
    plt.title("2D Array Visualization with Gridlines and Annotations")
    plt.xlabel("Columns")
    plt.ylabel("Rows")
    
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            plt.text(j, i, arr[i, j], ha="center", va="center", color="black", fontsize=10)

    plt.grid(visible=True, color="black", linestyle="-", linewidth=0.5) 
    plt.show()

arr_2d = np.random.randint(0, 20, size=(10, 10)) 
visualize_2d_array(arr_2d)
