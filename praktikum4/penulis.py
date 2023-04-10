class Penulis:
    def __init__(self, nama):
        self.nama = nama
        self.buku = []

    def tulis_buku(self, judul, tahun):
        buku = Buku(judul, tahun)
        self.buku.append(buku)

class Buku:
    def __init__(self, judul, tahun):
        self.judul = judul
        self.tahun = tahun

    def __str__(self):
        return f"{self.judul} ({self.tahun})"

class Perpustakaan:
    def __init__(self):
        self.koleksi_buku = []

    def tambah_buku(self, buku):
        self.koleksi_buku.append(buku)

    def cari_buku(self, judul):
        for buku in self.koleksi_buku:
            if buku.judul.lower() == judul.lower():
                return buku
        return None

# membuat objek Penulis
penulis1 = Penulis("Agus")

# penulis menulis buku
penulis1.tulis_buku("Pemrograman Python", 2021)
penulis1.tulis_buku("Data Science", 2022)

# membuat objek Perpustakaan
perpustakaan = Perpustakaan()

# menambahkan buku ke dalam perpustakaan
for buku in penulis1.buku:
    perpustakaan.tambah_buku(buku)

# mencari buku di perpustakaan
cari_buku = perpustakaan.cari_buku("Data Science")
if cari_buku:
    print(f"Buku {cari_buku} ditemukan di perpustakaan.")
else:
    print("Buku tidak ditemukan di perpustakaan.")
