input = open('./input1.txt', 'r')
arr = [int(a) for a in input.readlines()]

# begins actual logic
for elem in arr:
	if (2020 - elem) in arr:
		print (elem * (2020 - elem))

# find three entries
for i, one in enumerate(arr):
	for j, two in enumerate(arr[i+1:]):
		target = 2020 - (arr[i] + arr[j])
		if target in arr[j+1:]:
			print(arr[i] * arr[j] * target)