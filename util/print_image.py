import matplotlib.pyplot as plt
import numpy as np
from math import floor


def plot_images(images,rows=3, cols=3):
    num_images = len(images)
    stride = floor(num_images / (rows * cols))
    fig, axes = plt.subplots(nrows=rows, ncols=cols, figsize=(cols *3, rows * 3))

    count = 0
    for row in range (rows) :
        for col in range (cols) :
            axes[row, col].imshow(images[:,:,stride*count], cmap='gray')
            axes[row, col].set_title('Label: {}'.format(stride*count))
            axes[row, col].axis('off')
            count +=1
    plt.tight_layout()
    plt.show()


def reshape_output (output) :
    empty= []

    for i in range(len (output)) :
        size = output [i].shape[1]
        temp = np.squeeze(output[i],axis=0)
        temp = temp [(size//2):(size//2+1),:,:,1]
        for index, value in enumerate(temp.shape):
            
            if value == 1:
                to_squeeze = index
        temp = np.squeeze(temp,axis= to_squeeze)
        empty.append (temp)

    return empty



def plot_layer(images,rows=3, cols=3):
    num_images = len(images)
    stride = floor(num_images / (rows * cols))
    fig, axes = plt.subplots(nrows=rows, ncols=cols, figsize=(cols *3, rows * 3))

    count = 0
    for row in range (rows) :
        for col in range (cols) :
            if  count +1 == rows*cols :
                axes[row, col].imshow(images[num_images-1], cmap='gray')
                axes[row, col].set_title('Layer: {}'.format(num_images))
                axes[row, col].axis('off')
                pass
            else :
                axes[row, col].imshow(images[count*stride], cmap='gray')
                axes[row, col].set_title('Layer: {}'.format(stride*count))
                axes[row, col].axis('off')
                count +=1
    plt.tight_layout()
    plt.show()
    print (count)
