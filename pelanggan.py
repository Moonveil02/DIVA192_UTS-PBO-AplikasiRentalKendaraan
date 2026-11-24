# Class Pelanggan: data penyewa kendaraan.

class Pelanggan:
    # Constructor berparameter
    def __init__(self, kode_pelanggan, nama, email):
        # Atribut private
        self.__kode_pelanggan = kode_pelanggan
        self.__nama = nama
        self.__email = ""
        # Email awal divalidasi lewat ubah_email(); jika gagal -> error
        if not self.ubah_email(email):
            raise ValueError("Email tidak valid")

    # ---------- GETTER ----------
    def get_kode(self):
        return self.__kode_pelanggan

    def get_nama(self):
        return self.__nama

    def get_email(self):
        return self.__email

    # Mengubah email dengan validasi sederhana ("@" dan ".")
    # Jika gagal, email lama tetap dan method mengembalikan False
    def ubah_email(self, email_baru):
        if "@" not in email_baru or "." not in email_baru:
            return False
        self.__email = email_baru
        return True

    # Menampilkan data pelanggan
    def tampilkan_info(self):
        print("Kode  :", self.__kode_pelanggan)
        print("Nama  :", self.__nama)
        print("Email :", self.__email)

    # Mengecek apakah kode pelanggan ini sama dengan kode yang dicari
    def punya_kode(self, kode):
        return self.__kode_pelanggan.lower() == kode.lower()

    # Mengecek apakah kata kunci cocok dengan kode atau nama pelanggan
    def cocok_dengan(self, kata):
        kata = kata.lower()
        return kata in self.__kode_pelanggan.lower() or kata in self.__nama.lower()