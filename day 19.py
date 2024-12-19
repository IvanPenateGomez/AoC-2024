def valid(pattern, patterns):
    possible = [0]
    visited = set()
    while possible:
        pos = possible.pop(0)
        if pos in visited:
            continue
        visited.add(pos)
        for i in range(len(pattern), pos, -1):
            if pattern[pos:i] in patterns:
                if i == len(pattern):
                    return True
                possible.append(i)
    return False

def part1():
    file = open("day 19.txt",'r')
    patterns = set(file.readline().replace(" ",'').replace("\n",'').split(","))
    
    file.readline()
    
    validCount = 0
    for logo in file:
        if valid(logo.strip(),patterns):
            validCount += 1
    
    return validCount

def getArrangements(pattern, patterns):
    global cache
    if pattern in cache: return cache[pattern]
    if not pattern: return 1

    cache[pattern] = sum(
        getArrangements(pattern[i:], patterns) 
            for i in range(1,len(pattern) + 1) 
                if pattern[:i] in patterns)
    
    return cache[pattern]

cache = dict()
def part2():
    file = open("day 19.txt",'r')
    patterns = set(file.readline().strip().replace(" ", "").split(","))
    file.readline()
    return sum(getArrangements(logo.strip(), patterns) for logo in file if valid(logo.strip(), patterns))

print(part2())