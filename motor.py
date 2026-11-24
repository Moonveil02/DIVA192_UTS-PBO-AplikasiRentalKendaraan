# SUBCLASS kedua: Motor adalah jenis dari Kendaraan (is-a).

from kendaraan import Kendaraan


class Motor(Kendaraan):
    # Constructor subclass: data umum dikirim ke superclass lewat super()
    def __init__(self, kode, merek, tarif_per_hari, kapasitas_cc, jenis):
        # Memanggil constructor induk
        super().__init__(kode, merek, tarif_per_hari)
        # Validasi atribut khusus Motor
        if kapasitas_cc <= 0:
            raise ValueError("Kapasitas mesin tidak valid")
        if jenis not in ("Matic", "Sport", "Bebek"):
            raise ValueError("Jenis harus Matic, Sport, atau Bebek")
        # Atribut private milik Motor
        self.__kapasitas_cc = kapasitas_cc
        self.__jenis = jenis

    # Getter atribut khusus
    def get_kapasitas_cc(self):
        return self.__kapasitas_cc

    def get_jenis(self):
        return self.__jenis

    # Method khusus Motor: informasi tambahan
    def info_khusus(self):
        return f"Motor | {self.__kapasitas_cc} cc | Jenis {self.__jenis}"