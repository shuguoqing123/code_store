
class make_xlat:
  def __init__ (self, *args, **kwds): 
    self.adict = dict(*args, **kwds)  
    self.rx = self.make_rx()   
  def make_rx(self):   
    print('|'.join(map(re.escape, self.adict)))   
    return re.compile('|'.join(map(re.escape, self.adict)))#escape取消转义  
  def one_xlat(self, match): 
    print(match.group(0))    
    return self.adict[match.group(0)] 
  def __call__ (self, text):    
    return self.rx.sub(self.one_xlat, text)
