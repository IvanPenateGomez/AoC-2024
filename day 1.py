def part1():
    l = []
    r = []
    
    for line in open("day 1.txt").read().split("\n"):
        l.append(int(line.split()[0]))
        r.append(int(line.split()[1]))
    
    l.sort()
    r.sort()
    
    return sum(abs(l[i] - r[i]) for i in range(len(l)))

def part2():
    l = set()
    r = []
    
    for line in open("day 1.txt").read().split("\n"):
        l.add(int(line.split()[0]))
        r.append(int(line.split()[1]))
    
    return sum(a * r.count(a) for a in l)
   
print("Part 1:" ,part1())
print("Part 2:" ,part2())