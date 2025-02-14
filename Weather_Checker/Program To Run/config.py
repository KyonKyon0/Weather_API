# Simple Weather API 
import requests

def get_weather(api_key, base_url, city):
    if not city.strip():
        return "Error: Nama kota tidak boleh kosong."
    
    url = f"{base_url}?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    
    if response.ok:
        try:
            data = response.json()
            if 'main' in data and 'weather' in data:
                temp = data['main']['temp']
                description = data['weather'][0]['description']
                country = data['sys'].get('country', 'N/A')
                return f"Cuaca di {city}, {country}: {temp}°C, {description}"
            else:
                return "Error: Format respons API tidak sesuai."
        except ValueError:
            return "Error: Gagal memproses respons JSON."
    elif response.status_code == 400:
        return "Error 400: Permintaan tidak valid. Periksa API Key atau URL."
    elif response.status_code == 401:
        return "Error 401: API Key salah atau tidak diberikan."
    elif response.status_code == 404:
        return f"Error 404: Kota '{city}' tidak ditemukan. Periksa parameter kota."
    else:
        return f"Error {response.status_code}: Tidak dapat mengambil data cuaca."

