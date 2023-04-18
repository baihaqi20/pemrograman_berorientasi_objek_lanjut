data = {"nama": "John", "umur": 25, "alamat": "Jl. Sudirman"}

try:
    pekerjaan = data["pekerjaan"]
    print("Pekerjaan:", pekerjaan)
except KeyError:
    print("KeyError terjadi! Mohon periksa kembali key yang diminta.")
