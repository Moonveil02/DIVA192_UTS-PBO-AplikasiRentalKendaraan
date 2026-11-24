# SUBCLASS pertama: Mobil adalah jenis dari Kendaraan (is-a).

from kendaraan import Kendaraan


class Mobil(Kendaraan):
    # Constructor subclass: data umum dikirim ke superclass lewat super()
    def __init__(self, kode, merek, tarif_per_hari, jumlah_pintu, transmisi):
        # Memanggil constructor induk (validasi tarif ikut berjalan)
        super().__init__(kode, merek, tarif_per_hari)
        # Validasi atribut khusus Mobil
        if jumlah_pintu <= 0:
            raise ValueError("Jumlah pintu tidak valid")
        if transmisi not in ("Manual", "Otomatis"):
            raise ValueError("Transmisi harus Manual atau Otomatis")
        # Atribut private milik Mobil
        self.__jumlah_pintu = jumlah_pintu
        self.__transmisi = transmisi

    # Getter atribut khusus
    def get_jumlah_pintu(self):
        return self.__jumlah_pintu

    def get_transmisi(self):
        return self.__transmisi

    # Method khusus Mobil: informasi tambahan
    def info_khusus(self):
        return f"Mobil | {self.__jumlah_pintu} pintu | Transmisi {self.__transmisi}"