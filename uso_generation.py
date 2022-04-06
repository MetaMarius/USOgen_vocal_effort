import random
import math
from os import listdir
import numpy as np
import slab
import pathlib
import os

DIR = pathlib.Path(os.getcwd())

dis_1 = [DIR / "laughter_test" / "dis_1" / f for f in listdir(DIR / "laughter_test" / "dis_1")]
dis_2 = [DIR / "laughter_test" / "dis_2" / f for f in listdir(DIR / "laughter_test" / "dis_2")]
dis_3 = [DIR / "laughter_test" / "dis_3" / f for f in listdir(DIR / "laughter_test" / "dis_3")]
dis_4 = [DIR / "laughter_test" / "dis_4" / f for f in listdir(DIR / "laughter_test" / "dis_4")]
dis_5 = [DIR / "laughter_test" / "dis_5" / f for f in listdir(DIR / "laughter_test" / "dis_5")]


def gen_stimulus(d):
    n = 0
    while n < 7:
        s = combine_sounds(distance=d, n_sounds=3)
        a = 'p'
        while a == "p":
            s.play()
            a = input('Take?')
        if a == "y":
            s.write("uso_second_draft/" + "new_uso_" + input("File number:") + '.wav')
        elif a == "s":
            break
        else:
            continue

    print("Finished")


def combine_sounds(distance, n_sounds):

    t = random.choice(distance)
    sout = slab.Sound(t)

    # if sout.duration > 1.0:
    #    sout = sout.data[:, 0]
    #    sout = sout[np.where((sout > 0.03) == True)[0][0]:np.where((sout > 0.03) == True)[0][-1]][1000:25000]   # cutting bases 24000 samples long and taking only parts where it is louder than 0.03
    # else:
    #    sout = sout.data[:, 0]

    for i in range(n_sounds):
        f = random.choice(distance)
        s = slab.Sound(f)
        sout = slab.Sound.sequence(sout, s)

        # s_sr = s.samplerate
        # if base_sr != s_sr:
        #    print("Error: Samplerates don't match")
        # offset = math.ceil(np.random.random(1) * length - 4800)
        # if offset < 0:
        #    offset = 0
        # s = np.append(np.zeros(offset), s)
        # s = np.append(s, np.zeros(length))
        # s = s[:length]  # /15000
        # sout = np.sum((sout, s), axis=0)
    # sout.data = sout.data*0.5
    # sout = sout / abs(sout).max()
    return slab.Sound(data=sout, samplerate=48000)
