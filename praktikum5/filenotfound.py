try:
    file = open("data.txt", "r")
    print(file.read())
    file.close()
except FileNotFoundError:
    print("File tidak ditemukan! Mohon periksa kembali nama file atau direktori penyimpanannya.")
