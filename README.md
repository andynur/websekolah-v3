# WebSekolah

Aplikasi web sederhana untuk manajemen data siswa menggunakan Django. Proyek ini dibuat sebagai bahan pembelajaran CRUD (Create, Read, Update, Delete) dengan Django Framework dan database SQLite.

---

## Fitur

- [x] **List Siswa** — Menampilkan semua data siswa
- [x] **Detail Siswa** — Menampilkan detail siswa berdasarkan ID
- [x] **Tambah Siswa** — Form untuk menambahkan siswa baru
- [ ] **Edit Siswa** — *(coming soon)*
- [ ] **Hapus Siswa** — *(coming soon)*

---

## Teknologi

- **Framework**: Django 6.0
- **Database**: SQLite 3
- **Template Engine**: Django Template Language (DTL)
- **Bahasa**: Python 3

---

## Prasyarat

Pastikan kamu sudah menginstall:

- [Python 3.10+](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installation/)
- Virtual environment (opsional, tapi direkomendasikan)

---

## Instalasi & Menjalankan Proyek

### 1. Clone Repository

```bash
git clone https://github.com/username/websekolah.git
cd websekolah
```

### 2. Buat Virtual Environment

```bash
# Linux/macOS
python3 -m venv .venv
source .venv/bin/activate

# Windows
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Jalankan Migrasi Database

```bash
python manage.py migrate
```

### 5. Jalankan Server Development

```bash
python manage.py runserver
```

Buka browser dan akses: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## Struktur Proyek

```
websekolah/
├── websekolah/           # Konfigurasi project utama (settings, urls, wsgi)
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── siswa/                # App untuk mengelola data siswa
│   ├── migrations/       # File migrasi database
│   ├── templates/        # Template HTML
│   ├── models.py         # Model: Siswa
│   ├── views.py          # Logic: list, detail, create, update, delete
│   ├── urls.py           # Routing app siswa
│   └── admin.py
├── manage.py             # Command line utility Django
├── db.sqlite3            # Database SQLite
└── requirements.txt      # Daftar dependency
```

---

## Database

Proyek ini menggunakan **SQLite** sebagai database default.

### Struktur Tabel `siswa`

| Kolom  | Tipe          | Keterangan               |
|--------|---------------|--------------------------|
| `id`   | INTEGER (PK)  | Auto-increment, Primary Key |
| `nama` | VARCHAR(255)  | Nama siswa               |
| `umur` | INTEGER       | Umur siswa               |

---

## Endpoint / URL

| URL | Method | Fungsi |
|-----|--------|--------|
| `/` | GET | List semua siswa |
| `/siswa/<id>/` | GET | Detail siswa |
| `/siswa/create/` | GET / POST | Form tambah siswa |
| `/siswa/update/<id>/` | GET | *(placeholder)* Edit siswa |
| `/siswa/delete/<id>/` | GET | *(placeholder)* Hapus siswa |
| `/admin/` | GET | Django Admin Panel |

---

## Cara Membuat Superuser (Admin)

```bash
python manage.py createsuperuser
```

Ikuti instruksi untuk membuat username, email, dan password.

---

## Perintah Berguna

```bash
# Jalankan server
python manage.py runserver

# Buat migrasi baru
python manage.py makemigrations

# Jalankan migrasi
python manage.py migrate

# Django shell
python manage.py shell

# Cek migrasi
python manage.py showmigrations
```

---

## Kontribusi

Proyek ini dibuat untuk tujuan pembelajaran. Kontribusi, saran, dan perbaikan sangat diterima!

---

## Lisensi

Distribusi dibawah lisensi [MIT](LICENSE).

---

> **Catatan**: Proyek ini menggunakan Django secara vanilla (tanpa Django REST Framework). Template HTML menggunakan Django Template Language (DTL) dengan sistem inheritance (`base.html`).

Dibuat dengan ❤️ untuk belajar Django.