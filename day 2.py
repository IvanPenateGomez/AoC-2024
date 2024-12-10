
def is_safe(report):
    prev = report[0]
    inc = None
    for a in report[1:]:
        if a > prev:
            if inc is not None and not inc:
                return False
            inc = True
        elif a == prev:
            return False
        else:
            if inc is not None and inc:
                return False
            inc = False
        if abs(a - prev) > 3:
            return False
        prev = a
    return True


def part1():
    return sum(1 for line in open("day 2.txt").read().split("\n")
                if is_safe(list(int(x) for x in line.split())))

def part2():
    counter = 0

    # Read and process input
    for line in open("day 2.txt").read().split("\n"):
        line = list(int(x) for x in line.split())
        
        # Check if the line is safe without modification
        if is_safe(line):
            counter += 1
            continue

        # Check if removing one level makes the line safe
        for i in range(len(line)):
            modified_line = line[:i] + line[i+1:]
            if is_safe(modified_line):
                counter += 1
                break

    return counter

print(part2())

print(part1())