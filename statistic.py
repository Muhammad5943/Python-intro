import numpy as np

print("Matrix kota")
np_kota = np.array([[1.64,71.78],[1.37,63.35],[1.6,55.09],[2.04,74.85],[2.01,73.57]])
print(np_kota)

print("mean matrix kota")
print(np.mean(np_kota[:,0]))
print("median matrix kota")
print(np.median(np_kota[:,0]))
print("deviation standard matrix kota")
print(np.std(np_kota[:,0]))
print("corelation coefficient matrix kota")
print(np.corrcoef(np_kota[:,0], np_kota[:,0]))