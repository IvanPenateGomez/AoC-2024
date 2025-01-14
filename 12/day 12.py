def part1():
    def perimeter(arr,region):
        total = len(region) * 4
        
        for x,y in region:
            for dx,dy in [(-1,0),(1,0),(0,1),(0,-1)]:
                nx,ny = x + dx, dy+y
                
                if (0<=nx<len(arr[0]) and 0<=ny<len(arr) and
                    arr[ny][nx] == arr[y][x]): total -= 1
        return total
    
    DIRECTIONS = [(0,1),(0,-1),(1,0),(-1,0)]
    def getRegion(arr,x,y,region:set):
        region.add((x,y))
        for dx,dy in DIRECTIONS:
            nx,ny = x + dx, y + dy
            
            if (0<=nx<len(arr[0]) and 0<=ny<len(arr) and (nx,ny) not in region and
                    arr[ny][nx] == arr[y][x]):
                getRegion(arr,nx,ny,region)
    
    arr = list(open("day 12.txt",'r').read().split("\n"))
    seen = set()    
    
    total = 0
    for y,v in enumerate(arr):
        for x,p in enumerate(v):
            if (x,y) not in seen:
                seen.add((x,y))
                region = set()
                getRegion(arr,x,y,region)
                seen = seen.union(region)
                total += len(region) * perimeter(arr,region)
    
    return total

def part2():
    def sides(arr,region):
        per = set()
        for x,y in region:
            for dx,dy in [(-1,0),(1,0),(0,1),(0,-1)]:
                nx,ny = x + dx, dy+y
                
                if not (0<=nx<len(arr[0]) and 0<=ny<len(arr) and
                    arr[ny][nx] == arr[y][x]): 
                        per.add((x,y,nx,ny))
        
        total = 0
        for ax,ay,bx,by in per:
            if not any((ax+dx,ay+dy,bx+dx,by+dy) in per for dx,dy in ((0,1),(1,0))):
                total += 1

        return total
    
    DIR = [(1,0),(0,1),(-1,0),(0,-1)]
    def getRegion(arr,x,y,region:set):
        region.add((x,y))
        for dx,dy in DIR:
            nx,ny = x + dx, y + dy
            
            if (0<=nx<len(arr[0]) and 0<=ny<len(arr) and (nx,ny) not in region and
                    arr[ny][nx] == arr[y][x]):
                getRegion(arr,nx,ny,region)
    
    arr = list(open("day 12.txt",'r').read().split("\n"))
    seen = set()    
    
    total = 0
    for y,v in enumerate(arr):
        for x,p in enumerate(v):
            if (x,y) not in seen:
                seen.add((x,y))
                region = set()
                getRegion(arr,x,y,region)
                seen = seen.union(region)
                total += len(region) * sides(arr,region)
    
    return total


print("Part 1:", part1())
print("Part 2:", part2())