#parse file
def parseFile(inputFile: str):
	input = open(inputFile, 'r')
	arr = [a for a in input.readlines()]
	# print(arr)
	passports = []
	passportEntry = []
	for entry in arr:
		if entry != '\n':
			passportEntry.append(entry)
		else:
			passports.append(passportEntry)
			passportEntry = []
	# append last entry to passports as well
	print(passportEntry)
	passports.append(passportEntry)
	print(arr.count('\n'))
	return passports

	# once we have list of lists of passports we need to extract maps from each passport


def parsePassports(passports: (list), validKeys = set):
	validPassportCount = 0
	for i, passport in enumerate(passports):
		currSet = set()
		passportMap = dict()
		for entry in passport:
			# print(entry)
			# check if entry has multiple key value pairs
			entries = entry.split()
			keyMap = {key: value for (key, value) in [kv.split(':') for kv in entries]}
			# print(keyList) # we actually don't care about the 
			currSet.update(keyMap.keys())
			passportMap.update(keyMap)
			
		if validKeys.issubset(currSet):
			if checkValues(passportMap):
				validPassportCount += 1
				print (i, passportMap, validPassportCount)
			# in part two we have to check value

		# else:
		# 	# print(currSet, validPassportCount)
	print(validPassportCount)
import re
def checkValues(passportDict):
	for key, value in passportDict.items():
		if key == 'byr' and int(value) >=1920 and int(value) <= 2002: continue
		elif key =='iyr' and int(value) >= 2010 and int(value) <= 2020: continue
		elif key == 'eyr' and int(value) >= 2010 and int(value) <= 2030: continue
		elif key == 'hgt':
			if value[-2:] == 'cm' and int(value[:-2]) >=150 and int(value[:-2]) <=193: 
				continue
			elif value[-2:] == 'in' and int(value[:-2]) >=59 and int(value[:-2]) <=76:
				continue
			else:
				return False
		elif key == 'hcl' and value[0] == '#' and len(value) == 7 and re.match('[0-9a-f]{6}', value[1:]): continue
		elif key == 'ecl' and value in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'): continue
		elif key == 'pid' and len(value) == 9: continue
		elif key == 'cid': continue # cause we need skip ut lol
		else: return False
	return True


passports = parseFile('input4.txt')
# print(passports)
requiredKeys = set(['byr', 'iyr', 'hgt', 'hcl', 'ecl', 'pid', 'eyr']) # cid not included cause it's optional
# print(requiredKeys)
parsePassports(passports, requiredKeys)