input = open('input6.txt', 'r')
with open('input6.txt', 'r') as input:
	content = input.readlines()
	group = []
	groups = []
	# print(content)
	for item in content:
		if item != '\n':
			group.append(item.rstrip())
		else:
			groups.append(group)
			group = []
	# append last item
	groups.append(group)
# print(groups)

def countAnswers(arr):
	totalAns = 0
	for group in groups:
		groupAns = ''.join(group)
		totalAns += len(set(groupAns))
	print(totalAns)

from functools import reduce

def countAnsweredByAll(arr):
	count = 0
	# find count fo commong elemet in list of strings
	for group in groups:
		itemSet = [set(item) for item in group]
		count += len(list(reduce(lambda i, j: i & j, (item for item in itemSet))))
	print(count)

print(groups[0])

countAnswers(groups)
countAnsweredByAll(groups)