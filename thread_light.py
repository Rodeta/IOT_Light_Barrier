
import RPi.GPIO as GPIO
import os, time, asyncio


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
async def light_barrier1_check():
    try:
        while True:
            await asyncio.sleep(1)
            if(GPIO.input(23)== GPIO.HIGH):
                print("Schranke 1 verbunden")
    except:
        # Event wieder entfernen mittels:
        GPIO.remove_event_detect(RECEIVER_PIN)
        
async def light_barrier2_check():
    try:
        while True:
            await asyncio.sleep(1)
            if(GPIO.input(25) == GPIO.HIGH):
                print("Schranke 2 verbunden")
    except:
        # Event wieder entfernen mittels:
        GPIO.remove_event_detect(RECEIVER_PIN2)

async def run_task():
    task1 = asyncio.create_task(light_barrier1_check())
    task2 = asyncio.create_task(light_barrier2_check())
    await task1
    await task2
        
if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    
    GPIO.setup(RECEIVER_PIN, GPIO.IN)
    GPIO.setup(RECEIVER_PIN2, GPIO.IN)
    GPIO.add_event_detect(RECEIVER_PIN, GPIO.RISING, callback=callback_func, bouncetime=200)
    GPIO.add_event_detect(RECEIVER_PIN2, GPIO.RISING, callback=callback_func2, bouncetime=200)
    
    asyncio.run(run_task())

