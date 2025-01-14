DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)] # east, south, west, north

import heapq

def dijkstra(arr, start):
    priority_queue = [(0, start)]
    distances = {(x, y): float('inf') for y in range(len(arr)) for x in range(len(arr[0])) if arr[y][x] != "#"}
    distances[start] = 0

    while priority_queue:
        current_cost, (x, y) = heapq.heappop(priority_queue)

        if current_cost > distances[(x, y)]:
            continue

        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy

            if not (0 <= ny < len(arr) and 0 <= nx < len(arr[0])) or arr[ny][nx] == "#":
                continue

            new_cost = current_cost + 1
            if new_cost < distances[(nx, ny)]:
                distances[(nx, ny)] = new_cost
                heapq.heappush(priority_queue, (new_cost, (nx, ny)))

    return distances

def part1():
    arr = [list(line) for line in open("day 20.txt",'r').read().split("\n")]
    
    s = [(x,y) for y in range(len(arr)) for x in range(len(arr[0])) if arr[y][x] == "S"][0]

    distances = dijkstra(arr,s)
    counter = 0
    for ((x,y), distA) in distances.items():
        for ((s,t),distB) in distances.items():
            if (s,t) == (x,y): continue
            
            dist = abs(x - s) + abs(y - t)
            if dist <= 2 and distB - distA - dist >= 100:
                counter += 1
            
    return counter

def part2():
    arr = [list(line) for line in open("day 20.txt",'r').read().split("\n")]
    
    s = [(x,y) for y in range(len(arr)) for x in range(len(arr[0])) if arr[y][x] == "S"][0]

    distances = dijkstra(arr,s)
    counter = 0
    for ((x,y), distA) in distances.items():
        for ((s,t),distB) in distances.items():
            if (s,t) == (x,y): continue
            
            dist = abs(x - s) + abs(y - t)
            if dist <= 20 and distB - distA - dist >= 100:
                counter += 1
            
    return counter


print("Part 1:", part1())
print("Part 2:", part2())