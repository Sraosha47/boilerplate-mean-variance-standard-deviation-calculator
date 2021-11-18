import numpy as np

def calculate(list):
    if len(list) < 9:
        raise ValueError('List must contain nine numbers.')
    else:
        arr = np.array([(list[0:3]), (list[3:6]), (list[6:9])])
        flat_arr = arr.flatten()
        calculations = {
            "mean": [arr.mean(axis = 0).tolist(), arr.mean(axis=1).tolist(), flat_arr.mean().tolist()],
            "variance": [arr.var(axis=0).tolist(), arr.var(axis=1).tolist(), flat_arr.var().tolist()],
            "standard deviation": [arr.std(axis=0).tolist(), arr.std(axis=1).tolist(), flat_arr.std().tolist()],
            "max": [arr.max(axis=0).tolist(), arr.max(axis=1).tolist(), flat_arr.max().tolist()],
            "min": [arr.min(axis=0).tolist(), arr.min(axis=1).tolist(), flat_arr.min().tolist()],
            "sum": [arr.sum(axis=0).tolist(), arr.sum(axis=1).tolist(), flat_arr.sum().tolist()]
        }
    return calculations