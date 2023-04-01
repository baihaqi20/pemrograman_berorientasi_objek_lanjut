class Kendaraan:
    def __init__(self, jenis_kendaraan, bahan_bakar):
        self.jenis_kendaraan = jenis_kendaraan
        self.bahan_bakar = bahan_bakar

    def tampilkan_jenis_kendaraan(self):
        print(f"Jenis kendaraan ini adalah {self.jenis_kendaraan}")

    def tampilkan_bahan_bakar(self):
        print(f"Bahan bakar yang digunakan adalah {self.bahan_bakar}")

class RodaEmpat:
    def __init__(self, merk, tahun):
        self.merk = merk
        self.tahun = tahun

    def tampilkan_merk(self):
        print(f"Merk kendaraan ini adalah {self.merk}")

    def tampilkan_tahun(self):
        print(f"Tahun produksi kendaraan ini adalah {self.tahun}")

class Mobil(Kendaraan, RodaEmpat):
    def __init__(self, jenis_kendaraan, bahan_bakar, merk, tahun, warna):
        Kendaraan.__init__(self, jenis_kendaraan, bahan_bakar)
        RodaEmpat.__init__(self, merk, tahun)
        self.warna = warna

    def tampilkan_warna(self):
        print(f"Warna mobil ini adalah {self.warna}")

mobil = Mobil("SUV", "Bensin", "Toyota", 2022, "Hitam")
mobil.tampilkan_jenis_kendaraan()  # Output: Jenis kendaraan ini adalah SUV
mobil.tampilkan_bahan_bakar()  # Output: Bahan bakar yang digunakan adalah Bensin
mobil.tampilkan_merk()  # Output: Merk kendaraan ini adalah Toyota
mobil.tampilkan_tahun()  # Output: Tahun produksi kendaraan ini adalah 2022
mobil.tampilkan_warna()  # Output: Warna mobil ini adalah Hitam
