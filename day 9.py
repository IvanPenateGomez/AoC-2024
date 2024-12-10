def part1():
    with open("day 9.txt", 'r') as file:
        string = file.read().strip()
        out = []
        currentNum = 0
        isFile = True
        pointer = 0
        freeSpaces = []

        for num in string:
            a = int(num)
            if isFile:
                out.extend([str(currentNum)] * a)
                isFile = False
                currentNum += 1
            else:
                out.extend(['.'] * a)
                isFile = True
                freeSpaces.extend(range(pointer, pointer + a))
            pointer += a

        p = 0
        while p < len(freeSpaces):
            while out[-1] == '.':
                out.pop(-1)
                freeSpaces.pop(-1)
            if p >= len(freeSpaces):
                break
            out[freeSpaces[p]] = out.pop(-1)
            p += 1

        total = sum(int(out[x]) * x for x in range(len(out)) if out[x] != '.')
        return total
    
def part2():
    def find_place(L, out):
        for x in range(len(out)):
            if out[x] == ".":
                if all(out[x + i] == "." for i in range(L)):
                    return x
        return None

    with open("day 9.txt", 'r') as file:
        string = file.read().strip()
        out = []
        currentNum = 0
        
        isFile = True
        for num in string:
            count = int(num)
            if isFile:
                out.extend([str(currentNum)] * count)
                currentNum += 1
            else:
                out.extend(["."] * count)
            isFile = not isFile

        arr = []
        i = 0
        while i < len(out):
            if (id:=out[i]) != ".":
                start = i
                while i < len(out) and out[i] == id: 
                    i += 1
                arr.append((id, start, i - start))
            else:
                i += 1

        for id, start, length in reversed(arr):
            p = find_place(length, out)
            if p is not None and p < start:
                for i in range(length):
                    out[p + i] = id
                    out[start + i] = "."

        return sum(int(v) * i for i,v in enumerate(out) if out[i] != ".")

print(part2())
