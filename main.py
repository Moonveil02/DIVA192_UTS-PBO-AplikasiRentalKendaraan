# Program utama: aplikasi CLI Rental Kendaraan.
# Tugas file ini: import class, membuat object, dan menampilkan menu teks.

from mobil import Mobil
from motor import Motor
from pelanggan import Pelanggan
from penyewaan import Penyewaan

# PENYIMPANAN DATA (disimpan di list selama program berjalan)
daftar_kendaraan = []
daftar_pelanggan = []
daftar_penyewaan = []

# DATA AWAL (contoh agar program mudah dicoba)
daftar_kendaraan.append(Mobil("KL001", "Toyota Fortuner", 950000, 5, "Manual"))
daftar_kendaraan.append(Motor("KR002", "Ducati Panigale V4", 1200000, 1.103 , "Sport"))
daftar_pelanggan.append(Pelanggan("PL001", "Kastara Raizen", "astaraizen@gmail.com"))

# FUNGSI PENDUKUNG 
# Membaca angka bulat positif dari keyboard; mengulang sampai input valid
def baca_angka(pesan):
    while True:
        teks = input(pesan).strip()
        if teks.isdigit() and int(teks) > 0:
            return int(teks)
        print("Input harus berupa angka lebih dari 0.")


# Mencari kendaraan berdasarkan kode (return object atau None)
def cari_kendaraan_by_kode(kode):
    for k in daftar_kendaraan:
        if k.punya_kode(kode):
            return k
    return None

# Mencari pelanggan berdasarkan kode (return object atau None)
def cari_pelanggan_by_kode(kode):
    for p in daftar_pelanggan:
        if p.punya_kode(kode):
            return p
    return None

# Mencari penyewaan berdasarkan kode (return object atau None)
def cari_penyewaan_by_kode(kode):
    for s in daftar_penyewaan:
        if s.punya_kode(kode):
            return s
    return None

# 1. TAMBAH DATA
def tambah_kendaraan():
    print("\n-- Tambah Kendaraan --")
    jenis = input("Jenis (1 = Mobil, 2 = Motor): ").strip()
    if jenis not in ("1", "2"):
        print("Pilihan tidak valid.")
        return
    kode = input("Kode kendaraan: ").strip()
    if kode == "" or cari_kendaraan_by_kode(kode) is not None:
        print("Kode kosong atau sudah dipakai.")
        return
    merek = input("Merek: ").strip()
    tarif = baca_angka("Tarif per hari: ")
    # try-except hanya dipakai untuk menangkap ValueError dari constructor
    try:
        if jenis == "1":
            pintu = baca_angka("Jumlah pintu: ")
            transmisi = input("Transmisi (Manual/Otomatis): ").strip().capitalize()
            kendaraan = Mobil(kode, merek, tarif, pintu, transmisi)
        else:
            cc = baca_angka("Kapasitas mesin (cc): ")
            jenis_motor = input("Jenis (Matic/Sport/Bebek): ").strip().capitalize()
            kendaraan = Motor(kode, merek, tarif, cc, jenis_motor)
    except ValueError as e:
        print("Gagal menambah kendaraan:", e)
        return
    daftar_kendaraan.append(kendaraan)
    print("Kendaraan berhasil ditambahkan.")


def tambah_pelanggan():
    print("\n-- Tambah Pelanggan --")
    kode = input("Kode pelanggan: ").strip()
    if kode == "" or cari_pelanggan_by_kode(kode) is not None:
        print("Kode kosong atau sudah dipakai.")
        return
    nama = input("Nama: ").strip()
    email = input("Email: ").strip()
    try:
        pelanggan = Pelanggan(kode, nama, email)
    except ValueError as e:
        print("Gagal menambah pelanggan:", e)
        return
    daftar_pelanggan.append(pelanggan)
    print("Pelanggan berhasil ditambahkan.")


def tambah_penyewaan():
    print("\n-- Tambah Penyewaan --")
    kode = input("Kode penyewaan: ").strip()
    if kode == "" or cari_penyewaan_by_kode(kode) is not None:
        print("Kode kosong atau sudah dipakai.")
        return
    pelanggan = cari_pelanggan_by_kode(input("Kode pelanggan: ").strip())
    if pelanggan is None:
        print("Pelanggan tidak ditemukan.")
        return
    kendaraan = cari_kendaraan_by_kode(input("Kode kendaraan: ").strip())
    if kendaraan is None:
        print("Kendaraan tidak ditemukan.")
        return
    lama = baca_angka("Lama sewa (hari): ")
    # Membuat object relasi: Penyewaan memegang 1 Pelanggan + 1 Kendaraan
    sewa = Penyewaan(kode, pelanggan, kendaraan, lama)
    # mulai() menolak jika kendaraan sedang disewa
    if not sewa.mulai():
        print("Gagal: kendaraan sedang disewa.")
        return
    daftar_penyewaan.append(sewa)
    print("Penyewaan berhasil dimulai.")
    sewa.tampilkan_rincian()


def menu_tambah():
    print("\n1. Tambah kendaraan\n2. Tambah pelanggan\n3. Tambah penyewaan")
    pilih = input("Pilih: ").strip()
    if pilih == "1":
        tambah_kendaraan()
    elif pilih == "2":
        tambah_pelanggan()
    elif pilih == "3":
        tambah_penyewaan()
    else:
        print("Pilihan tidak valid.")


# 2. TAMPILKAN DATA
def menu_tampilkan():
    print("\n1. Tampilkan kendaraan\n2. Tampilkan pelanggan\n3. Tampilkan penyewaan")
    pilih = input("Pilih: ").strip()
    print()
    if pilih == "1":
        if not daftar_kendaraan:
            print("Belum ada data kendaraan.")
        for k in daftar_kendaraan:
            k.tampilkan_lengkap()
    elif pilih == "2":
        if not daftar_pelanggan:
            print("Belum ada data pelanggan.")
        for p in daftar_pelanggan:
            p.tampilkan_info()
            print("-" * 30)
    elif pilih == "3":
        if not daftar_penyewaan:
            print("Belum ada data penyewaan.")
        for s in daftar_penyewaan:
            s.tampilkan_rincian()
            print("-" * 30)
    else:
        print("Pilihan tidak valid.")


# 3. CARI DATA
def menu_cari():
    print("\n1. Cari kendaraan (kode/merek)\n2. Cari pelanggan (kode/nama)")
    pilih = input("Pilih: ").strip()
    if pilih not in ("1", "2"):
        print("Pilihan tidak valid.")
        return
    kata = input("Kata kunci: ").strip()
    ditemukan = False
    print()
    if pilih == "1":
        for k in daftar_kendaraan:
            if k.cocok_dengan(kata):
                k.tampilkan_lengkap()
                ditemukan = True
    else:
        for p in daftar_pelanggan:
            if p.cocok_dengan(kata):
                p.tampilkan_info()
                print("-" * 30)
                ditemukan = True
    if not ditemukan:
        print("Data tidak ditemukan.")


# 4. UBAH DATA
def menu_ubah():
    print("\n1. Ubah tarif kendaraan\n2. Ubah email pelanggan")
    pilih = input("Pilih: ").strip()
    if pilih == "1":
        kendaraan = cari_kendaraan_by_kode(input("Kode kendaraan: ").strip())
        if kendaraan is None:
            print("Kendaraan tidak ditemukan.")
            return
        tarif = baca_angka("Tarif baru: ")
        # Perubahan hanya lewat method yang memvalidasi
        if kendaraan.ubah_tarif(tarif):
            print("Tarif berhasil diubah menjadi", kendaraan.get_tarif())
        else:
            print("Tarif ditolak.")
    elif pilih == "2":
        pelanggan = cari_pelanggan_by_kode(input("Kode pelanggan: ").strip())
        if pelanggan is None:
            print("Pelanggan tidak ditemukan.")
            return
        email = input("Email baru: ").strip()
        if pelanggan.ubah_email(email):
            print("Email berhasil diubah menjadi", pelanggan.get_email())
        else:
            print("Email tidak valid, email lama tetap:", pelanggan.get_email())
    else:
        print("Pilihan tidak valid.")


# 5. CEK STATUS DATA 
def menu_status():
    print("\n1. Cek status kendaraan\n2. Cek status penyewaan")
    pilih = input("Pilih: ").strip()
    if pilih == "1":
        kendaraan = cari_kendaraan_by_kode(input("Kode kendaraan: ").strip())
        if kendaraan is None:
            print("Kendaraan tidak ditemukan.")
        else:
            print(kendaraan.get_merek(), "->", kendaraan.get_status())
    elif pilih == "2":
        sewa = cari_penyewaan_by_kode(input("Kode penyewaan: ").strip())
        if sewa is None:
            print("Penyewaan tidak ditemukan.")
        else:
            print("Penyewaan", sewa.get_kode(), "->", sewa.cek_status())
    else:
        print("Pilihan tidak valid.")


# 6. KEMBALIKAN KENDARAAN (menyelesaikan penyewaan)
def kembalikan_kendaraan():
    sewa = cari_penyewaan_by_kode(input("Kode penyewaan: ").strip())
    if sewa is None:
        print("Penyewaan tidak ditemukan.")
    elif sewa.selesaikan():
        print("Kendaraan dikembalikan. Total bayar:", sewa.get_total())
    else:
        print("Gagal: penyewaan tidak sedang berlangsung.")


# MENU UTAMA 
def main():
    while True:
        print("\n===== RENTAL KENDARAAN =====")
        print("1. Tambah data")
        print("2. Tampilkan data")
        print("3. Cari data")
        print("4. Ubah data")
        print("5. Cek status data")
        print("6. Kembalikan kendaraan")
        print("7. Keluar")
        pilih = input("Pilih menu: ").strip()
        if pilih == "1":
            menu_tambah()
        elif pilih == "2":
            menu_tampilkan()
        elif pilih == "3":
            menu_cari()
        elif pilih == "4":
            menu_ubah()
        elif pilih == "5":
            menu_status()
        elif pilih == "6":
            kembalikan_kendaraan()
        elif pilih == "7":
            print("Terima kasih. Program selesai.")
            break
        else:
            print("Menu tidak valid.")


# Program dijalankan hanya jika file ini dieksekusi langsung
if __name__ == "__main__":
    main()