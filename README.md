# Weather API Project

## 📂 Struktur File:
```
project-folder/
├── main.py
└── config.py
└── creator_id.txt
```

## 📝 Deskripsi:
Proyek sederhana ini mengambil data cuaca dari OpenWeatherMap menggunakan Python.

### 1️⃣ **main.py**  
- Membaca `creator_id.txt` dan mencetak isinya.
- Meminta input nama kota.
- Menggunakan fungsi `get_weather()` dari `config.py`.
- Menampilkan hasil cuaca.

### 2️⃣ **config.py**  
- Mendefinisikan fungsi `get_weather()`.
- Menggunakan `requests` untuk memanggil API.
- Memproses respons JSON dan menampilkan hasil cuaca atau pesan error.

---

## 💻 Cara Menjalankan:
### 1. **Persiapkan Lingkungan:**
- Pastikan Python terinstal.
- Instal dependensi:
  ```bash
  pip install requests
  ```

### 2. **Siapkan API Key:**
- Dapatkan API key dari [OpenWeatherMap](https://openweathermap.org/).
- Masukkan API key di `main.py` pada baris:
  ```python
  api_key = "input_your_api_key"
  ```

### 3. **Jalankan Script:**
```bash
python main.py
```

---
## 🛡️ Penanganan Error:
- **400:** Permintaan tidak valid.
- **401:** API Key salah.
- **404:** Kota tidak ditemukan.
- Format JSON tidak sesuai.

---
## 💡 Contoh Hasil Output:
```
INPUT CITY NAME: Jakarta
Cuaca di Jakarta, ID: 30°C, clear sky
```

