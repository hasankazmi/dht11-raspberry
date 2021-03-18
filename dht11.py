import time 
import board
import adafruit_dht

sensor = adafruit_dht.DHT11(board.D4, use_parse= False)

while True:
    try:
        temp_c = sensor.temperature
        temp_f = temp_c * (9/2) + 32
        humidity = sensor.humidity
        print("temp: {.1f} f / {.1f} C Humidity: {}%".format(temp_c, temp_f, humidity))
    except RuntimeError as error:
        print(error.arg[0])
        time.sleep(2)
        continue
    except Exception as error:
        sensor()
        exit
    time.sleep(2.0)