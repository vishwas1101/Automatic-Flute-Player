"""
Created on Fri Feb  7 10:49:29 2020
@author: abhij
"""
port_a = ("COM6")


import serial as sl
import io
import time

file = open(r"C:\Users\abhij\Desktop\Projects\Automation and Robotics club\Automatic Flute\Excel files\Notes.csv", "r")
str_array = file.read()
str_array = str_array.split("\n")

notes = []

for string in range(1, len(str_array)):
    text  = str_array[string].split(",")
    notes.append(text[0])    

ser = sl.Serial(port = port_a, baudrate = 9600)
sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))
for text1 in text:
    sio.write((text1))
    sio.flush()
    
    count = 0
    while(true):
        
        time.sleep(10)
        check_text = sio.readline()
        if check_text = "executed":
            break;
        count += 1
        
        if count >= 3000:
            print("message lost")
            break;
