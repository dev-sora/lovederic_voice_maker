import wave
import numpy as np
import struct
from random import randint
import csv

fname = 'test.wav'
wavefile = wave.open(fname, 'r')
framerate = wavefile.getframerate()
data = wavefile.readframes(wavefile.getnframes())
x = np.frombuffer(data, dtype="int16")

output = []

for i in range(20):
    start = randint(0, len(x)-44100)
    output.extend(x[start:start+22050] + x[start+500:start+22550])

x_fix = np.array([i*2 for i in output])
x_fix = struct.pack("h"*len(x_fix), *x_fix)

w = wave.Wave_write('output.wav')
w.setnchannels(1)
w.setsampwidth(2)
w.setframerate(44100)
w.writeframes(x_fix)
w.close()