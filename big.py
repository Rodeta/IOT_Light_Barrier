import RPi.GPIO as GPIO
import os, time

import threading

import requests


receiver_pin_1 = 18
receiver_pin_2 = 23

lock = threading.Lock()
car_count = 0

def increase_parking_row_space(rowId):
    with lock:
        request_try = 0 
        update_path = 'https://192.168.0.94:44378/api/parkingrow/'+ str(rowId)
        data = {"increasing":True}
        patch_request = requests.patch(update_path, json=data, verify=False)
        print(patch_request.status_code)
        if patch_request.status_code != 200:
            while(patch_request.status_code != 200 or request_try <3):
                time.sleep(3)
                patch_request = requests.patch(update_path, json=data, verify=False)
                request_try = request_try + 1
        else:
            print("[{}]Space in parking row ".format(current_time_ms()) + str(rowId) + " succesfully increased")
        
def decrease_parking_row_space(rowId):
    with lock:
        request_try = 0 
        update_path = 'https://192.168.0.94:44378/api/parkingrow/'+ str(rowId)
        data = {"increasing":False}
        patch_request = requests.patch(update_path, json=data, verify=False)
        if patch_request.status_code != 200:
            while(patch_request.status_code != 200 or request_try <3):
                time.sleep(3)
                patch_request = requests.patch(update_path, json=data, verify=False)
                request_try = request_try + 1
        else:
            print("[{}]Space in parking row ".format(current_time_ms()) + str(rowId) + " succesfully decreased")


def current_time_ms():
    return round(time.time() * 1000)

# def callback(channel):
#     if GPIO.input(channel) == GPIO.LOW:
#         # Lichtschranke misst Laser, kein Detection-Event
#         callback_connect(channel)
#     else:
#         # Lichtschranke misst Laser NICHT, Detection-Event
#         callback_disconnect(channel)


def update_car_count(channel):
    if channel is receiver_pin_1:
        decrease_parking_row_space(1)
    if channel is receiver_pin_2:
        increase_parking_row_space(1)
        

# def callback_disconnect(channel):
#     ldr = -1
#     if channel is receiver_pin_1:
#         ldr = 1
#         # print("Ein KfZ ist auf den Parkplatz aufgefahren.")
#     if channel is receiver_pin_2:
#         ldr = 2
#         # print("Ein KfZ ist von dem Parkplatz abgefahren.")
#     print("[{}] Lichtschranke {} wurde unterbrochen".format(current_time_ms(), ldr))
#     time.sleep(0.01)
        
# def callback_connect(channel):
#     ldr = -1
#     if channel is receiver_pin_1:
#         ldr = 1
#     if channel is receiver_pin_2:
#         ldr = 2
#     print("[{}] Lichtschranke {} wurde verbunden".format(current_time_ms(), ldr))
#     time.sleep(0.01)
    
def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    
    GPIO.setup(receiver_pin_1, GPIO.IN)
    GPIO.setup(receiver_pin_2, GPIO.IN)
    
    GPIO.add_event_detect(receiver_pin_1, GPIO.RISING, callback=update_car_count, bouncetime=200)
    GPIO.add_event_detect(receiver_pin_2, GPIO.RISING, callback=update_car_count, bouncetime=200)

    try:
        while True:
           time.sleep(0.5)

    except:
        # Event wieder entfernen mittels:
        GPIO.remove_event_detect(receiver_pin_1)
        GPIO.remove_event_detect(receiver_pin_2)
        
if __name__ == '__main__':
    
    main()
    
