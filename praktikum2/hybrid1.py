class Hewan:
    def __init__(self, nama):
        self.nama = nama

    def tampilkan_nama(self):
        print(f"Nama hewan ini adalah {self.nama}")

class Kucing(Hewan):
    def __init__(self, nama, umur):
        super().__init__(nama)
        self.umur = umur

    def tampilkan_umur(self):
        print(f"Umur kucing ini adalah {self.umur} tahun")

class HewanPeliharaan:
    def __init__(self, pemilik):
        self.pemilik = pemilik

    def tampilkan_pemilik(self):
        print(f"Hewan peliharaan ini memiliki pemilik {self.pemilik}")

class KucingPeliharaan(Kucing, HewanPeliharaan):
    def __init__(self, nama, umur, pemilik):
        Kucing.__init__(self, nama, umur)
        HewanPeliharaan.__init__(self, pemilik)

    def tampilkan_info(self):
        self.tampilkan_nama()
        self.tampilkan_umur()
        self.tampilkan_pemilik()

kucing_peliharaan = KucingPeliharaan("Kitty", 2, "John")
kucing_peliharaan.tampilkan_info()  # Output: Nama hewan ini adalah Kitty, Umur kucing ini adalah 2 tahun, Hewan peliharaan ini memiliki pemilik John
