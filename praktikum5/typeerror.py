try:
    num = int(input("Masukkan angka: "))
    print("Angka yang dimasukkan adalah:", num)
except TypeError:
    print("Terjadi kesalahan tipe data! Mohon masukkan angka yang benar.")
