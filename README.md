Company Profile Website - Django & SQLite

Website profil perusahaan yang dibangun menggunakan Django 5.2 dan Tailwind CSS. Proyek ini dirancang agar mudah dikelola melalui halaman Admin Django dan menggunakan SQLite sebagai database untuk kemudahan portabilitas.

Fitur Utama

Halaman Dinamis: Produk, Artikel, dan Galeri yang bisa dikelola penuh via Admin.

Profil Perusahaan Singleton: Pengaturan visi, misi, dan sejarah yang terpusat.

Responsive Design: Tampilan modern menggunakan Tailwind CSS.

Admin Panel: Sistem manajemen konten yang instan dan aman.

Cara Menjalankan Proyek

Ikuti langkah-langkah di bawah ini untuk menjalankan proyek di perangkat lokal Anda:

1. Download (Clone) Proyek

Buka terminal dan clone repository Anda:

git clone <URL_REPO_GITHUB_ANDA>
cd company-profile


2. Buat Virtual Environment

Gunakan virtual environment agar library proyek ini terisolasi dan tidak bentrok dengan proyek lain.

# Membuat environment
python -m venv venv

# Mengaktifkan environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate


3. Install Dependensi

Pastikan Anda sudah berada di dalam virtual environment, lalu instal library yang dibutuhkan:

pip install -r requirements.txt


Catatan: Library utama yang diinstal termasuk Django dan Pillow (untuk pengolahan gambar).

4. Jalankan Migrasi Database

Buat struktur database SQLite lokal Anda:

python manage.py migrate


5. Buat Akun Admin (Superuser)

Anda bisa membuat akun admin secara manual atau menggunakan script otomatis yang sudah disediakan:

Opsi A (Manual):

python manage.py createsuperuser


Opsi B (Otomatis):
Gunakan script create_superuser.py untuk membuat admin dengan cepat:

python create_superuser.py


Kredensial Default Opsi B: Username: admin | Password: admin123

6. Jalankan Server Development

Langkah terakhir, nyalakan servernya:

python manage.py runserver


Buka browser Anda dan akses:

Website: http://127.0.0.1:8000

Halaman Admin: http://127.0.0.1:8000/admin

Struktur Folder Penting

/core: Berisi logika utama (Models, Views, URLs).

/templates: Folder untuk file HTML (Base template & Page templates).

/static: File aset statis (CSS/JS).

/media: Tempat penyimpanan gambar yang di-upload via Admin.

Catatan Tambahan

Pastikan folder media/ tersedia jika Anda ingin meng-upload gambar produk atau artikel.

Tailwind CSS dipanggil via CDN di base.html, sehingga memerlukan koneksi internet untuk memuat styling dengan sempurna saat pengembangan.

Dibuat untuk Tugas Project Company Profile.
