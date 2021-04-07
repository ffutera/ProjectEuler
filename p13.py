import numpy as np
data = [ int(i) for i in open("p13.txt","r").read().split("\n") ]
firstTen = int("".join([i for i in str(np.sum(data))][0:10]))
print(firstTen)