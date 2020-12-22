import copy

def parseInput(file):
	with open(file, 'r') as ip:
		contents = ip.readlines()
		arr = [[item for item in item.rstrip()] for item in contents]
		return arr


def impLogic(arr):
	stateChange = True
	res = 0
	while stateChange:
		stateChange, newArray = loopArray(arr)
		res += 1
		# print(arr)
		arr = [[newArray[i][j] for j in range(len(newArray[0]))] for i in range(len(newArray))]
		# if res == 7: break
	# count the number of occupied seats
	print(arr)
	print(res)
	return len([1 for i in range(0, len(arr)) for j in range(len(arr[0])) if arr[i][j] == '#'])


def loopArray(arr):
	sc = False
	newArray = [[arr[i][j] for j in range(len(arr[0]))] for i in range(len(arr))]
	# print(arr, newArray)
	for i in range(len(arr)):
		for j in range(len(arr[0])):
			if arr[i][j] == 'L' and checkNeighbors(arr, i, j, arr[i][j]) >= 8:
				newArray[i][j] = '#'
				sc = True
			elif arr[i][j] == '#' and checkNeighbors(arr, i, j, arr[i][j]) >= 4:
				newArray[i][j] = 'L'
				sc = True
	# printArrays(arr, newArray)
	# print()
	if sc: return sc, newArray 
	else: return sc, arr


def checkNeighbors(arr, i, j, val) -> int:
	res = 0
	for k in [-1, 0, 1]:
		for m in [-1, 0, 1]:
			if i + k >= len(arr) or i + k < 0 or j + m >= len(arr[0]) or j + m < 0:
				# print('OUt', i + k, j + m, len(arr), len(arr[0]))
				res = res + 1 if val == 'L' else res
			elif val == 'L' and arr[i+k][j+m] in (val, '.'):
				# print('Neighbor empty',i + k, j + m, arr[i+k][j+m])
				res += 1
			elif val == '#' and arr[i+k][j+m] == val:
				# print('Neighbor occupied', i + k, j + m, arr[i+k][j+m])
				res += 1
	return res - 1 # remove the position of val 

def printArrays(lst1, lst2):
	for i, j in zip(range(len(lst1)), range(len(lst2))):
		print(lst1[i], lst2[j])

arr = parseInput('./ip/input11.txt')
# newArray = [['.' for j in range(len(arr[0]))] for i in range(len(arr))]
# print(newArray)
res = impLogic(arr)
print(res)