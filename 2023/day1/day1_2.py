def convert_num(num):
    if num == "one":
        num = 1
    elif num == "two":
        num = 2
    elif num == "three":
        num = 3
    elif num == "four":
        num = 4
    elif num == "five":
        num = 5
    elif num == "six":
        num = 6
    elif num == "seven":
        num = 7
    elif num == "eight":
        num = 8
    elif num == "nine":
        num = 9
    elif num == "zero":
        num = 0
    #End if

    return num
#End convert_num function

with open("input.txt", "r") as input_file:
	lines = input_file.readlines()
#End with

total = 0

for line in lines:
    num_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0",
                "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "zero"]

    num1_dict = {}
    num2_dict = {}

    for num in num_list:
        try:
            num1_dict[num] = line.index(num)
        except:
            pass
        #End try

        try:
            num2_dict[num] = line.rindex(num)
        except:
            pass
        #End try
    #End for

    num1 = convert_num(min(num1_dict, key=num1_dict.get))
    num2 = convert_num(max(num2_dict, key=num2_dict.get))

    total += int(str(num1) + str(num2))
#End for

print(total)
