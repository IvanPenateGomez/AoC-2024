def solveEq(A, B, P):
    a = abs((B[1] * P[0] - B[0] * P[1]) / (B[0] * A[1] - A[0] * B[1]))
    b = (P[1] - A[1] * a) / B[1] if B[1] != 0 else (P[0] - A[0] * a) / B[0]
    return (
        3 * int(a) + int(b) 
        if a >= 0 and b >= 0 and abs(a - round(a)) < 1e-9 and abs(b - round(b)) < 1e-9 
        else 0)

def part1():    
    p1,p2 = 0,0
    for line in list(open("day 13.txt",'r').read().split("\n")):
        if line == "":
            p1 += solveEq(A,B,P)
            p2 += solveEq(A,B,(P[0]+10**13,P[1]+10**13))
            continue
        
        label, coords = line.split(":")
        x,y = coords.split(",")
        if "A" in label:A = (int(x.split("+")[1]), int(y.split("+")[1]))
        if "B" in label:B = (int(x.split("+")[1]), int(y.split("+")[1]))
        if "P" in label:P = (int(x.split("=")[1]), int(y.split("=")[1]))
    return p1,p2

p1,p2 = part1()
print("Part 1:", p1)
print("Part 2:", p2)