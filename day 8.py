N = 50

def getAntiNodes(ax):
    newAntiNodes = set()
    for (i, j) in ax:
        for (u, v) in ax:
            if (u, v) == (i, j):
                continue

            diffY, diffX = u - i, v - j
            candidate1 = (u,v)
            newAntiNodes.add(candidate1)

            while True:
                candidate1 = (candidate1[0] + diffY, candidate1[1] + diffX)
                if 0 <= candidate1[0] < N and 0 <= candidate1[1] < N:
                    newAntiNodes.add(candidate1)
                else:
                    break

            candidate2 = (i,j)
            newAntiNodes.add(candidate2)

            while True:
                candidate2 = (candidate2[0] - diffY, candidate2[1] - diffX)
                if 0 <= candidate2[0] < N and 0 <= candidate2[1] < N:
                    newAntiNodes.add(candidate2)
                else:
                    break

    return newAntiNodes


def part1():
    m = []
    antennas = dict()
    with open("day 8.txt", 'r') as file:
        i = 0
        for line in file:
            j = 0
            newRow = []
            for x in line.replace("\n",""):
                if x != ".":
                    try: antennas[x].append((i,j))
                    except: antennas[x] = [(i,j)]
                
                newRow.append(x)
                j+=1
            m.append(newRow)
            i+=1

    antiNodes = set()
    for v in antennas.values():
        antiNodes = antiNodes.union(getAntiNodes(v))

    return len(antiNodes)

#print("Part 1:", part1())
print("Part 2:", part1())