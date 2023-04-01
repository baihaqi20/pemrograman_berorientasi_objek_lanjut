class Kendaraan:
    def __init__(self, nama):
        self.nama = nama

    def tampilkan_nama(self):
        print(f"Nama kendaraan ini adalah {self.nama}")

class Mobil(Kendaraan):
    def __init__(self, nama, jenis):
        super().__init__(nama)
        self.jenis = jenis

    def tampilkan_jenis(self):
        print(f"Jenis mobil ini adalah {self.jenis}")

class MobilSport(Mobil):
    def __init__(self, nama, jenis, kecepatan):
        super().__init__(nama, jenis)
        self.kecepatan = kecepatan

    def tampilkan_kecepatan(self):
        print(f"Kecepatan mobil sport ini adalah {self.kecepatan} km/h")

mobil_sport = MobilSport("Lamborghini", "Sport", 400)
mobil_sport.tampilkan_nama()  # Output: Nama kendaraan ini adalah Lamborghini
mobil_sport.tampilkan_jenis()  # Output: Jenis mobil ini adalah Sport
mobil_sport.tampilkan_kecepatan()  # Output: Kecepatan mobil sport ini adalah 400 km/h
