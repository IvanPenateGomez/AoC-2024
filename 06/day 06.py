def moveForward(x,y,z,m):
    newX,newY = x,y
    if z == 0:
        newY -= 1
    elif z == 1:
        newX += 1
    elif z == 2:
        newY += 1
    else:
        newX -= 1
    
    if m[newY][newX] == "#":
        return x,y,(z+1)%4
    return newX,newY,z
    
    
def part1():
    m = list(open("day 6.txt",'r').read().split("\n"))
    history = [(x,y) for x in range(len(m[0])) for y in range(len(m)) if m[y][x] == "^"]
    z = 0
    while ((history[-1][0] > 0 and history[-1][0] < (len(m[0]) - 1)) and
            (history[-1][1] > 0) and history[-1][1] < (len(m) - 1)):
                x,y = history[-1]
                x,y,newZ = moveForward(x,y,z,m)
                if z == newZ:
                    history.append((x,y))
                z = newZ
    return len(set(history))

def part2():
    m = [list(line) for line in open("day 6.txt", 'r').read().split("\n")]
    directions = {0: (0, -1), 1: (1, 0), 2: (0, 1), 3: (-1, 0)}
    z = 0

    history = set((initialPos:=(x,y)) for x in range(len(m[0])) for y in range(len(m)) if m[y][x] == "^")

    x, y = initialPos
    while 0 < x < len(m[0]) - 1 and 0 < y < len(m) - 1:
        dx, dy = directions[z]
        newX, newY = x + dx, y + dy
        if m[newY][newX] == "#":
            z = (z + 1) % 4
        else:
            history.add((newX, newY))
            x, y = newX, newY

    counter = 0
    for x, y in history:
        m[y][x] = "#"
        currentX, currentY = initialPos
        z = 0
        visited = set()
        
        while 0 < currentX < len(m[0]) - 1 and 0 < currentY < len(m) - 1:
            dx, dy = directions[z]
            newX, newY = currentX + dx, currentY + dy
            
            if m[newY][newX] == "#":
                z = (z + 1) % 4
            else:
                if (newX, newY, z) in visited:
                    counter += 1
                    break
                visited.add((newX, newY, z))
                currentX, currentY = newX, newY
        
        m[y][x] = "."
    
    return counter


print("Part 1:" ,part1())
print("Part 2:" ,part2())