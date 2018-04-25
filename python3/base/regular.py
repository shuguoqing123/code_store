#!/usr/bin/env python3
#-*-coding:utf-8-*-

#字符串替换类
import re

class make_xlat:
    def __init__(self, *args, **kwds):
        self.adict = dict(*args, **kwds)
        self.rx = self.make_rx()
    def make_rx(self):
        return re.compile('|'.join(map(re.escape, self.adict)))#escape取消转义
    def one_xlat(self, match):
        return self.adict[match.group(0)]
    def __call__ (self, text):
        return self.rx.sub(self.one_xlat, text)


if __name__=="__main__":
    repl = {'a':'A','b':'B','c':'C'}
    xlat = make_xlat(repl)
    print(xlat('cab'))
