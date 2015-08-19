import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def plot_mnist_digit(image):
    '''Plot a single MNIST image.'''
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.matshow(image, cmap = matplotlib.cm.binary)
    plt.xticks(np.array([]))
    plt.yticks(np.array([]))
    plt.show()

def plot_10_by_10_images(images):
    ''' Plot 100 MNIST images in a 10 by 10 table. Note that we crop
    the images so that they appear reasonably close together.  The
    image is post-processed to give the appearance of being continued.'''
    fig = plt.figure()
    images = [image[3:25, 3:25] for image in images]
    #image = np.concatenate(images, axis=1)
    for x in range(10):
        for y in range(10):
            ax = fig.add_subplot(10, 10, 10*y+x)
            ax.matshow(images[10*y+x], cmap = matplotlib.cm.binary)
            plt.xticks(np.array([]))
            plt.yticks(np.array([]))
    plt.show()

def plot_first_k_numbers(X,k):
    m = X.shape[0]
    k = min(m,k)
    j = int(round(k / 10.0))

    fig, ax = plt.subplots(j,10)

    for i in range(k):
        w=X[i,:]

        w=w.reshape(28,28)
        ax[i/10, i%10].imshow(w, cmap=plt.cm.gist_yarg, interpolation='nearest', aspect='equal')
        ax[i/10, i%10].axis('off')

    plt.tick_params(
        axis='x',          # changes apply to the x-axis
        which='both',      # both major and minor ticks are affected
        bottom='off',      # ticks along the bottom edge are off
        top='off',         # ticks along the top edge are off
        labelbottom='off')
    plt.tick_params(
        axis='y',          # changes apply to the x-axis
        which='both',      # both major and minor ticks are affected
        left='off',
        right='off',    # ticks along the top edge are off
        labelleft='off')

    fig.show()
