import numpy as np

def calculate(list):
    if len(list) < 9:
        raise ValueError('List must contain nine numbers')
    else:
        arr = np.array([(list[0:3]), (list[3:6]), (list[6:9])])


    print(arr)
    print(arr.shape)
    #return calculations

calculate([1, 2, 3, 4, 5, 6, 7, 8, 9])