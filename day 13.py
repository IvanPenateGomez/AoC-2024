def part1():
    def getPath(A, B, P):
        ax, ay = A
        bx, by = B
        px, py = P

        min_cost = float('inf')
        for aCount in range(max([P[0]//A[0],P[1]//A[1],P[0]//B[0],P[1]//B[1]])):
            if (px - ax * aCount) % bx == 0 and (py - ay * aCount) % by == 0:
                bCount_x = (px - ax * aCount) // bx
                bCount_y = (py - ay * aCount) // by

                if bCount_x == bCount_y and bCount_x >= 0:
                    cost = 3 * aCount + bCount_x
                    min_cost = min(min_cost, cost)

        return min_cost if min_cost != float('inf') else 0       
    
    total = 0
    A = (0,0)
    B = (0,0)
    P = (0,0)
    for line in list(open("day 13.txt",'r').read().split("\n")):
        if line == "":
            total += getPath(A,B,P)
            continue
        
        label, coords = line.split(":")
        x,y = coords.split(",")
        if "A" in label:
            A = (int(x.split("+")[1]), int(y.split("+")[1]))
        if "B" in label:
            B = (int(x.split("+")[1]), int(y.split("+")[1]))
        if "P" in label:
            P = (int(x.split("=")[1]), int(y.split("=")[1]))
    return total


def part2():
    from sympy import symbols, Eq, solve
        
    def solveEq(A, B, P):
        a, b = symbols('a b', integer=True)
        eq1 = Eq(A[0] * a + B[0] * b, P[0])
        eq2 = Eq(A[1] * a + B[1] * b, P[1])

        solution = solve((eq1, eq2), (a, b))
        if solution:
            aC, bC = solution[a], solution[b]
            if aC >= 0 and bC >= 0:
                return 3 * aC + bC
        return 0

    total = 0
    A = (0, 0)
    B = (0, 0)
    P = (0, 0)

    for line in list(open("day 13.txt", 'r').read().split("\n")):
        if line == "":
            total += solveEq(A, B, (P[0]+10000000000000,P[1]+10000000000000))
            continue

        label, coords = line.split(":")
        x, y = coords.split(",")
        if "A" in label:A = (int(x.split("+")[1]), int(y.split("+")[1]))
        elif "B" in label:B = (int(x.split("+")[1]), int(y.split("+")[1]))
        elif "P" in label:P = (int(x.split("=")[1]), int(y.split("=")[1]))

    return total

print(part1())
print(part2())