import numpy as np


# receives an array, returns an array where data gets comulated
def comulate(data):
    tmp = np.zeros(len(data))
    for i in range(0, len(data)):
        tmp[i] = tmp[i-1] + data[i]
    return tmp
