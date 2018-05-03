import os
import sys
import struct


def del_pre_sil(name1, name2):
    data = open(name1, 'rb').read()

    cframesum = 0
    lframesum = 0

    i = 0
    while i < len(data):
        point = abs(struct.unpack('h', data[i:i+2])[0])
        cframesum += point
        if i%640 == 0 and i > 0:
            if cframesum > 3*lframesum and lframesum > 3000:break
            lframesum = cframesum
            cframesum = 0
        i += 2

    if i > 640*25:
        i -= 640*25
    else:
        i = 0
    newpcm = open(name2, 'wb')
    while i < len(data):
        point = struct.unpack('h', data[i:i + 2])[0]
        newpcm.write(struct.pack('h', point))
        i += 2


if __name__=='__main__':
    del_pre_sil('20180503.pcm', 'new.pcm')

