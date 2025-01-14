def addValue(graph,a,b,c,operation):
    match operation:
        case 'OR':
            graph[c] = graph[a] or graph[b]
        case 'AND':
            graph[c] = graph[a] and graph[b]
        case 'XOR':
            graph[c] = graph[a] ^ graph[b]

def solve(rules, graph) -> int:
    pendingRules = []
    for _,a,b,c,operation in rules:
        try:addValue(graph,a,b,c,operation)
        except:pendingRules.append((a,operation,b,c))
        
    while pendingRules:
        a,operation,b,c = pendingRules.pop(0)
        try:addValue(graph,a,b,c,operation)
        except:pendingRules.append((a,operation,b,c))

    zValues = []
    for k,v in graph.items():
        if k.startswith('z'):
            zValues.append((k,v))

    total = 0
    counter = 0
    for _,v in sorted(zValues):
        total += (2**counter) * v
        counter += 1
    return total

def part1():
    graph = dict()
    isRule = False
    rules = []
    counter = 0
    for line in open('day 24.txt','r').read().split("\n"):
        if line == "":
            isRule = True
            continue
            
        if isRule:
            a,operation,b,_,c = line.split()
            rules.append([counter,a,b,c,operation])
            counter += 1
        else:
            a,value = line.split(":")
            graph[a] = value == " 1"
    return solve(rules, graph)


from itertools import combinations
def part2():
    graph = dict()
    isRule = False
    rules = []
    counter = 0
    for line in open('day 24.txt','r').read().split("\n"):
        if line == "":
            isRule = True
            continue
            
        if isRule:
            a,operation,b,_,c = line.split()
            rules.append([counter,a,b,c,operation])
            counter += 1
        else:
            a,value = line.split(":")
            graph[a] = value == " 1"
    
   
    xCounter = 0
    yCounter = 0
    yTotal = 0
    xTotal = 0
    for k,v in graph.items():
        if k.startswith('x'):
            xTotal += (2**xCounter) * v
            xCounter += 1
        else:
            yTotal += (2**yCounter) * v
            yCounter += 1
    expected = yTotal + xTotal
    
    for r1,r2 in combinations(rules,2):
        prevR1 = r1[3]
        prevR2 = r2[3]
        rules[r1[0]][3] = r2[3]
        rules[r2[0]][3] = prevR1
        
        for r3,r4 in combinations(rules,2):
            if (r3[3] == prevR1 or r3[3] == prevR2 or
                r4[3] == prevR1 or r4[3] == prevR2):
                continue
            prevR3 = r3[3]
            prevR4 = r4[3]
            rules[r3[0]][3] = r4[3]
            rules[r4[0]][3] = prevR3
            
            if solve(rules, graph.copy()) == expected:
                return sorted([r1[3],r2[3],r3[3],r4[3]]) # ,r5[3],r6[3],r7[3],r8[3]

            rules[r3[0]][3] = prevR4
            rules[r4[0]][3] = prevR3
        
        rules[r1[0]][3] = prevR1
        rules[r2[0]][3] = prevR2
    
print("Part 1:", part1())
print("Part 2:", part2())

options = sorted(["z07","gmt","qjj","cbj","z18","stg","dmn","z35","cfk"])
for i in range(len(options)):
    print(",".join(options[:i] + options[i + 1:]))