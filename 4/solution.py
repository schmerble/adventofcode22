def main():
    openedFile = open('input.txt', 'r')
    allLines = openedFile.readlines()
    total = 0
    for line in allLines:
        string1 = line[:line.index(',')]
        string2 = line[line.index(',') + 1:]
        if(parse(string1, string2)):
            total+=1
    print(total)



def parse(string1, string2):
    i = int(string1[:string1.index('-')])
    end = int(string1[string1.index('-')+1:])
    firstString = set()
    secondString = set()
    while(i <= end):
        firstString.add(i)
        i+=1
    i2 = int(string2[:string2.index('-')])
    end2 = int(string2[string2.index('-')+1:])
    while(i2 <= end2):
        secondString.add(i2)
        i2+=1
    if(firstString.intersection(secondString) == secondString or secondString.intersection(firstString) == firstString):
        return True
    #if(len(firstString.intersection(secondString)) > 0):
    #    return True
    # uncomment if require solution for part 2
    return False


if __name__ == "__main__":
    main()