import numpy as np 

# implement your function to combine two numpy arrays 

def combination(a, b, axis=0):
    a = np.squeeze(a)
    b = np.squeeze(b)

    if not a.ndim == b.ndim:
        print("the arrays are of different dimensions")
        return
    if a.shape[:axis] != b.shape[:axis] or a.shape[axis+1:] != b.shape[axis+1:]:
        print("Arrays cannot be combined along the specified axis")
        return

    return np.concatenate((a, b), axis)
if __name__ == "__main__":
    a = np.array([[[[1, 2], [3, 4], [5, 6]]]])
    b = np.ones((2,2))
    combination(a, b)
