""" # import numpy
import numpy as np # used alias

numpyarr = np.array([1, 2, 3])
print(numpyarr) """

import numpy

keluarga = ["Irin", 21, "Ria", 18, "sega", 24, "Irin", 21, "Ria", 18, "Sega", 24]

tam_kel = keluarga + ["abi", 4.78]

print(str(len(tam_kel)) + " elemen didalam list tam_kel") # diubah bertipe string agar bisa diconcat dengan string lainya

np_kel = numpy.array(tam_kel)