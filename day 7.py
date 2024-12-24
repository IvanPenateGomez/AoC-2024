def part1():
    def valid(y, xs):
        if len(xs) == 1: return xs[0]==y
        
        return (
            valid(y,[xs[0]+xs[1]] + xs[2:]) or
            valid(y,[xs[0]*xs[1]] + xs[2:])
        )

    total = 0
    with open("day 7.txt", 'r') as file:
        for line in file:
            result, values = line.split(":")
            result = int(result)
            values = list(map(int, values.split()))
            if valid(result, values):
                total += result

    return total

def part2():
    def valid(y, xs):
        if len(xs) == 1: return xs[0]==y
        
        return (
            valid(y,[xs[0]+xs[1]] + xs[2:]) or
            valid(y,[xs[0]*xs[1]] + xs[2:]) or
            valid(y,[int(f"{xs[0]}{xs[1]}")] + xs[2:])
        )

    total = 0
    with open("day 7.txt", 'r') as file:
        for line in file:
            result, values = line.split(":")
            result = int(result)
            values = list(map(int, values.split()))
            if valid(result, values):
                total += result

    return total

print("Part 1:" ,part1())
print("Part 2:" ,part2())