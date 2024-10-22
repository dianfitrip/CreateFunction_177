def konversisuhu(temperature, value):
    if value == 'C':
        temperaturesuhu = (temperature - 32) * 5/9
        return temperaturesuhu, 'C'
    else:
        temperaturesuhu = (temperature * 9/5) +32
        return temperaturesuhu, 'F'
    
celcius_temperature = 30
temperaturesuhu, target_value = konversisuhu(celcius_temperature, 'F')
print (f"{celcius_temperature}°C dikonversi ke Fahreinheit adalah {temperaturesuhu}°{target_value} ")



fahreinheit_temperature = 86
temperaturesuhu, target_value = konversisuhu(fahreinheit_temperature, 'C')
print (f"{fahreinheit_temperature}°F dikonversi ke celcius adalah {temperaturesuhu}°{target_value}")