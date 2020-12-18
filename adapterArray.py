def parseIp(file):
	with open(file, 'r') as ip:
		content = ip.readlines()
	return [int(item.rstrip()) for item in content]

res = parseIp('input10.txt')
res = sorted(res)
res = [0] + res + [max(res) + 3]

one, three = 0, 0
for i in range(len(res) - 1):
	first, second = res[i], res[i+1]
	diff = second - first
	
	if diff == 1: one += 1
	elif diff == 3: three += 1
	else: print("WTF")

print(one*three)	
import math
def impLogic2(res):
	i = 0
	count_three = 0
	count_two = 0
	while i < len(res) - 3:	
		if res[i+3] == res[i] + 3:
			count_three += 1
		elif res[i+2] == res[i] + 2:
			print(i, res)
			count_two += 1
		i += 1
	print(count_two, count_three)
	print(count_two*2 * count_three*6)

impLogic2(res)

def impLogic3(jolts):
	joltMap = {jolts[-1] : 1, jolts[-2] : 1, jolts[-3] : 1}
	for i in range(len(jolts) - 4, -1, -1):
		print(i)
		combos = joltMap[jolts[i+1]] #You know the next adapter will fit
		if jolts[i+3] - jolts[i] <= 3:
			combos += joltMap[jolts[i+2]] + joltMap[jolts[i+3]]
		elif jolts[i+2] - jolts[i] <= 3:
			combos += joltMap[jolts[i+2]]
		joltMap[jolts[i]] = combos
	print(joltMap[0])

impLogic3(res)