def parseIp(file):
	commandList = []
	with open(file, 'r') as ip:
		content = ip.readlines()
		for entry in content:
			cmd, val = entry.split()
			commandList.append((cmd, int(val)))
		return commandList

def impLogic(cmdList):
	acc = 0
	visited, i = set(), 0
	flag = True
	while i < len(cmdList):
		if i in visited:
			flag = False
			break
		tup = cmdList[i]
		if tup[0] == 'jmp':
			visited.add(i)
			i += tup[1]
		elif tup[0] == 'nop':
			visited.add(i)
			i += 1
		else:
			visited.add(i)
			i += 1
			acc += tup[1]
	return flag, acc


commandList = parseIp('input8.txt')
# impLogic(commandList)

# now the logic has to adabt to find exactly one instruct jmp/nop to flip 
# brute force way is to flip every command from beginnin and check which one completes
def impSwitchLogic(cmdList):
	swithc_idx = 0
	for i, tup in enumerate(cmdList):
		if tup[0] == 'jmp':
			flag, acc = impLogic(cmdList[:i] + [('nop', tup[1])] + cmdList[i+1:])
			if flag: print(acc)
		elif tup[0] == 'nop':
			flag, acc = impLogic(cmdList[:i] + [('jmp', tup[1])] + cmdList[i+1:])
			if flag: print(acc)
	print('WTF')

impSwitchLogic(commandList)