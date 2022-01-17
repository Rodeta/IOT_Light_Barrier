
import RPi.GPIO as GPIO
import os, time
from multiprocessing import Process

RECEIVER_PIN = 23
RECEIVER_PIN2 = 25
def callback_func(channel):
    if GPIO.input(channel):
        print("Lichtschranke 1 wurde unterbrochen {}")
        
        # alternativ kann ein Script / Shell Befehl gestartet werden
        # os.system("ls")
def callback_func2(channel):
    if GPIO.input(channel):
        print("Lichtschranke 2 wurde unterbrochen {}")
        
        # alternativ kann ein Script / Shell Befehl gestartet werden
        # os.system("ls")
def light_barrier1_check():
    try:
        while True:
            time.sleep(1)
            if(GPIO.input(23)== GPIO.HIGH):
                print("Schranke 1 verbunden")
    except:
        # Event wieder entfernen mittels:
        GPIO.remove_event_detect(RECEIVER_PIN)
        
def light_barrier2_check():
    try:
        while True:
            time.sleep(1)
            if(GPIO.input(25) == GPIO.HIGH):
                print("Schranke 2 verbunden")
    except:
        # Event wieder entfernen mittels:
        GPIO.remove_event_detect(RECEIVER_PIN2)
def light_barrier3_check(i):
    
    while(GPIO.input(25) == GPIO.HIGH):
        if(i==1):
            i = 0
            print(i)
        #print("Schranke verbunden")
    time.sleep(3)
    print("Schranke unterbrochen")
    i = 1
    
      
   
if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    
    #GPIO.setup(RECEIVER_PIN, GPIO.IN)
    GPIO.setup(RECEIVER_PIN2, GPIO.IN)
    #GPIO.add_event_detect(RECEIVER_PIN, GPIO.RISING, callback=callback_func, bouncetime=200)
    #GPIO.add_event_detect(RECEIVER_PIN2, GPIO.RISING, callback=callback_func2, bouncetime=200)
    #light_barrier1_check()
    i = 0
    while True:
        light_barrier3_check(i)
    #light_barrier2_check()
    #p1 = Process(target=light_barrier1_check)
    #p1.start()
    #p2 = Process(target=light_barrier2_check)
    #p2.start()
    #p1.join()
    #p2.join()

