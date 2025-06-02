

import serial
import time
from datetime import datetime

# Configuration du port série (modifie le port selon ton système, ex: 'COM3' sur Windows, '/dev/ttyUSB0' sur Linux)
PORT = '/dev/ttyACM0'
BAUDRATE = 115200
INTERVAL = 1  # secondes

def main():
    try:
        with serial.Serial(
            port='/dev/ttyACM0',
            baudrate=115200,
            bytesize=serial.EIGHTBITS,   # 8 bits de données
            parity=serial.PARITY_NONE,   # Pas de bit de parité
            stopbits=serial.STOPBITS_ONE,# 1 bit de stop
            timeout=1                    # timeout de lecture (1 seconde)
            ) as ser:
            print(f"Connexion ouverte sur {PORT} à {BAUDRATE} bps.")
            while True:
                current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                message = f"Heure actuelle: {current_time}\n"
                ser.write(message.encode('utf-8'))
                print(f"Envoyé: {message.strip()}")
                time.sleep(INTERVAL)
    except serial.SerialException as e:
        print(f"Erreur de communication série: {e}")
    except KeyboardInterrupt:
        print("\nArrêt du script par l'utilisateur.")

if __name__ == "__main__":
    main()
