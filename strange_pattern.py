import numpy as np

# implement the function strange pattern

def strange_pattern(shape):
    a = np.zeros(shape, dtype=bool)
    a[::3, ::3] = True
    a[2::3, 1::3] = True
    a[1::3, 2::3] = True
    print(a)
    return a    

if __name__ == "__main__":
    strange_pattern((0, 0));
