from math import sqrt, ceil
import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np

def all_prime(n):
    # https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

def prime_plot(n):
    '''
    Takes on argument (n), which is a number > 2 and produces a list of all primes up to n.
    Will then show on a plot the primes vs all numbers in range n.
    '''

    x = all_prime(n)
    y = list(range(n))

    data = np.random.rand(10, 10) * 20

    cmap = colors.ListedColormap(['white', 'black'])
    bounds = [0,10,20]
    norm = colors.BoundaryNorm(bounds, cmap.N)

    fig, ax = plt.subplots()
    ax.imshow(data, cmap=cmap, norm=norm)

    # draw gridlines
    ax.grid(which='major', axis='both', linestyle='-', color='k', linewidth=2)
    ax.set_xticks(np.arange(0, 10, 1));
    ax.set_yticks(np.arange(0, 10, 1));

    plt.show()

prime_plot(100)  