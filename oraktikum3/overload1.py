def hitung_luas_persegi(sisi):
    return sisi ** 2

def hitung_luas_persegi_panjang(panjang, lebar):
    return panjang * lebar
luas_persegi = hitung_luas_persegi(5)
luas_persegi_panjang = hitung_luas_persegi_panjang(3, 8)

print("Luas Persegi: ", luas_persegi) # output: Luas Persegi: 25
print("Luas Persegi Panjang: ", luas_persegi_panjang) # output: Luas Persegi Panjang: 24
