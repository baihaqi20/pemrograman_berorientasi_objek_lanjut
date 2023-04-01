class Binatang:
    def __init__(self, jenis):
        self.jenis = jenis

    def tampilkan_jenis(self):
        print(f"Jenis binatang ini adalah {self.jenis}")

class Kucing(Binatang):
    def __init__(self, nama, jenis):
        super().__init__(jenis)
        self.nama = nama

    def tampilkan_nama(self):
        print(f"Nama kucing ini adalah {self.nama}")

class Anjing(Binatang):
    def __init__(self, nama, jenis):
        super().__init__(jenis)
        self.nama = nama

    def tampilkan_nama(self):
        print(f"Nama anjing ini adalah {self.nama}")

kucing = Kucing("Tom", "Persia")
kucing.tampilkan_nama()  # Output: Nama kucing ini adalah Tom
kucing.tampilkan_jenis()  # Output: Jenis binatang ini adalah Persia

anjing = Anjing("Snoopy", "Bulldog")
anjing.tampilkan_nama()  # Output: Nama anjing ini adalah Snoopy
anjing.tampilkan_jenis()  # Output: Jenis binatang ini adalah Bulldog
