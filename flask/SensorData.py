from WasteWater import get_water_level
from GasLevel import get_gas_level
from WaterPressure import get_water_pressure
from AirQuality import get_air_quality

def sensorData():
    return {
        'wasteWaterLevel': get_water_level(),
        'waterPressureLevel': get_water_pressure(),
        'gasLevel': get_gas_level(),
        'airQuality': get_air_quality()
    }
