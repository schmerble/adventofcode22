import math


def part1():
    openedFile = open('input.txt', 'r')
    allLines = openedFile.readlines()
    total = 0
    for lines in allLines:
        commonItem = parseString(lines)
        for x in commonItem:
            total += convertToPriority(x)
    print(total)

def part2():
    openedFile = open('input.txt', 'r')
    allLines = openedFile.readlines()
    total = 0
    i = 0
    while(i < len(allLines)):
        commonItem = parseString2(allLines[i], allLines[i+1], allLines[i+2])
        commonItem.discard("\n")
        for x in commonItem:
            total += convertToPriority(x)
        i+=3
    print(total)

def parseString(lines):
    charSetF = set()
    charSetS = set()
    firstHalf = lines[0: math.floor(len(lines) / 2)]
    secondHalf = lines[math.floor(len(lines)/2):]
    for char in firstHalf:
        charSetF.add(char)
    for char in secondHalf:
        charSetS.add(char)
    return charSetF.intersection(charSetS)

def parseString2(line1, line2, line3):
    set1 = set()
    set2 = set()
    set3 = set()
    for char in line1:
        set1.add(char)
    for char in line2:
        set2.add(char)
    for char in line3:
        set3.add(char)
    return set1.intersection(set2, set3)

def convertToPriority(data):
    asciiNum = ord(data)
    if(asciiNum >= 65 and asciiNum <= 91):
        return asciiNum - 38
    return asciiNum - 96



if __name__ == "__main__":
    part2()