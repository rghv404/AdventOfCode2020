input = open("input3.txt", 'r')
arr = [a.rstrip() for a in input.readlines()]
# trying to find 3 right and down 1 basically means going three to right in current string and then checking next string at same pos where it is tree or not

repeatAfter = len(arr[0]) - 1
treeCountProduct = 1
for (stepValue, downStep) in [(1,1), (3,1), (5,1), (7,1), (1,2)]:
	treeCount, rightStep = 0, -stepValue
	for i in range(0,len(arr), downStep):
		road = arr[i]
		rightStep += stepValue
		if rightStep > repeatAfter:
			rightStep = rightStep - repeatAfter - 1
		if road[rightStep] == '#':
			treeCount += 1
		# print(currStep, i, repeatAfter, treeCount)
	treeCountProduct *= treeCount
	print(treeCount)
print(treeCountProduct)

