import numpy as np


# removes every part in the begining of data that is smaller than the minimum
def minimum(data, minimum):
    tmp = data.copy()
    counter = 0
    for i in range(0, len(tmp)):
        if tmp[0] < minimum:
            tmp = np.delete(tmp,0)
            counter += 1
        else:
            break
    return [counter, tmp]
