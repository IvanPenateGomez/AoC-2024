def countClusters(mapping, seen, tComp, a):
    tempTotal = 0
    for comp, b in mapping.items():
        if comp == tComp or tComp not in b:continue
        for c in a.intersection(b):
            if c in mapping[tComp] and c in mapping[comp]:
                trip = frozenset([tComp, comp, c])
                if trip not in seen:
                    seen.add(trip)
                    tempTotal += 1
    return tempTotal
                    
def part1():
    mapping = {}
    for line in open("day 23.txt", 'r').read().split("\n"):
        a, b = line.split("-")
        if a not in mapping: mapping[a] = set()
        if b not in mapping: mapping[b] = set()
        mapping[a].add(b)
        mapping[b].add(a)

    seen = set()
    return sum(countClusters(mapping, seen, tComp, connections) 
               for tComp, connections in mapping.items() if tComp.startswith('t'))

print(part1())

import networkx as nx
def part2():
    mapping = nx.Graph()
    for line in open("day 23.txt",'r').read().split("\n"):
        a, b = line.split("-")
        mapping.add_edge(a, b)
    
    cluster = max(list(nx.find_cliques(mapping)),key=len)
    return ",".join(sorted(cluster))

print("Part 1:", part1())
print("Part 2:", part2())