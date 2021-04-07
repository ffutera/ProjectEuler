import math
print(math.pow(sum([i for i in range(1,101)]),2)-sum(math.pow(i,2) for i in range(101)))