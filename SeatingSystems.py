def parseInput(file):
	with open(file, 'r') as ip:
		contents = ip.readlines()
		arr = [[item.rstrip()] for item in contents]
		print(len(arr))


arr = parseInput('input11.txt')