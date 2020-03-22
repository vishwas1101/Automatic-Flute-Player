from time import sleep

# from pysine import sine
from pyfirmata import ArduinoMega
import time

upperbt = 60
lowerbt = 0
l = .3
h = .9
board = ArduinoMega('COM15')
servo1 = board.get_pin('d:7:s')  #
servo2 = board.get_pin('d:8:s')
servo3 = board.get_pin('d:6:s')  #
servo4 = board.get_pin('d:9:s')
servo5 = board.get_pin('d:5:s')  #
servo6 = board.get_pin('d:10:s')
servo7 = board.get_pin('d:4:s')  #
servo8 = board.get_pin('d:13:s')
servo9 = board.get_pin('d:2:s')  #
servo10 = board.get_pin('d:12:s')
servo11 = board.get_pin('d:3:s')  #
servo12 = board.get_pin('d:11:s')
airpin = board.get_pin('d:14:s')  # not used yet
# to initialize all values to zero angle
servo1.write(0)  #
servo2.write(0)
servo3.write(0)  #
servo4.write(0)
servo5.write(0)  #
servo6.write(0)
servo7.write(0)
servo8.write(0)
servo9.write(0)  #
servo10.write(0)
servo11.write(0)  #
servo12.write(0)
sleep(2)
# the mechanism of opening and closing notes
matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
          [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
""""matrix2 = [[0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
           [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
           [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
           [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
           [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
           [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
           [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
           [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1]]
"""
s = 207
# r1 = 220
r2 = 233
# r3 = 246
g3 = 261
m1 = 277
# m2 = 293
p = 311
# d1 = 329
d2 = 349
# d3 = 369
n3 = 391


# rt = 415
# rt3 = 440
# rt4 = 466
# rt5 = 493
# rt6 = 523
# r0 = 0

def notes(i, tim):
    if i == s:
        play(0, tim, l)
    if i == r2:
        play(1, tim, l)
    if i == g3:
        play(2, tim, l)
    if i == m1:
        play(3, tim, l)
    if i == p:
        play(4, tim, l)
    if i == d2:
        play(5, tim, l)
    if i == n3:
        play(6, tim, l)
    if i==0:
        sleep(.5)


"""""
def notes(i, tim):
    if i == s:
        play(7, tim, l)
    if i == r1:
        play(8, tim, l)
    if i == r2:
        play(9, tim, l)
    if i == r3:
        play(10, tim, l)
    if i == g3:
        play(11, tim, l)
    if i == m1:
        play(0, tim, l)
    if i == m2:
        play(1, tim, l)
    if i == p:
        play(2, tim, l)
    if i == d1:
        play(3, tim, l)
    if i == d2:
        play(4, tim, l)
    if i == d3:
        play(5, tim, l)
    if i == n3:
        play(6, tim, l)
    if i == r0:
        play(7, tim, h)
    if i == r0:
        play(8, tim, h)
    if i == r0:
        play(10, tim, h)
    if i == r0:
        play(11, tim, h)
    if i == r0:
        play(11, tim, h)
    if i == 554:
        play(0, tim, h)
    if i == 587:
        play(1, tim, h)
    if i == 622:
        play(2, tim, h)
    if i == 659:
        play(3, tim, h)
    if i == 698:
        play(4, tim, h)

"""
# sample song
array = [[s, .5], [s, 10], [s, .5], [r2, .5], [s, .5],
         [g3, .5], [r2, 1], [s, .5], [s, .5], [r2, .5],
         [s, .5], [p, .5], [r2, 1], [s, .5], [s, 0.5],
         [s, .5], [n3, .5], [p, 0.5], [g3, .5], [r2, 1],
         [m1, .5], [m1, .5], [g3, .5],[s,.5], [r2, .5], [s, 1.5]]
array2=[[s,.5],[s,.5],[r2,.5],[g3,1.5],[m1,.5],[g3,.5],
        [r2,.5],[s,.5],[r2,.5],[p,1.5],[g3,.5],[p,.5],[d2,.5],
        [p,.5],[m1,.5],[g3,.5],[r2,.5]]
array3=[[g3,.5],[g3,.5],[g3,.5],[g3,.5],[0,3],[g3,.5],
        [g3,.5],[g3,.5],[g3,.5],[p,.5],[s,.5],
        [r2,.5],[g3,1]]
# array2=[[],[],[],[],[],[],[],[],[],[]]

# the servos getting the reading from the matrix
def play(number, delay, air):
    airpin.write(air / 100)
    for t in range(lowerbt, upperbt, 2):
        c = t
        servo1.write((1 - matrix[number][11]) * (upperbt - t) + (matrix[number][11]) * t)
        servo2.write((1 - matrix[number][10]) * (upperbt - c) + (matrix[number][10]) * t)
        servo3.write((1 - matrix[number][9]) * (upperbt - c) + (matrix[number][9]) * t)
        servo4.write((1 - matrix[number][8]) * (upperbt - c) + (matrix[number][8]) * t)
        servo5.write((1 - matrix[number][7]) * (upperbt - c) + (matrix[number][7]) * t)
        servo6.write((1 - matrix[number][6]) * (upperbt - c) + (matrix[number][6]) * t)
        servo7.write((1 - matrix[number][5]) * (upperbt - c) + (matrix[number][5]) * t)
        servo8.write((1 - matrix[number][4]) * (upperbt - c)+5 + (matrix[number][4]) * t)
        servo9.write((1 - matrix[number][3]) * (upperbt - c) + (matrix[number][3]) * t)
        servo10.write((1 - matrix[number][2]) * (upperbt - c) + (matrix[number][2]) * t)
        servo11.write((1 - matrix[number][1]) * (upperbt - c) + (matrix[number][1]) * t)
        servo12.write((1 - matrix[number][0]) * (upperbt - c) + (matrix[number][0]) * t)

    sleep(delay)


# to initialize to play notes
for k in range(1, 25):
    notes(array[k][0], array[k][1])
servo1.write(0)
servo2.write(0)
servo3.write(0)
servo4.write(0)
servo5.write(0)
servo6.write(0)
servo7.write(0)
servo8.write(0)
servo9.write(0)
servo10.write(0)
servo11.write(0)
servo12.write(0)

sleep(2)
