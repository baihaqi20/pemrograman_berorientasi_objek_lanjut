data = ["aldo", "nurhadi", 25, "Jl. Sudirman"]

try:
    alamat = data[4]
    print("Alamat:", alamat)
except IndexError:
    print("IndexError terjadi! Mohon periksa kembali index yang diminta.")
