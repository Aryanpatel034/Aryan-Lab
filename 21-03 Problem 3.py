import numpy as np

def create_array(dim1, dim2, dim3, initial_value):

    return np.full((dim1, dim2, dim3), initial_value)

dim1, dim2, dim3 = 3, 4, 5
initial_value = 9
array = create_array(dim1, dim2, dim3, initial_value)

print(array)
