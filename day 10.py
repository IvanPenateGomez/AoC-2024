DIRECTIONS = ((0, 1), (1, 0), (-1, 0), (0, -1))

def findEnds(x, y, arr, seen):
    current = arr[y][x]
    seen.add((y, x))
    
    if current == 9:
        return 1

    total = 0
    for dx, dy in DIRECTIONS:
        ny, nx = y + dy, x + dx
        if (
            0 <= ny < len(arr) and 0 <= nx < len(arr[0]) and 
            (arr[ny][nx] == current + 1) and 
            (ny, nx) not in seen
        ):
            total += findEnds(nx, ny, arr, seen)
    
    return total
        
    

def findEndsPart2(x, y, arr, seen):
    current = arr[y][x]
    seen.add((y, x))
    
    if current == 9:
        seen.remove((y, x))
        return 1

    total = 0
    for dx, dy in DIRECTIONS:
        ny, nx = y + dy, x + dx
        if (
            0 <= ny < len(arr) and 0 <= nx < len(arr[0]) and 
            (arr[ny][nx] == current + 1) and 
            (ny, nx) not in seen
        ):
            total += findEndsPart2(nx, ny, arr, seen)
    seen.remove((y, x))
    return total

def part1():
    with open("day 10.txt", 'r') as f:
        arr = [list(map(int, line.strip())) for line in f if line.strip()]

    starting = [(x, y) for y in range(len(arr)) for x in range(len(arr[0])) if arr[y][x] == 0]
    
    return sum(findEnds(x, y, arr, set()) for x,y in starting)

def part2():
    with open("day 10.txt", 'r') as f:
        arr = [list(map(int, line.strip())) for line in f if line.strip()]

    starting = [(x, y) for y in range(len(arr)) for x in range(len(arr[0])) if arr[y][x] == 0]
    
    return sum(findEndsPart2(x, y, arr, set()) for x,y in starting)


print("Part 1:", part1())
print("Part 2:", part2())