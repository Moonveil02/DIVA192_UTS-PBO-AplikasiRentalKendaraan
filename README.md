# Aplikasi Rental Kendaraan

## Identitas Mahasiswa

- **Nama:** Diva Nasyifah Nurazizah
- **NIM:** 25552011192
- **Kelas:** TIF RP 25B
- **Mata Kuliah:** Pemrograman Berorientasi Objek I
- **Dosen Pengampu:** Gia Yuliana, S.Kom., M.Kom.

---

## 1. Deskripsi Aplikasi

Aplikasi Rental Kendaraan merupakan aplikasi berbasis Python yang dibuat untuk memenuhi tugas Ujian Tengah Semester (UTS) mata kuliah Pemrograman Berorientasi Objek (PBO).

Aplikasi ini digunakan untuk mengelola data kendaraan (mobil dan motor), data pelanggan, serta transaksi penyewaan kendaraan melalui Command Line Interface (CLI).

## 2. Fitur Aplikasi

- Menambahkan data kendaraan (mobil dan motor).
- Menampilkan daftar kendaraan.
- Mencari data kendaraan berdasarkan kode atau merek.
- Mengubah tarif sewa kendaraan.
- Memeriksa status kendaraan (tersedia atau sedang disewa).
- Menambahkan data pelanggan.
- Menampilkan dan mencari data pelanggan.
- Mengubah email pelanggan.
- Membuat transaksi penyewaan kendaraan.
- Menghitung total biaya sewa.
- Menampilkan daftar penyewaan.
- Memeriksa status penyewaan.
- Mengembalikan kendaraan dan menyelesaikan penyewaan.

## 3. Penerapan Konsep Pemrograman Berorientasi Objek (PBO)

**a. Class dan Object**
Digunakan untuk membuat objek Kendaraan, Mobil, Motor, Pelanggan, dan Penyewaan.

**b. Constructor**
Digunakan untuk menginisialisasi atribut setiap objek.

**c. Encapsulation**
Menggunakan atribut private dan getter untuk mengakses data objek. Perubahan data dilakukan melalui method yang melakukan validasi, misalnya `ubah_tarif()` dan `ubah_email()`.

**d. Inheritance**
Class Mobil dan Motor merupakan turunan dari class Kendaraan.

**e. Association**
Class Penyewaan berhubungan dengan satu objek Pelanggan dan satu objek Kendaraan.

## 4. Struktur File Program

- `main.py` : Program utama dan menu interaktif.
- `kendaraan.py` : Superclass Kendaraan.
- `mobil.py` : Subclass Mobil.
- `motor.py` : Subclass Motor.
- `pelanggan.py` : Class Pelanggan.
- `penyewaan.py` : Class Penyewaan (relasi antara Pelanggan dan Kendaraan).

## 5. Bahasa Pemrograman

Python 3

## 6. Cara Menjalankan Program

1. Buka folder aplikasi di Visual Studio Code.
2. Buka Terminal.
3. Jalankan perintah berikut:

```
python main.py
```
