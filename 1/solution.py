import heapq

def part1():
    tempArray = []
    openedFile = open('input.txt', 'r')
    allLines = openedFile.readlines()
    total = 0
    for line in allLines:
        if line == "\n":
            tempArray.append(total)
            total = 0
        else:
            total+= int(line)
    heapq.heapify(tempArray)
    print(heapq.nlargest(1, tempArray))

def part2():
    tempArray = []
    openedFile = open('input.txt', 'r')
    allLines = openedFile.readlines()
    total = 0
    for line in allLines:
        if line == "\n":
            tempArray.append(total)
            total = 0
        else:
            total+= int(line)
    heapq.heapify(tempArray)
    print(sum(heapq.nlargest(3, tempArray)))


if __name__ == '__main__':
    part2()
