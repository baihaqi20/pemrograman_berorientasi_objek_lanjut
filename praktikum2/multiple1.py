class Bentuk:
    def __init__(self, jenis_bentuk):
        self.jenis_bentuk = jenis_bentuk

    def cetak_jenis_bentuk(self):
        print(f"Ini adalah bentuk {self.jenis_bentuk}")

class Warna:
    def __init__(self, warna):
        self.warna = warna

    def cetak_warna(self):
        print(f"Warna dari bentuk ini adalah {self.warna}")

class BentukWarna(Bentuk, Warna):
    def __init__(self, jenis_bentuk, warna):
        Bentuk.__init__(self, jenis_bentuk)
        Warna.__init__(self, warna)

    def tampil(self):
        self.cetak_jenis_bentuk()
        self.cetak_warna()

bentuk_warna = BentukWarna("Lingkaran", "Merah")
bentuk_warna.tampil()  # Output: Ini adalah bentuk Lingkaran, Warna dari bentuk ini adalah Merah
