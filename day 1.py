def part1():
    l = set()
    r = []
    
    for line in open("day 1.txt").read().split("\n"):
        l.add(int(line.split()[0]))
        r.append(int(line.split()[1]))
    
    return sum(a * r.count(a) for a in l)
        
print(part1())