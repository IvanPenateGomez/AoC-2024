N,M = 71,71

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
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
            if (not (0<=ny<N and 0<=nx<M)) or arr[ny][nx] == "#":continue
            
            
            new_cost = current_cost + 1
            if new_cost < distances[(nx,ny)]:
                distances[(nx,ny)] = new_cost
                heapq.heappush(priority_queue, (new_cost, (nx,ny),i))

    return distances


def part1():
    arr = [['.' for _ in range(M)] for _ in range(N)]
    
    count = 0
    for line in open("day 18.txt",'r').read().split("\n"):
        x,y = map(int, line.split(","))
        arr[y][x] = "#"
        count += 1
        if count == 12:
            break
            
    
    return dijkstra(arr,(0,0))[(N-1,M-1)]


def dijkstra2(arr, start, target):
    priority_queue = [(0, start)]
    visited = set()
    distances = {(x, y): float('inf') for x in range(len(arr[0])) for y in range(len(arr)) if arr[y][x] != "#"}
    previous = {}
    distances[start] = 0

    while priority_queue:
        current_cost, current_node = heapq.heappop(priority_queue)

        if current_node in visited:
            continue

        visited.add(current_node)

        if current_node == target:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = previous.get(current_node, None)
            return path[::-1]

        x, y = current_node
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if not (0 <= ny < len(arr) and 0 <= nx < len(arr[0])) or arr[ny][nx] == "#":
                continue

            new_cost = current_cost + 1
            if new_cost < distances[(nx, ny)]:
                distances[(nx, ny)] = new_cost
                previous[(nx, ny)] = current_node
                heapq.heappush(priority_queue, (new_cost, (nx, ny)))

    return None


def part2():
    arr = [['.' for _ in range(M)] for _ in range(N)]
    flag = True
    count = 0
    for line in open("day 18.txt",'r').read().split("\n"):
        x,y = map(int, line.split(","))
        arr[y][x] = "#"
        if flag:
            count += 1
            if count == 1024:
                flag = not flag
        else:
            newPath = dijkstra2(arr,(0,0),(N-1,M-1))
            if not newPath:
                return x,y

print(part2())