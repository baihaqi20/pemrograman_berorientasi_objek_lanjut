try:
    num1 = int(input("Masukkan angka pertama: "))
    num2 = int(input("Masukkan angka kedua: "))
    hasil = num1 / num2
    print("Hasil pembagian adalah:", hasil)
except ZeroDivisionError:
    print("Terjadi pembagian dengan angka nol! Mohon masukkan angka yang tidak nol.")
