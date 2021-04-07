import math

def palindromeCheck(number):
	return str(number) == str(number)[::-1]

palindromicSums = []
for i in range(1, int(math.pow(10,4))):
#for i in range(1, 1000):
	counter=i
	s=0
	sumedNumbers = 0
	while (s<math.pow(10,8)):
	#while (s<1000):
		s+=int(math.pow(counter,2))
		sumedNumbers+=1
		#if palindromeCheck(s) and i!=counter:
		if palindromeCheck(s) and sumedNumbers>1:
			print("first value: ",i," second value ",counter, " palindromic sum: ", s)
			if s<math.pow(10,8):
			#if s<1000:
			#palindromicSums.append(s)
				palindromicSums.append(s)
		counter+=1
nonDuplicatedSums = list(dict.fromkeys(palindromicSums))
print(nonDuplicatedSums)
print(sum(nonDuplicatedSums))


