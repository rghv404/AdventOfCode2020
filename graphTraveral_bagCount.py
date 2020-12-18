def parseIp(file):
	bagMap = dict()
	with open(file, 'r') as ip:
		content = ip.readlines()
		for entry in content:
			mapEntrySet = entry.rstrip().split('contain')
			mapKey, mapVal = mapEntrySet[0].rstrip().rstrip('s'), [bag.strip().rstrip('.').rstrip('s')[2:] for bag in mapEntrySet[1].split(',') if bag.strip() != 'no other bags.'] # 2: cause we don't care abotu the number
			# print(mapKey, mapVal)
			bagMap[mapKey] = mapVal
	return bagMap

def parseIpWithCount(file):
	bagMap = dict()
	with open(file, 'r') as ip:
		content = ip.readlines()
		for entry in content:
			mapEntrySet = entry.rstrip().split(' contain ')
			mapKey, mapVal = mapEntrySet[0].rstrip('s'), [bag.strip().rstrip('.').rstrip('s') for bag in mapEntrySet[1].split(',') if bag.strip() != 'no other bags.'] # 2: cause we don't care abotu the number
			bagMap[mapKey] = [(int(bag[0]), bag[2:]) for bag in mapVal]
			print(mapKey, bagMap[mapKey])
	return bagMap

bagMap = parseIp('input7.txt')

def impLogic():
	bagMap = parseIp('input7.txt')
	deadEnds = set()
	count = 0
	def dfs(bag: str):
		if bag == 'shiny gold bag': 
			return True
		if 'shiny gold bag' in bagMap[bag]:
		 	return True
		count = 0
		for item in bagMap[bag]:
			# print(bag, count)
			if item in deadEnds:
				# add bag to dead end as well
				continue
			else:
				if dfs(item):
					count += 1
				else:
					deadEnds.add(item)
			# if dfs(item): count += 1
		return count


	print(bagMap)
	for key, val in bagMap.items():
		if key != 'shiny gold bag':
			print(key, count)
			if dfs(key) > 0:
				count += 1
	print(count)
	print(deadEnds)

def impLogicPartTwo():
	bagMap = parseIpWithCount('input7.txt')
	def dfs(bag):
		ans = 1
		for count, currBag in bagMap[bag]:
			# print(count, currBag, ans)
			ans += count*dfs(currBag)
			# print(count, currBag, ans)
		return ans
	res = dfs("shiny gold bag")
	print(res - 1)

# impLogic()
impLogicPartTwo()