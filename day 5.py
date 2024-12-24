def goodOrder(arr, data):
    for i in range(len(arr)):
        e = arr[i]
        try:
            if not all(x not in arr[:i] for x in data[e]):
                return False
        except:
            continue
    return True

def part1():
    data = {}
    total = 0
    startOpp = False
    for line in open("day 5.txt",'r').read().split("\n"):
        if not startOpp:
            if "|" in line:
                a,b = line.split("|")
                if a in data.keys():
                    data[a].append(b)
                else:
                    data[a] = [b]
            elif line == "":
                startOpp=True
        else:
            a = line.split(",")
            if goodOrder(a,data):
                total += int(a[len(a)//2])
    return total

def getProblemIndex(arr, data):
    for i in range(len(arr)):
        e = arr[i]
        try:
            for x in range(len(data[e])):
                for y in range(len(arr[:i])):
                    if data[e][x] == arr[:i][y]:
                        return i , y
        except:
            continue
    return None, None

def fixOrder(arr, data):
    while True:
        a,b = getProblemIndex(arr,data)
        if a == None:
            return int(arr[len(arr)//2])
        
        arr = arr[:b] + [arr[a]] + arr[b + 1:a] + [arr[b]] + arr[a + 1:]

def part2():
    data = {}
    total = 0
    startOpp = False
    for line in open("day 5.txt",'r').read().split("\n"):
        if not startOpp:
            if "|" in line:
                a,b = line.split("|")
                if a in data.keys():
                    data[a].append(b)
                else:
                    data[a] = [b]
            elif line == "":
                startOpp=True
        else:
            a = line.split(",")
            if not goodOrder(a,data):
                total += fixOrder(a,data)
    return total

print("Part 1:" ,part1())
print("Part 2:" ,part2())