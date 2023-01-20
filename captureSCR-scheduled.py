import os
import argparse
import pyautogui
import time

parse_it = argparse.ArgumentParser()
parse_it.add_argument("-p", "--path", help="absolute path to store screenshot.", default=r"./images")
parse_it.add_argument("-t", "--type", help="h (in hour) or m (in minutes) or s (in seconds)", default='h')
parse_it.add_argument("-f", "--frequency", help="frequency for screenshot per h/m/s.", default=1, type=int)

arguments = parse_it.parse_args()
sec = 0.

if arguments.type == 'h':
    sec = 60 * 60 / arguments.frequency
elif arguments.type == 'm':
    sec = 60 / arguments.frequency

if sec < 1.:
    sec = 1.
    
if os.path.isdir(arguments.path) != True:
    os.mkdir(arguments.path)

try:
    while True:
        t = time.localtime()
        current_time = time.strftime("%H_%M_%S", t)
        file = current_time + ".jpg"
        image = pyautogui.screenshot(os.path.join(arguments.path,file))
        print(f"{file} saved successfully.\n")
        time.sleep(sec)
        
except KeyboardInterrupt:
    print("Interrupt: user interrupt")