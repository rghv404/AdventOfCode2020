input = open('input5.txt', 'r')
boardingPassList = [a.rstrip() for a in input.readlines()]

def findVal(pattern: str) -> int:
	n = len(pattern)
	l, r = 0, (2**n) - 1 
	# print(l, r)
	for char in pattern:
		# if lower half
		mid = (l + r) // 2
		if char in ('F', 'L'): r = mid
		else: l = mid + 1
		# print(l, r)
	return l

rows = [r[:7] for r in boardingPassList]
cols = [c[-3:] for c in boardingPassList]
# print(rows, cols)
maxVal = 0
idList = set()

for r, c in zip(rows, cols):
	rowVal = findVal(r)
	colVal = findVal(c)
	idList.add(rowVal * 8 + colVal)
	print(rowVal, colVal, (rowVal * 8) + colVal)
	maxVal = max(maxVal, ((rowVal * 8) + colVal))

print(idList)
ans = set([i for i in range(89, 990)]).difference(idList)
print(ans)