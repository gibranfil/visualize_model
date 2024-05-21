import matplotlib.pyplot as plt
from math import floor


def plot_images(images,rows=3, cols=3):
    num_images = len(images)
    stride = floor(num_images / (rows * cols))
    fig, axes = plt.subplots(nrows=rows, ncols=cols, figsize=(cols *3, rows * 3))

    count = 0
    for row in range (rows) :
        for col in range (cols) :
            axes[row, col].imshow(images[:,:,stride*count], cmap='gray')  # You might need to adjust the cmap according to your images
            axes[row, col].set_title('Label: {}'.format(stride*count))
            axes[row, col].axis('off')
            count +=1
    plt.tight_layout()
    plt.show()