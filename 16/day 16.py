DIRECTIONS = ((1,0), (0, 1), (-1, 0), (0, -1))
import heapq

def dijkstra(arr, start):
    priority_queue = [(0, start,0)]
    visited = set()
    distances = {(x,y): float('inf') for x in range(len(arr[0])) for y in range(len(arr)) if arr[y][x] != "#"}
    distances[start] = 0

    while priority_queue:
        current_cost, current_node , prevDir= heapq.heappop(priority_queue)

        if current_node in visited:
            continue

        visited.add(current_node)
        x,y = current_node
        for i in range(4):
            nx,ny = x+DIRECTIONS[i][0],y+DIRECTIONS[i][1]
            if arr[ny][nx] == "#":continue
            
            if abs(abs(prevDir) - i) == 1 or (prevDir == 3 and i == 0) or (prevDir == 0 and i == 3):
                new_cost = current_cost + 1001
            elif abs(abs(prevDir) - i) == 0:
                new_cost = current_cost + 1
            if new_cost < distances[(nx,ny)]:
                distances[(nx,ny)] = new_cost
                heapq.heappush(priority_queue, (new_cost, (nx,ny),i))

    return distances

def part1():
    arr = []
    for line in open("day 16.txt", 'r').read().split("\n"):
        arr.append(line)
            
    sx,sy = [(x,y) for x in range(len(arr[0])) for y in range(len(arr)) if arr[y][x] == "S"][0]
    ex,ey = [(x,y) for x in range(len(arr[0])) for y in range(len(arr)) if arr[y][x] == "E"][0]

    distances = dijkstra(arr,(sx,sy))     
    return distances[(ex,ey)]

def dijkstra2(grid, start):
    pq = [(0, start[0], start[1], 0)]
    dist = {}
    prev = {}

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] != "#":
                for d in range(4): 
                    dist[(x, y, d)] = float('inf')
                prev[(x, y)] = set()

    dist[(start[0], start[1], 0)] = 0 
    
    while pq:
        cost, x, y, dir_prev = heapq.heappop(pq)

        if dist[(x, y, dir_prev)] < cost:
            continue

        for d in range(4): 
            nx, ny = x + DIRECTIONS[d][0], y + DIRECTIONS[d][1]

            if not (0 <= nx < len(grid[0]) and 0 <= ny < len(grid)): continue
            if grid[ny][nx] == "#": continue

            if dir_prev == d:
                new_cost = cost + 1
            elif abs(dir_prev - d) == 1 or (dir_prev == 3 and d == 0) or (dir_prev == 0 and d == 3):
                new_cost = cost + 1001

            if new_cost < dist[(nx, ny, d)]:
                dist[(nx, ny, d)] = new_cost
                prev[(nx, ny, d)] = {(x, y, dir_prev)}
                heapq.heappush(pq, (new_cost, nx, ny, d))
            elif new_cost == dist[(nx, ny, d)]:
                prev[(nx, ny, d)].add((x, y, dir_prev))

    return dist, prev

def count_reachable_nodes(prev_nodes, end_node):
    stack = [end_node]
    visited = set(stack)

    while stack:
        node = stack.pop()
        for neighbor in prev_nodes.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)
    return len(set((x, y) for x, y, _ in visited)) 

def part2():
    arr = []
    for line in open("day 16.txt", 'r').read().split("\n"):
        arr.append(list(line))
    
    sx, sy = [(x, y) for x in range(len(arr[0])) for y in range(len(arr)) if arr[y][x] == "S"][0]
    ex, ey = [(x, y) for x in range(len(arr[0])) for y in range(len(arr)) if arr[y][x] == "E"][0]

    distances, prev_nodes = dijkstra2(arr, (sx, sy))

    min_distance = min(distances[(ex, ey, d)] for d in range(4))

    return count_reachable_nodes(prev_nodes, (ex, ey, 0)) - 1

print("Part 1:", part1())
print("Part 2:", part2())