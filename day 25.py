def getValue(graph):
    keys = [-1 for _ in range(5)]
    
    if "." in graph[0]:
        for x in range(len(graph[0])):
            for y in range(len(graph) - 1):
                if graph[y][x] != graph[y + 1][x]:
                    keys[x] = 6 - (y + 1)
                    break
        return keys,True 
    else:
        for x in range(len(graph[0])):
            for y in range(len(graph) - 1):
                if graph[y][x] != graph[y + 1][x]:
                    keys[x] = y
                    break
        return keys,False

def valid(kA,kB):
    for i in range(len(kA)):
        if kA[i] + kB[i] >= 6:
            return False
    return True

def part1():
    locks = []
    keys = []
    
    temp = []
    for line in open("day 25.txt",'r').read().split("\n"):
        if line == "":
            val,isKey = getValue(temp)
            if isKey: keys.append(val)
            else:locks.append(val)
            temp = []
        else:
            temp.append(line)
    
    total = 0
    for a in range(len(locks)):
        for b in range(len(keys)):
            if valid(locks[a],keys[b]):
                total += 1
    return total

print(valid([0,5,3,4,3],[3,0,2,0,1]))
print("Part 1:", part1())