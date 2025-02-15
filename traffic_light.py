import time

print("***** the traffic signal lights *****")

def display_light(color):
    print(f"{color} light is ON.")

def traffic_light():
    while True:
        display_light("RED")
        time.sleep(5)
        display_light("YELLOW")
        time.sleep(3)
        display_light("GREEN")
        time.sleep(5)

traffic_light()        
