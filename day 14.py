m, n = 101, 103

def part1():
    seconds = 100
    quadrants = [0, 0, 0, 0]
    
    for line in open("day 14.txt", 'r').read().split("\n"):
        p, v = line.split()
        x, y = map(int, p.split("=")[1].split(","))
        xs, ys = map(int, v.split("=")[1].split(","))

        x = (x + (xs * seconds)) % m
        y = (y + (ys * seconds)) % n

        if x == m // 2 or y == n // 2:
            continue

        if y < n // 2 and x < m // 2:
            quadrants[0] += 1
        elif y > n // 2 and x < m // 2:
            quadrants[1] += 1
        elif y < n // 2 and x > m // 2:
            quadrants[2] += 1
        elif y > n // 2 and x > m // 2:
            quadrants[3] += 1

    return quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3]

m, n = 101, 103

def part2():
    def printGraph(graph):
        for row in graph:
            print("".join(row))
        print("\n")

    robots = []
    for line in open("day 14.txt", 'r').read().split("\n"):
        p, v = line.split()
        x, y = map(int, p.split("=")[1].split(","))
        xs, ys = map(int, v.split("=")[1].split(","))
        robots.append([x, y, xs, ys])

    import time
    graph = [['.' for _ in range(m)] for _ in range(n)]  

    for counter in range(10000):
        if counter > 7500:
            print(f"Time: {counter}")
            printGraph(graph)
            time.sleep(0.25)
        graph = [['.' for _ in range(m)] for _ in range(n)] 

        for i in range(len(robots)):
            x, y, xs, ys = robots[i]
            x = (x + xs) % m
            y = (y + ys) % n
            
            graph[y][x] = "O"
            robots[i] = [x, y, xs, ys]  # Save updated robot position

print(part1())
part2()