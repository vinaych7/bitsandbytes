import numpy as np

arr = np.array([[1, 1, 1, 1, 1, 1, 1],
                [2, 2, 2, 2, 2, 2, 2],
                [3, 3, 3, 3, 3, 3, 3],
                [4, 4, 4, 4, 4, 4, 4],
                [5, 5, 5, 5, 5, 5, 5],
                [6, 6, 6, 6, 6, 6, 6],
                [7, 7, 7, 7, 7, 7, 7]])

kernel = np.array([[1, 1, 1],
                   [1, 1, 1],
                   [1, 1, 1]])


def stride_conv(array, kernel, s):
    width, height = array.shape
    kernw, kernh = kernel.shape
    beg = 0
    end = kernw
    final = []
    xlim = (width - (width % kernw)) - 1
    for i in range(0, xlim, s):
        k = []

        ylim = (height - (height % kernh)) - 1
        for j in range(0, ylim, s):
            k.append(np.sum(array[beg+i: end+i, beg+j:end+j] * (kernel)))
        final.append(k)

    return np.array(final)


result = stride_conv(arr, kernel, 3)
print(result)
