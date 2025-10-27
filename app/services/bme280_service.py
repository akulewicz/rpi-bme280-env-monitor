import smbus2
import bme280


logger = logging.getLogger(__name__)

port = 1
address = 0x76
bus = smbus2.SMBus(port)

def read_bme280_data() -> dict:
    """Odczytuje temperaturę, wilgotność i ciśnienie z czujnika BME280."""    
    try:
        calibration_params = bme280.load_calibration_params(bus, address)
        data = bme280.sample(bus, address, calibration_params)
        return {
            "temperature": round(data.temperature, 2),
            "humidity": round(data.humidity, 2),
            "pressure": round(data.pressure, 2)
        }
    except Exception as e:
        logger.warning(f"Nie udało sie odczytać danych z czujnika BME280: {e}")
        return {}

