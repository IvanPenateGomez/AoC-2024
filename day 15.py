g = []
def part1():
    isMap = True
    DIR = [(-1,0),(0,1),(1,0),(0,-1)]
    for line in open("day 15.txt",'r').read().split("\n"):
        if line == "":
            x,y = [(x,y) for x in range(len(g[0])) for y in range(len(g)) if g[y][x] == "@"][0]
            isMap = False
            continue
        if isMap:
            g.append(list(line))
            continue
        
    
        for move in line:
            match move:
                case '^':dy,dx = DIR[0]
                case '>':dy,dx = DIR[1]
                case 'v':dy,dx = DIR[2]
                case '<':dy,dx = DIR[3]
                case _: pass
            
            nx,ny =  x+dx,y+dy
            if 0<=nx<(len(g[0])) and 0<=ny<(len(g)):
                if g[ny][nx] == ".": 
                    g[ny][nx] = "@"
                    g[y][x] = "."
                    x = nx
                    y = ny
                    continue
                elif g[ny][nx] == "#":
                    continue
                
                boxX,boxY = nx,ny
                while 0<boxX<(len(g[0])-1) and 0<boxY<(len(g)-1):
                    boxX,boxY = boxX+dx,boxY+dy
                    if g[boxY][boxX] == ".":
                        g[boxY][boxX] = "O"
                        g[ny][nx] = "@"
                        g[y][x] = "."
                        x = nx
                        y = ny
                        break
                    elif g[boxY][boxX] == "#":
                        break
    return sum(y*100 + x for x in range(len(g[0])) for y in range(len(g)) if g[y][x] == "O")   

def moveVertically(graph,dir,y,x):
    if not (0<=y+dir<len(graph)):return False,1
    if graph[y+dir][x] in "[]" or graph[y+dir][x+1] in "[]":            
        if graph[y+dir][x] != graph[y][x] and graph[y+dir][x] in "[]":
            f,_ = moveVertically(graph,dir,y+dir,x-1)
            if not f:
                return False,1
        if graph[y+dir][x+1] != graph[y][x+1] and graph[y+dir][x+1] in "[]":
            f,_ = moveVertically(graph,dir,y+dir,x+1)
            if not f:
                return False,1
        if (graph[y+dir][x] == "[" or graph[y+dir][x+1] == "]"):
            f,_=moveVertically(graph,dir,y+dir,x,)
            if not f:
                return False,1
    
    if graph[y+dir][x] == "#" or graph[y+dir][x+1] == "#":
        return False,1
    if graph[y+dir][x] == "." and graph[y+dir][x+1] == ".":
        graph[y+dir][x] = graph[y][x]
        graph[y+dir][x+1] = graph[y][x+1]
        graph[y][x] = '.'
        graph[y][x+1] = '.'
        return True,graph

from copy import deepcopy
def part2():
    g = []
    isMap = True
    DIR = [(-1,0),(0,1),(1,0),(0,-1)]
    for line in open("day 15.txt",'r').read().split("\n"):
        if line == "":
            x,y = [(x,y) for x in range(len(g[0])) for y in range(len(g)) if g[y][x] == "@"][0]
            isMap = False
            continue
        if isMap:
            newRow = list()
            for pos in line:
                if pos == "O":
                    newRow.append("[")
                    newRow.append("]")
                elif pos == "@":
                    newRow.append("@")
                    newRow.append(".")
                else:
                    newRow.append(pos)
                    newRow.append(pos)
            g.append(newRow)
            continue           
        for move in line:
            match move:
                case '^':dy,dx = DIR[0]
                case '>':dy,dx = DIR[1]
                case 'v':dy,dx = DIR[2]
                case '<':dy,dx = DIR[3]
                case _: pass
            
            nx,ny =  x+dx,y+dy
            if 0<=nx<(len(g[0])) and 0<=ny<(len(g)):
                if dy == 0:
                    boxX,boxY = x,y
                    while 0<boxX<(len(g[0])-1) and 0<boxY<(len(g)-1):
                        boxX,boxY = boxX+dx,boxY+dy
                        if g[boxY][boxX] == ".":
                            row = g[ny]
                            row.pop(boxX)
                            row.insert(x,'.')
                            x = nx
                            y = ny 
                            break
                        elif g[boxY][boxX] == "#":
                            break
                else:
                    if g[ny][nx] == "#":continue
                    if g[ny][nx] == ".":
                        g[y][x] = "."
                        g[ny][nx] = "@"
                        y = ny
                        x = nx
                        continue
                    otherBox = g[ny][nx] == "[" and g[ny][nx + 1] == "]"
                    valid,tempG = moveVertically(deepcopy(g),dy,ny,(nx if otherBox else nx -1))
                    if valid:
                        g = tempG
                        g[y][x] = "."
                        g[ny][nx] = "@"
                        y = ny
                        x = nx    
    return sum(y*100 + x for x in range(len(g[0])) for y in range(len(g)) if g[y][x] == "[")   

print(part2())