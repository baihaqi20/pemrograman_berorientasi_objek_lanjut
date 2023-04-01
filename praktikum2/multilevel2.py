class Manusia:
    def __init__(self, nama):
        self.nama = nama

    def tampilkan_nama(self):
        print(f"Nama manusia ini adalah {self.nama}")

class Pekerja(Manusia):
    def __init__(self, nama, jabatan):
        super().__init__(nama)
        self.jabatan = jabatan

    def tampilkan_jabatan(self):
        print(f"Jabatan pekerja ini adalah {self.jabatan}")

class Programmer(Pekerja):
    def __init__(self, nama, jabatan, bahasa):
        super().__init__(nama, jabatan)
        self.bahasa = bahasa

    def tampilkan_bahasa(self):
        print(f"Bahasa pemrograman yang dikuasai oleh programmer ini adalah {self.bahasa}")

programmer = Programmer("John", "Programmer", "Python")
programmer.tampilkan_nama()  # Output: Nama manusia ini adalah John
programmer.tampilkan_jabatan()  # Output: Jabatan pekerja ini adalah Programmer
programmer.tampilkan_bahasa()  # Output: Bahasa pemrograman yang dikuasai oleh programmer ini adalah Python
