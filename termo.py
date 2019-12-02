import smbus2 #importejam lib
import bme280 #importejam lib
from datetime import datetime #importejam lib
import time #importejam lib
import keyboard #importejam lib
import RPi.GPIO as GPIO #importejam lib
GPIO.setmode(GPIO.BCM) #nomainam gpio modu
GPIO.setwarnings(False) #izsledzam bridinajums 
GPIO.setup(4, GPIO.IN, GPIO.PUD_UP) #definejm gpio pinu
GPIO.setup(18, GPIO.IN, GPIO.PUD_UP) #definejm gpio pinu
GPIO.setup(23, GPIO.IN, GPIO.PUD_UP) #definejm gpio pinu
print("DOne") #izprintejam, la zinatu ka viss kartiba
def truncate(n): #definejam funkciju lai saisinatu
        return int(n * 10000) / 10000 #funkcija



port = 1
address = 0x76
bus = smbus2.SMBus(port)
calibration_params = bme280.load_calibration_params(bus, address)
I = "        "
data = bme280.sample(bus, address, calibration_params)

        
try:
    while True:
        button_state1 = GPIO.input(4) #Ja poga ir inputs true
        button_state2 = GPIO.input(18)
        button_state3 = GPIO.input(23)
        print("Ja velies sanemt datus nospied -c-") #printejam,lai zinatu.
        if button_state1 == GPIO.LOW: #Ja nospiez pogu, daram to
                GPIO.output(17,GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(17,GPIO.LOW)
                print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'),(I), truncate(data.temperature),(I), truncate(data.pressure), file=open("output.txt", "a+"))
                print(datetime.now().strftime('%Y-%m-%d %H:%M:%S')) #printejam laiku
                print(truncate(data.temperature)) #printejam temperaturu
                print(truncate(data.pressure)) #printejam spiedienu
                print(truncate(data.humidity)) #printejam mitrumu
                print("""\t \t Ja velies redzet saglabatos datus, nospied
                 pogu 3 vai -c- uz klaviaturas uz klaviaturas.""") #printejam tekstu
        if button_state2 == GPIO.LOW:
                GPIO.output(27,GPIO.HIGH)
                GPIO.output(17,GPIO.HIGH)
                GPIO.output(22,GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(27,GPIO.LOW)
                GPIO.output(17,GPIO.LOW)
                GPIO.output(22,GPIO.LOW)
                f = open('output.txt', 'r') #definejam lasit datu failu
                faila_saturs = f.read() #lasam datu failu
                print(faila_saturs) #printejam, kas faila
                f.close() #aizveram datu failu 
                print("Ja velies beigt nospied. -e-")
               
        if keyboard.read_key() == "c":
                GPIO.output(27,GPIO.HIGH)
                GPIO.output(22,GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(22,GPIO.LOW)
                GPIO.output(27,GPIO.LOW)
                f = open('output.txt', 'r')
                faila_saturs = f.read()
                print(faila_saturs)
                f.close()
                print("Ja velies beigt nospied. -e-")
        if keyboard.read_key() == "e": #ja nospiez uz klaviaturas jebkura bridi
                break #beidz visu programmu
                
                



