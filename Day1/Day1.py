
total = 0

fp = open('day1Changed.txt', 'r')

for line in fp.readlines():
    strippedLine = line.strip()
    print(strippedLine)
    justNums = []

    for char in strippedLine: 
        if char.isdigit(): 
            justNums.append(char)

    firstAndLastString = justNums[0] + justNums[-1]

    print(firstAndLastString)

    total += int(firstAndLastString)

print(total)
fp.close()

# # 'one two three four five six seven eight nine'
# # oneight
# # threeight
# # nineight
# # fiveight
# # sevenine
# # eightwo
# # eighthree



