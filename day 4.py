def part1():
    mat = []
    counter = 0
    
    #Count in rows
    for line in open("day 4.txt",'r').read().split('\n'):
        counter += line.count("XMAS")
        counter += line.count("SAMX")
        mat.append(line)
    
    #Count in columns
    for y in range(len(mat[0])):
        col = "".join(list(mat[x][y] for x in range(len(line))))
        counter += col.count("XMAS")
        counter += col.count("SAMX")    
    
    #Count one diagonal
    for z in range(len(mat) * 2):
        diagonal = "".join(list(mat[y][x] for x in range(z+1) for y in range(z+1) if x + y == z and y < len(mat) and x < len(mat)))
        counter += diagonal.count("XMAS")
        counter += diagonal.count("SAMX")
    
    #Counter opp diagonal
    for z in range(len(mat) * 2):
        diagonal = "".join(list(mat[y][len(mat) - 1 - x] for x in range(z+1) for y in range(z+1) if x + y == z and y < len(mat) and x < len(mat)))
        counter += diagonal.count("XMAS")
        counter += diagonal.count("SAMX")
    return counter

def part2():
    mat = list(a for a in open("day 4.txt",'r').read().split('\n'))
    counter = 0
    
    for y in range(1,len(mat) - 1):
        for x in range(1,len(mat) - 1):
            if mat[y][x] == 'A' and (
                    (mat[y + 1][x + 1] == 'S' and mat[y + 1][x - 1] == 'S' and 
                     mat[y - 1][x + 1] == 'M' and mat[y - 1][x - 1] == 'M') or
                    (mat[y + 1][x + 1] == 'M' and mat[y + 1][x - 1] == 'S' and 
                     mat[y - 1][x + 1] == 'M' and mat[y - 1][x - 1] == 'S') or 
                    (mat[y + 1][x + 1] == 'M' and mat[y + 1][x - 1] == 'M' and 
                     mat[y - 1][x + 1] == 'S' and mat[y - 1][x - 1] == 'S') or 
                    (mat[y + 1][x + 1] == 'S' and mat[y + 1][x - 1] == 'M' and 
                     mat[y - 1][x + 1] == 'S' and mat[y - 1][x - 1] == 'M')
                ):
                counter += 1
    return counter
print(part2())  