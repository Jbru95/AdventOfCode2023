
fp = open('input.txt', 'r')

total = 0
total2 = 0

for line in fp.readlines():
    redCount = 0
    blueCount = 0
    greenCount = 0

    gameId = int(line.strip().split()[1][0:-1])

    roundArray = line.strip().split(':')[1].split(';')

    for round in roundArray:
        for count in round.split(','):
            cubeCount = int(count.split()[0])
            cubeColor = count.split()[1]

            if cubeColor == 'red' and cubeCount > redCount:
                redCount = cubeCount
            if cubeColor == 'blue' and cubeCount > blueCount:
                blueCount = cubeCount
            if cubeColor == 'green' and cubeCount > greenCount:
                greenCount = cubeCount
    
    if redCount < 13 and greenCount < 14 and blueCount < 15:
        total += gameId

    total2 += redCount * blueCount * greenCount

print(total)
print(total2)
