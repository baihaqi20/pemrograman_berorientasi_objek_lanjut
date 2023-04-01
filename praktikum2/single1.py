class Kendaraan:
    def __init__(self, jenis, merek, tahun):
        self.jenis = jenis
        self.merek = merek
        self.tahun = tahun

    def info_kendaraan(self):
        print("Ini adalah kendaraan {} {} tahun {}".format(self.merek, self.jenis, self.tahun))

class Mobil(Kendaraan):
    def __init__(self, merek, tahun, warna):
        Kendaraan.__init__(self, "mobil", merek, tahun)
        self.warna = warna

    def info_mobil(self):
        print("Ini adalah mobil {} {} tahun {} dengan warna {}".format(self.merek, self.jenis, self.tahun, self.warna))

# Contoh Penggunaan
mobil1 = Mobil("Toyota", 2020, "Hitam")
mobil1.info_kendaraan()
mobil1.info_mobil()
