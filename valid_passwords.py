input = open("input2.txt", 'r')
arr = input.readlines()
correctPwdCount = 0
for item in [a.split() for a in  arr]:
	# since the item will always be three items, we can parse using index
	rangeLimit  = item[0].split('-')
	minLimit, maxLimit = rangeLimit[0], rangeLimit[1]
	charToLimit = item[1][0]
	password = item[2]
	# iterate password to check if it adheres to the limits
	count = password.count(charToLimit)
	# print(minLimit, maxLimit, charToLimit, password)
	# for c in password:
	# 	if c == charToLimit:
	# 		count+=1
	# 	if count > int(maxLimit):
	# 		break;
	if count >= int(minLimit) and count <= int(maxLimit):
		correctPwdCount += 1
	# print(minLimit, maxLimit, charToLimit, password, count, correctPwdCount)

# part two -- Each policy actually describes two positions in the password, 
# where 1 means the first character, 2 means the second character, and so on. 
# (Be careful; Toboggan Corporate Policies have no concept of "index zero"!) 
# Exactly one of these positions must contain the given letter. Other occurrences of the letter are irrelevant for the purposes of policy enforcement.
correctPwdCount_PartTwo = 0
for item in [a.split() for a in  arr]:
	# since the item will always be three items, we can parse using index
	rangeLimit  = item[0].split('-')
	firstPos, secondPos = int(rangeLimit[0]), int(rangeLimit[1])
	charToFind = item[1][0]
	password = item[2]
	count = 0
	for pos in [firstPos, secondPos]:
		if password[pos - 1] == charToFind:
			count += 1
	if count == 1:
		correctPwdCount_PartTwo += 1

print(correctPwdCount)
print(correctPwdCount_PartTwo)