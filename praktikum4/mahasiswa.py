class Mahasiswa:
    def __init__(self, nama, npm):
        self.nama = nama
        self.npm = npm
        self.kelompok_kkm = KelompokKKM()

    def join_kelompok(self, kelompok):
        self.kelompok_kkm.add_anggota(self, kelompok)

    def leave_kelompok(self):
        self.kelompok_kkm.remove_anggota(self)

class KelompokKKM:
    def __init__(self):
        self.anggota = {}

    def add_anggota(self, mahasiswa, kelompok):
        self.anggota[mahasiswa.npm] = (mahasiswa.nama, kelompok)
        print(f"{mahasiswa.nama} dengan NPM {mahasiswa.npm} bergabung ke kelompok {kelompok}.")

    def remove_anggota(self, mahasiswa):
        del self.anggota[mahasiswa.npm]
        print(f"{mahasiswa.nama} dengan NPM {mahasiswa.npm} keluar dari kelompok.")

    def print_anggota(self):
        for npm, data in self.anggota.items():
            print(f"{data[0]} dengan NPM {npm} dari kelompok {data[1]}")
# membuat objek Mahasiswa
mhs1 = Mahasiswa("Agus", "18001001")
mhs2 = Mahasiswa("Budi", "18001002")

# membuat objek KelompokKKM
kelompok1 = "A"
kelompok2 = "B"
kkm = KelompokKKM()

# mahasiswa bergabung ke kelompok KKM
mhs1.join_kelompok(kelompok1)
mhs2.join_kelompok(kelompok2)

# mencetak anggota pada kelompok KKM
kkm.print_anggota()

# mahasiswa keluar dari kelompok KKM
mhs1.leave_kelompok()

# mencetak anggota pada kelompok KKM setelah mahasiswa keluar
kkm.print_anggota()

