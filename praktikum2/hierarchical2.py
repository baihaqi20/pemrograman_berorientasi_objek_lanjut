class Bentuk:
    def __init__(self, nama):
        self.nama = nama

    def tampilkan_nama(self):
        print(f"Nama bentuk ini adalah {self.nama}")

class Persegi(Bentuk):
    def __init__(self, sisi):
        super().__init__("Persegi")
        self.sisi = sisi

    def tampilkan_luas(self):
        print(f"Luas persegi ini adalah {self.sisi**2}")

class Segitiga(Bentuk):
    def __init__(self, alas, tinggi):
        super().__init__("Segitiga")
        self.alas = alas
        self.tinggi = tinggi

    def tampilkan_luas(self):
        print(f"Luas segitiga ini adalah {(self.alas*self.tinggi)/2}")

persegi = Persegi(5)
persegi.tampilkan_nama()  # Output: Nama bentuk ini adalah Persegi
persegi.tampilkan_luas()  # Output: Luas persegi ini adalah 25

segitiga = Segitiga(4, 3)
segitiga.tampilkan_nama()  # Output: Nama bentuk ini adalah Segitiga
segitiga.tampilkan_luas()  # Output: Luas segitiga ini adalah 6.0
