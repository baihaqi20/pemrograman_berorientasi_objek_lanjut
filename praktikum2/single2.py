class Hewan:
    def __init__(self, jenis, makanan):
        self.jenis = jenis
        self.makanan = makanan

    def info_hewan(self):
        print("Ini adalah hewan {} yang makan {}".format(self.jenis, self.makanan))

class Kucing(Hewan):
    def __init__(self, nama, umur, ras, makanan):
        Hewan.__init__(self, "kucing", makanan)
        self.nama = nama
        self.umur = umur
        self.ras = ras

    def info_kucing(self):
        print("Ini adalah kucing bernama {} dengan umur {} tahun, ras {}, dan makanan {}".format(self.nama, self.umur, self.ras, self.makanan))

# Contoh Penggunaan
kucing1 = Kucing("Tom", 2, "Persia", "Ikan")
kucing1.info_hewan()
kucing1.info_kucing()
