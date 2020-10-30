import numpy as np # berfungsi untuk melakukan kalkulasi data yang bertipe integer

tinggi = [1.73, 1.68, 1.71, 1.89, 1.79]
lebar = [65.4, 59.2, 63.6, 88.4, 68.7]

print("Numpy variable")
np_tinggi = np.array(tinggi)
print(np_tinggi)
np_lebar = np.array(lebar)
print(np_lebar)
print('\n')

print("2D Numpy Array variable")
numpy_array_2D = [
    [1.73, 1.68, 1.71, 1.89, 1.79],
    [65.4, 59.2, 63.6, 88.4, 68.7]
]
np_numpy_array_2D = np.array(numpy_array_2D)
print(np_numpy_array_2D)
print('\n')

print("Numpy data type")
print(type(np_numpy_array_2D))
print('\n')

print("Numpy data shape")
print(np_numpy_array_2D.shape)
print('\n')

print("Numpy data index")
print(np_numpy_array_2D[0])
print('\n')

print("Koordinate of data in matrix")
print(numpy_array_2D[0][2])
print(numpy_array_2D[1][4])
print('\n')

print("print value on the both position")
print(np_numpy_array_2D[:,1:3])
print('\n')

print("print the value on every each line")
print(np_numpy_array_2D[0,:])
print(np_numpy_array_2D[1,:])
