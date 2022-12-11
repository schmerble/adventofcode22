from enum import Enum

class plays(Enum):
    A = "Rock"
    B = "Paper"
    C = "Scissors"
    X = "Rock"
    Y = "Paper"
    Z = "Scissors"

class pointEval(Enum):
    Rock = 1
    Paper = 2
    Scissors = 3

class opposite(Enum):
    Rock = "Scissors"
    Scissors = "Paper"
    Paper = "Rock"

class outcome(Enum):
    Y = "draw"
    X = "lose"
    Z = "win"


def part1():
    openedFile = open('input.txt', 'r')
    allLines = openedFile.readlines()
    total = 0
    for line in allLines:
        elfChoice = line[0]
        myChoice = line[2]
        total += parse1(elfChoice, myChoice)
    print(total)

def part2():
    openedFile = open('input.txt', 'r')
    allLines = openedFile.readlines()
    total = 0
    for line in allLines:
        elfChoice = line[0]
        myChoice = line[2]
        total += parse2(elfChoice, myChoice)
    print(total)


def parse1(x, y):
    input = plays[y].value
    otherInput = plays[x].value
    score = 0
    match input:
        case "Rock":
            score += 1
        case "Paper":
            score += 2
        case "Scissors":
            score += 3
    if(otherInput == input):
        score += 3
    if(input == "Scissors" and otherInput == "Paper"):
        score += 6
    if(input == "Paper" and otherInput == "Rock"):
        score += 6
    if(input == "Rock" and otherInput == "Scissors"):
        score += 6
    return score

def parse2(x, y):
    outcomeY = outcome[y].value
    otherInput = plays[x].value
    score = 0
    match outcomeY:
        case "win":
            score += (6 + (pointEval[opposite[opposite[otherInput].value].value].value))
        case "draw":
            score += (3 + pointEval[otherInput].value)
        case "lose":
            score += pointEval[opposite[otherInput].value].value
    return score

if __name__ == '__main__':
    part2()
