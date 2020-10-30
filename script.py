# Variables & Types
""" panjang = 50
lebar = 5

hasil = panjang * lebar / 2

print(hasil)

print(type(hasil)) """

# List
""" 
warna = ["merah", 5.5, "kuning", True, "hitam"]

print(warna)

kel_variable = [["merah", 5.5], ["kuning", True], ["hitam", 4.6]]

print(kel_variable)
print(kel_variable[0])
print(kel_variable[1])
print(kel_variable[2]) 
"""

# Subsetting list
""" 
keluarga = ["Irin", 21, "Ria", 18, "Sega", 24]
print(keluarga)
print(keluarga[2])
print(keluarga[-1])
print(keluarga[3:5])
print(keluarga[:5])
print(keluarga[3:])
"""

#  List manipulation
""" 
keluarga = ["Irin", 21, "Ria", 18, "Sega", 24]
print(keluarga)

keluarga[5] = 100
print(keluarga)

tambah_kel = keluarga + ["gery", 30]
print(tambah_kel)

keluarga[:2] = ["Khsirin", 23]
print(keluarga)

del(keluarga[2:5])
print(keluarga)
print(keluarga)

del(keluarga[0])
print(keluarga)
print(keluarga) 
"""

# Function
""" 
angka = [5.22, 7.89, 6.45, 5.02, 4.15]
print(angka)

max_nilai = max(angka)
print(max_nilai)

min_nilai = min(angka)
print(min_nilai)

pembulatan = round(angka[2])
print(pembulatan)

pembulatan = round(angka[1])
print(pembulatan)

pembulatan = round(angka[1], 1)
print(pembulatan) 
"""

# Method
keluarga = ["Irin", 21, "Ria", 18, "sega", 24, "Irin", 21, "Ria", 18, "Sega", 24]
print(keluarga)

""" keluarga = keluarga.index("Ria")
print(keluarga) """

""" type = type(keluarga)
print(type) """

""" keluarga = keluarga.count(24)
print(keluarga) """

""" keluarga[2] = "farah"
keluarga = keluarga[2].upper()
print(keluarga)
keluarga = keluarga[2].isupper()
print(keluarga) """

""" keluarga = keluarga[0].replace("Ir", "Ra")
print(keluarga) """

keluarga.append("abi")
print(keluarga)

keluarga.append(50)
print(keluarga)

type_kel = type(keluarga)
print(type_kel)