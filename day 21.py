NUMPAD = [
    [7,8,9],
    [4,5,6],
    [1,2,3],
    [None, 0, 10]
]

numPadPosition = {
    7:(0,0),
    8:(0,1),
    9:(0,2),
    
    4:(1,0),
    5:(1,1),
    6:(1,2),
    
    1:(2,0),
    2:(2,1),
    3:(2,2),
    
    None : (3,0),
    0:(3,1),
    'A':(3,2)
}

KEYPAD = [
    [None, '^' , 'A'],
    ['<', 'v', '>']
]

keyPadPosition = {
    '<': (1,0), 
    'v': (1,1), 
    '>': (1,2),
    '^': (0,1),
    'A': (0,2),
    None : (0,0)
}

def getNumPad(string):
    currentPos = numPadPosition['A']
    out = ""
    for symbol in string:
        try:getPos = numPadPosition[int(symbol)]
        except:getPos = numPadPosition[symbol]

        lt, rt = '<' * (currentPos[1] - getPos[1]), '>' * (getPos[1] - currentPos[1])
        up, dn = '^' * (currentPos[0] - getPos[0]), 'v' * (getPos[0] - currentPos[0])

        if (min(currentPos[0],getPos[0]) == numPadPosition[None][0]) and (max(currentPos[1],getPos[1]) == numPadPosition[None][1]):
            out += dn + rt + up + lt
        elif (max(currentPos[0],getPos[0]) == numPadPosition[None][0]) and (min(currentPos[1],getPos[1]) == numPadPosition[None][1]):
            out += up + rt + dn + lt
        else:
            out += lt + dn + up + rt 

        out += "A"
        currentPos = getPos
    return out

def getKeyPad(string):
    currentPos = keyPadPosition['A']
    out = ""
    for symbol in string:
        try:getPos = keyPadPosition[int(symbol)]
        except:getPos = keyPadPosition[symbol]
                
        lt, rt = '<' * (currentPos[1] - getPos[1]), '>' * (getPos[1] - currentPos[1])
        up, dn = '^' * (currentPos[0] - getPos[0]), 'v' * (getPos[0] - currentPos[0])

        if (min(currentPos[0],getPos[0]) == numPadPosition[None][0]) and (max(currentPos[1],getPos[1]) == numPadPosition[None][1]):
            out += dn + rt + up + lt
        elif (max(currentPos[0],getPos[0]) == numPadPosition[None][0]) and (min(currentPos[1],getPos[1]) == numPadPosition[None][1]):
            out += up + rt + dn + lt
        else:
            out += lt + dn + up + rt 

        out += "A"
        currentPos = getPos
    return out

def part1():
    total = 0
    for line in open("day 21.txt", 'r').read().split("\n"):
        it1 = getNumPad(line)
        it2 = getKeyPad(it1)
        it3 = getKeyPad(it2)
        print(len(it3))
        total += len(it3) * int(line[:-1])
    
    return total

def part2():
    cache = dict()
    total = 0
    
    for line in open("day 21.txt", 'r').read().split("\n"):
        if not line.strip():
            continue
        
        it1 = getNumPad(line)
        
        for x in range(25):
            l = 0
            temp = []
            is_stable = True
            
            for subString in it1[:-1].split("A"):
                if subString in cache:
                    sub, sub_len = cache[subString]
                    l += sub_len
                    temp.append(sub)
                    is_stable = False
                else:
                    sub = getKeyPad(subString + 'A')
                    sub_len = len(sub)
                    cache[subString] = (sub, sub_len)
                    l += sub_len
                    temp.append(sub)
                    is_stable = False
            
            it1 = "".join(temp)
            
            if is_stable:break
        
        total += l * int(line[:-1])
    
    return total


print(part2())