# SUPERCLASS: menyimpan data dan perilaku yang dimiliki SEMUA kendaraan.
# Mobil dan Motor akan mewarisi class ini (inheritance).

class Kendaraan:
    # Constructor berparameter: mengisi data awal saat object dibuat
    def __init__(self, kode, merek, tarif_per_hari):
        # Validasi nilai awal agar data tetap masuk akal
        if tarif_per_hari <= 0:
            raise ValueError("Tarif harus lebih dari 0")
        # Atribut PRIVATE (name mangling) -> tidak diubah langsung dari luar class
        self.__kode = kode
        self.__merek = merek
        self.__tarif_per_hari = tarif_per_hari
        self.__tersedia = True  # True = tersedia, False = sedang disewa

    # GETTER (membaca atribut private) 
    def get_kode(self):
        return self.__kode

    def get_merek(self):
        return self.__merek

    def get_tarif(self):
        return self.__tarif_per_hari

    def is_tersedia(self):
        return self.__tersedia

    # METHOD DENGAN VALIDASI (mengubah state) 
    # Mengubah tarif hanya boleh lewat method ini; tarif <= 0 ditolak
    def ubah_tarif(self, tarif_baru):
        if tarif_baru <= 0:
            return False
        self.__tarif_per_hari = tarif_baru
        return True

    # Menandai kendaraan sedang disewa; ditolak jika sudah disewa
    def sewa(self):
        if not self.__tersedia:
            return False
        self.__tersedia = False
        return True

    # Menandai kendaraan sudah dikembalikan; ditolak jika memang tersedia
    def kembalikan(self):
        if self.__tersedia:
            return False
        self.__tersedia = True
        return True

    # METHOD PERILAKU LAIN
    # Menghitung biaya sewa = tarif per hari x lama hari
    def hitung_biaya(self, lama_hari):
        return self.__tarif_per_hari * lama_hari

    # Mengembalikan teks status kendaraan
    def get_status(self):
        if self.__tersedia:
            return "Tersedia"
        return "Sedang Disewa"

    # Menampilkan data umum kendaraan
    def tampilkan_info(self):
        print("Kode  :", self.__kode)
        print("Merek :", self.__merek)
        print("Tarif :", self.__tarif_per_hari, "per hari")
        print("Status:", self.get_status())

    # Mengecek apakah kode kendaraan ini sama dengan kode yang dicari
    def punya_kode(self, kode):
        return self.__kode.lower() == kode.lower()

    # Mengecek apakah kata kunci cocok dengan kode atau merek kendaraan
    def cocok_dengan(self, kata):
        kata = kata.lower()
        return kata in self.__kode.lower() or kata in self.__merek.lower()

    # Menampilkan data umum + info khusus (info_khusus() ada di Mobil dan Motor)
    def tampilkan_lengkap(self):
        self.tampilkan_info()
        print("Jenis :", self.info_khusus())
        print("-" * 30)