# rpi-bme280-env-monitor  
Aplikacja napisana w FastAPI, służąca do monitorowania parametrów środowiska z wykorzystaniem Raspberry Pi oraz czujnika BME280.

## Opis  
Program odczytuje dane z czujnika BME280 zamontowanego na Raspberry Pi i udostępnia je w formacie JSON przez API, dzięki czemu można je łatwo wykorzystać w innych aplikacjach lub dashboardach.

## Funkcjonalności  
- Odczyt temperatury, wilgotności i ciśnienia ze sprzętu.  
- Odczytane dane zwraca przy pomocy API.  
- Prosta konfiguracja i uruchomienie na Raspberry Pi.

## Wymagania  
- Raspberry Pi z systemem operacyjnym.  
- Czujnik BME280 (I²C) podłączony do Raspberry Pi (piny SDA, SCL, GND, zasilanie).  
- Python 3.  
- Biblioteka do obsługi BME280 + inne zależności, określone w `requirements.txt`.  
- Uprawnienia I²C (włączenie I²C w raspi-config lub odpowiednia konfiguracja).

## Instalacja  

1. Podłącz BME280 do Pi:

- VCC → 3.3 V
- GND → GND
- SDA → SDA (np. GPIO 2)
- SCL → SCL (np. GPIO 3)

2. Sklonuj repozytorium:  
```bash
git clone https://github.com/akulewicz/rpi-bme280-env-monitor.git  
cd rpi-bme280-env-monitor  
```
3. Zainstaluj zależności:
```bash
python3 -m venv venv  
source venv/bin/activate  
pip install -r requirements.txt  
```
4. Włącz I²C na Raspberry Pi:
```bash
sudo raspi-config  
# wybierz: Interfacing Options → I²C → Enable  
```

5. Uruchom aplikację:
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

Jeśi po uruchomieniu aplikacji otrzymasz błąd w stylu:
```bash
OSError: [Errno 121] Remote I/O error
```
lub dane nie są odczytywane — wykonaj test:
```bash
sudo i2cdetect -y 1
```
Jeżeli czujnik pojawi się pod adresem 0x77, zmień w pliku:
```bash
# app/services/bme280_service.py
address = 0x76
```
na:
```bash
address = 0x77
```

Zapisz plik i uruchom ponownie aplikację.


## API

```bash
GET http://<adres_raspberrypi>:8000/env
```

**Przykładowa odpowiedź:**

```json
{
  "temperature": 22.05,
  "humidity": 48.25,
  "pressure": 1011.36
}
```