def isIncreasing(c):
	number = str(c)
	length = len(number)
	increasing = True
	for i in range(1,length):
		if number[i]<number[i-1]:
			increasing = False
	return increasing

def isDecreasing(c):
	number = str(c)
	length = len(number)
	decreasing = True
	for i in range(1,length):
		if number[i]>number[i-1]:
			decreasing = False
	return decreasing

proportion = 0.0
bumpy = 0
counter = 0
while (proportion!=0.99):
	counter+=1
	if not isIncreasing(counter) and not isDecreasing(counter):
		bumpy+=1
		print(counter)
	proportion = bumpy/counter

print(proportion)
print(counter)