import wave
import numpy as np
import struct
from random import randint
import csv
import sys

argvs = sys.argv
flag = 0

try:
    if argvs[1] == "-low":
        flag = 1
    elif argvs[1] == "-high":
        flag = 2
except IndexError:
    pass

fname = 'test.wav'
wavefile = wave.open(fname, 'r')
framerate = wavefile.getframerate()
data = wavefile.readframes(wavefile.getnframes())
x = np.frombuffer(data, dtype="int16")

output = []
prev = 0
for i in range(40):
    while(1):
        start = randint(0, len(x)-54100)
        if abs(start-prev)<44100:
            continue
        else:
            prev = start
            break
    tmp = x[start:start+15000] + x[start+600:start+15600]
    output.extend(tmp[::-1])
print(len(output))
final = []
if flag==1:
    for i in range(len(output)):
        final.append(output[i])
        if i%5==0:
            final.append(output[i])
elif flag==2:
    for i in range(len(output)):
        if i%7==0:
            continue
        final.append(output[i])
else:
    final = output

x_fix = np.array([i*2 for i in final])
x_fix = struct.pack("h"*len(x_fix), *x_fix)

w = wave.Wave_write('output.wav')
w.setnchannels(1)
w.setsampwidth(2)
w.setframerate(44100)
w.writeframes(x_fix)
w.close()