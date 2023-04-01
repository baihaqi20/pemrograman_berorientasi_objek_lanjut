class Hewan:
    def __init__(self, jenis):
        self.jenis = jenis

    def tampilkan_jenis(self):
        print(f"Jenis hewan ini adalah {self.jenis}")

class Mammalia(Hewan):
    def __init__(self, jenis, ukuran):
        super().__init__(jenis)
        self.ukuran = ukuran

    def tampilkan_ukuran(self):
        print(f"Ukuran hewan mammalia ini adalah {self.ukuran}")

class Anjing(Mammalia):
    def __init__(self, jenis, ukuran, ras):
        super().__init__(jenis, ukuran)
        self.ras = ras

    def tampilkan_ras(self):
        print(f"Ras anjing ini adalah {self.ras}")

class AnjingPintar(Anjing):
    def __init__(self, jenis, ukuran, ras, kemampuan):
        super().__init__(jenis, ukuran, ras)
        self.kemampuan = kemampuan

    def tampilkan_kemampuan(self):
        print(f"Kemampuan anjing pintar ini adalah {self.kemampuan}")

class AnjingPelacak(Anjing):
    def __init__(self, jenis, ukuran, ras, kecepatan):
        super().__init__(jenis, ukuran, ras)
        self.kecepatan = kecepatan

    def tampilkan_kecepatan(self):
        print(f"Kecepatan anjing pelacak ini adalah {self.kecepatan}")

anjing_pintar = AnjingPintar("Anjing", "Sedang", "Golden Retriever", "Bisa bermain piano")
anjing_pintar.tampilkan_jenis()  # Output: Jenis hewan ini adalah Anjing
anjing_pintar.tampilkan_ukuran()  # Output: Ukuran hewan mammalia ini adalah Sedang
anjing_pintar.tampilkan_ras()  # Output: Ras anjing ini adalah Golden Retriever
anjing_pintar.tampilkan_kemampuan()  # Output: Kemampuan anjing pintar ini adalah Bisa bermain piano

anjing_pelacak = AnjingPelacak("Anjing", "Besar", "Bloodhound", "60 km/h")
anjing_pelacak.tampilkan_jenis()  # Output: Jenis hewan ini adalah Anjing
anjing_pelacak.tampilkan_ukuran()  # Output: Ukuran hewan mammalia ini adalah Besar
anjing_pelacak.tampilkan_ras()  # Output: Ras anjing ini adalah Bloodhound
anjing_pelacak.tampilkan_kecepatan()  # Output: Kecepatan anjing pelacak ini adalah 60 km/h
