# CLASS RELASI (Association): Penyewaan MEMILIKI satu Pelanggan dan satu Kendaraan.
# Ini hubungan has-a antarobjek, BUKAN inheritance.

class Penyewaan:
    # Constructor berparameter: menerima OBJECT Pelanggan dan OBJECT Kendaraan
    def __init__(self, kode_penyewaan, pelanggan, kendaraan, lama_hari):
        if lama_hari <= 0:
            raise ValueError("Lama sewa harus lebih dari 0 hari")
        # Atribut private
        self.__kode_penyewaan = kode_penyewaan
        self.__pelanggan = pelanggan      # relasi ke 1 Pelanggan
        self.__kendaraan = kendaraan      # relasi ke 1 Kendaraan
        self.__lama_hari = lama_hari
        self.__status = "Belum Dimulai"   # Belum Dimulai -> Berlangsung -> Selesai

    # ---------- GETTER ----------
    def get_kode(self):
        return self.__kode_penyewaan

    def get_pelanggan(self):
        return self.__pelanggan

    def get_kendaraan(self):
        return self.__kendaraan

    def get_lama_hari(self):
        return self.__lama_hari

    # Mengembalikan teks status penyewaan
    def cek_status(self):
        return self.__status

    # Total biaya dihitung lewat method milik Kendaraan (bukan akses atribut langsung)
    def get_total(self):
        return self.__kendaraan.hitung_biaya(self.__lama_hari)

    # Memulai sewa: kendaraan harus tersedia dan status masih "Belum Dimulai"
    def mulai(self):
        if self.__status != "Belum Dimulai":
            return False
        if not self.__kendaraan.sewa():  # ditolak jika kendaraan sedang disewa
            return False
        self.__status = "Berlangsung"
        return True

    # Mengakhiri sewa: hanya bisa jika sedang berlangsung
    def selesaikan(self):
        if self.__status != "Berlangsung":
            return False
        self.__kendaraan.kembalikan()
        self.__status = "Selesai"
        return True

    # Menampilkan rincian penyewaan
    def tampilkan_rincian(self):
        print("Kode Sewa :", self.__kode_penyewaan)
        print("Pelanggan :", self.__pelanggan.get_nama())
        print("Kendaraan :", self.__kendaraan.get_merek(),
              "(" + self.__kendaraan.get_kode() + ")")
        print("Lama Sewa :", self.__lama_hari, "hari")
        print("Total     :", self.get_total())
        print("Status    :", self.__status)

    # Mengecek apakah kode penyewaan ini sama dengan kode yang dicari
    def punya_kode(self, kode):
        return self.__kode_penyewaan.lower() == kode.lower()