from serial import Serial
from time import sleep

serial_ard = None # ainda não possuimos o hardware

arduino = Serial(serial_ard, 9600)
sleep(2) 

minimum_humidity = 300 

print("Verificando umidade do solo...")

try:
    while True:
        if arduino.in_waiting:
            
            data = arduino.readline().decode().strip()
            
            if data.isdigit():  
                humidity = int(data)
                print(f"Umidade recebida: {humidity}")

            
                if humidity < minimum_humidity:
                    print("Solo está seco. Ligando bomba...")
                    arduino.write(b"LIGAR\n")
                else:
                    print("Solo está úmido. Desligando bomba...")
                    arduino.write(b"DESLIGAR\n")

        sleep(1)

except KeyboardInterrupt:
    print("\nEncerrando monitoramento...")
    arduino.close()
