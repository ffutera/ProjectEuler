f = open("p54.txt", "r")
data = f.read().split("\n")
li = []
for d in data:
	temp = (d.split(" "))
	#elem = (temp[0:5],temp[5:10])
	m = []
	n = []
	for i in range(5):
		m.append((temp[i][0],temp[i][1]))
		n.append((temp[i+5][0],temp[i+5][1]))
	li.append((m,n))

def sortOrder(char):
	if char == '2':
		return 2
	if char == '3':
		return 3
	if char == '4':
		return 4
	if char == '5':
		return 5
	if char == '6':
		return 6
	if char == '7':
		return 7
	if char == '8':
		return 8
	if char == '9':
		return 9
	if char == 'T':
		return 10
	if char == 'J':
		return 11
	if char == 'Q':
		return 12
	if char == 'K':
		return 13
	if char == 'A':
		return 14
	return 0

def checkRoyalFlush(array):
	count = 0
	for item in list(['A','K','Q','J','T']):
		if (array[0][0] == item) or (array[1][0] == item) or (array[2][0] == item) or (array[3][0] == item) or (array[4][0] == item):
			count+=1
	if (array[0][1]==array[1][1]==array[2][1]==array[3][1]==array[4][1]):
		count+=1
	return count==6

def straightFlush(array):
	context = "A23456789TJQKA"
	cards = [array[0][0],array[1][0],array[2][0],array[3][0],array[4][0]]
	cards.sort(key=sortOrder)
	p = "".join(cards)
	return p in context and array[0][1]==array[1][1]==array[2][1]==array[3][1]==array[4][1]

def fourKind(array):
	cards = [array[0][0],array[1][0],array[2][0],array[3][0],array[4][0]]
	cards.sort(key=sortOrder)
	p = "".join(cards)
	smallerThan = p[0:4]
	largerThan = p[1:5]
	string = list(["2222","3333","4444","5555","6666","7777","8888","9999","TTTT","JJJJ","QQQQ","KKKK","AAAA"])
	if smallerThan in string or largerThan in string:
		print(smallerThan, largerThan)
	return smallerThan in string or largerThan in string


def getWinner(element):
	oneHand = element[0]
	twoHand = element[1]
	orderOne = 0
	orderTwo = 0
	if checkRoyalFlush(oneHand):
		orderOne = 10
	elif straightFlush(oneHand):
		orderOne=9
	elif fourKind(oneHand):
		orderOne=8
	if checkRoyalFlush(twoHand):
		orderTwo = 10
	elif straightFlush(twoHand):
		orderTwo = 9
	elif fourKind(twoHand):
		orderOne=8
	return 0

winOne = 0
winTwo = 0
for element in li:
	winner = getWinner(element)
	if (winner == 1):
		winOne+=1
	else:
		winTwo+=1