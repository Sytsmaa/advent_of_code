with open("input.txt", "r") as input_file:
	lines = input_file.readlines()
#End with

total = 0

for line in lines:
	num1 = 0

	for num in line:
		if num.isnumeric():
			num1 = num
			break
		#End if
	#End for

	num2 = 0

	for num in reversed(line):
		if num.isnumeric():
			num2 = num
			break
		#End if
	#End for

	total += int(str(num1) + str(num2))
#End for

print(total)
