def parseIp(file):
	with open(file, 'r') as ip:
		content = ip.readlines()
	return [int(item.rstrip()) for item in content]

arr = parseIp('input9.txt')

def impLogic(arr, window):
	left, right = 0, window
	while right < len(arr):
		flag = False
		for i in range(left, right):
			tgt = abs(arr[right] - arr[i])
			tgtArray = arr[left:i] + arr[i+1:right]
			# print(tgtArray, arr[right], tgt)
			if tgt in tgtArray:
				flag = True
				break
		if not flag: return arr[right]
		left += 1
		right += 1

res = impLogic(arr, 25)
print(res)

# get sum of contiguous sub array that matches above result
def impLogic2(arr, k):
	left, right = 0, arr.index(k)
	while left < right:
		idx = left + 1
		currSum = arr[left]
		while currSum + arr[idx] <= k:
			currSum += arr[idx]
			idx += 1
		if currSum == k:
			return arr[left: idx]
		left += 1


res2 = impLogic2(arr, res)
print(min(res2) + max(res2))