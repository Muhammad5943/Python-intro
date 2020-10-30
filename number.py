import numpy as np

# fungsi numpy

tinggi = [1.73, 1.68, 1.71, 1.89, 1.79]
lebar = [65.4, 59.2, 63.6, 88.4, 68.7]

np_lebar = np.array(lebar)
print(np_lebar)
np_tinggi = np.array(tinggi)
print(np_tinggi)

hasil = np_lebar / np_tinggi ** 2
print(hasil) 


python_list = [1, 2, 3]
numpy_list = np.array([1, 2, 3])

tambah_list = python_list + python_list
print(tambah_list) # akan bergabung seperti string + string

tambah_numpy = numpy_list + numpy_list
print(tambah_numpy)

print(hasil > 23)
print(hasil[hasil > 23])