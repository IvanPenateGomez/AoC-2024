from collections import defaultdict

NUMPAD = [
    [7, 8, 9],
    [4, 5, 6],
    [1, 2, 3],
    [None, 0, 10]
]

numPadPosition = {
    '7': (0, 0), '8': (0, 1), '9': (0, 2),
    '4': (1, 0), '5': (1, 1), '6': (1, 2),
    '1': (2, 0), '2': (2, 1), '3': (2, 2),
    None: (3, 0), '0': (3, 1), 'A': (3, 2)
}

KEYPAD = [
    [None, '^', 'A'],
    ['<', 'v', '>']
]

keyPadPosition = {
    '<': (1, 0), 'v': (1, 1), '>': (1, 2),
    '^': (0, 1), 'A': (0, 2), None: (0, 0)
}

hardCodedPaths = dict([(('A','^'),'<A'),
                        (('A','>'),'vA'),
                        (('A','v'),'<vA'),
                        (('A','<'),'v<<A'),
                        (('^','A'),'>A'),
                        (('^','>'),'v>A'),
                        (('^','<'),'v<A'),
                        (('^','v'),'vA'),
                        (('v','A'),'^>A'),
                        (('v','>'),'>A'),
                        (('v','<'),'<A'),
                        (('v','^'),'^A'),
                        (('>','A'),'^A'),
                        (('>','^'),'<^A'),
                        (('>','v'),'<A'),
                        (('>','<'),'<<A'),
                        (('<','A'),'>>^A'),
                        (('<','^'),'>^A'),
                        (('<','v'),'>A'),
                        (('<','>'),'>>A')])

def getNumPad(string):
    currentPos = numPadPosition['A']
    out = []
    
    for symbol in string:
        getPos = numPadPosition.get(symbol)

        lt, rt = '<' * (currentPos[1] - getPos[1]), '>' * (getPos[1] - currentPos[1])
        up, dn = '^' * (currentPos[0] - getPos[0]), 'v' * (getPos[0] - currentPos[0])

        if (min(currentPos[0], getPos[0]) == numPadPosition[None][0]) and (max(currentPos[1], getPos[1]) == numPadPosition[None][1]):
            out.append(dn + rt + up + lt)
        elif (max(currentPos[0], getPos[0]) == numPadPosition[None][0]) and (min(currentPos[1], getPos[1]) == numPadPosition[None][1]):
            out.append(up + rt + dn + lt)
        else:
            out.append(lt + dn + up + rt)

        out.append("A")
        currentPos = getPos

    return ''.join(out)

def getKeyPad(newStrings, string,count):
    currentPos = 'A'   
    for symbol in string:
        if currentPos == symbol:out = 'A'
        else:out = hardCodedPaths[(currentPos,symbol)]
        
        if out in newStrings: newStrings[out] += count
        else: newStrings[out] = count
        currentPos = symbol

def part1():
    total = 0
    for line in open("day 21.txt", 'r').read().split("\n"):
        it1 = getNumPad(line)

        string = dict()
        for subString in it1[:-1].split("A"):    
            if (subString + 'A') in string: string[subString + 'A'] += 1
            else: string[subString + 'A'] = 1

        for x in range(2):
            newString = dict()           
            for s,count in string.items():
                getKeyPad(newString,s,count)

            string = newString.copy()
        
        total += sum(len(s) * c for s,c in string.items()) * int(line[:-1])
    return total

def part2():
    total = 0
    for line in open("day 21.txt", 'r').read().split("\n"):
        it1 = getNumPad(line)

        string = dict()
        for subString in it1[:-1].split("A"):    
            if (subString + 'A') in string: string[subString + 'A'] += 1
            else: string[subString + 'A'] = 1

        for x in range(25):
            newString = dict()           
            for s,count in string.items():
                getKeyPad(newString,s,count)

            string = newString.copy()
        
        total += sum(len(s) * c for s,c in string.items()) * int(line[:-1])
    return total

print(part1())
print(part2())