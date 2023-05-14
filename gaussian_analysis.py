import numpy as np

# implement the function gaussian_analysis

def gaussian_analysis(loc, scale, lower_bound, upper_bound):
    if not (isinstance(loc, int) or isinstance(loc, float)):
        print(f"type of loc ist wrong")
        return 
    if not (isinstance(scale, int) or isinstance(scale, float)):
        print(f"type of scale ist wrong")
        return 
    if not (isinstance(lower_bound, int) or isinstance(lower_bound, float)):
        print(f"type of lower_bound ist wrong")
        return 
    if not (isinstance(upper_bound, int) or isinstance(upper_bound, float)):
        print(f"type of upper_bound ist wrong")
        return
    a = np.random.normal(loc, scale, 100)
    a_new = a[a >= lower_bound]
    a_new_new = a_new[a_new <= upper_bound]
    mean = np.mean(a_new_new)
    std = np.std(a_new_new)
    return (mean, std)
if __name__ == "__main__":
    # use this for your own testing!

    pass
