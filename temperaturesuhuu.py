
#no.1 fungsi meng konversi suhu

def konversisuhu(temperature, value):

    #Jika value adalah 'C', maka suhu yang 
    #diterima dianggap dalam Fahrenheit dan akan dikonversi ke Celcius 
    if value == 'C':
        temperaturesuhu = (temperature - 32) * 5/9
        return temperaturesuhu, 'C'
    else:  
        #Jika value adalah selain 'C', maka suhu 
        #dianggap dalam Celcius dan akan dikonversi ke Fahrenheit
        temperaturesuhu = (temperature * 9/5) +32
        return temperaturesuhu, 'F'


#meng input suhu 30°C yang nantinya akan dikonversi ke fahreinheit
celcius_temperature = 30
temperaturesuhu, target_value = konversisuhu(celcius_temperature, 'F')
print (f"{celcius_temperature}°C dikonversi ke Fahreinheit adalah {temperaturesuhu}°{target_value} ")


#meng input suhu 86°F yang nantinya akan dikonversi ke celcius
fahreinheit_temperature = 86
temperaturesuhu, target_value = konversisuhu(fahreinheit_temperature, 'C')
print (f"{fahreinheit_temperature}°F dikonversi ke celcius adalah {temperaturesuhu}°{target_value}")




#no. 2
import math #library untuk operasi matematika

#membuat fungsi lamda yang diberinama luas_lingkaran.
luas_lingkaran = lambda r: math.pi * r*r

# Contoh penggunaannya

jari_jari = 7
area = luas_lingkaran(jari_jari)
print(f"Luas lingkaran dengan jari-jari {jari_jari} adalah {area:.2f}")