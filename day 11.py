def part1():
    arr = [int(x) for x in open("day 11.txt").readline().split()]
    for _ in range(25):
        tempArr = []
        for s in arr:
            if s == 0:
                tempArr.append(1)
            elif (v:=len(str(s))) % 2 == 0:
                tempArr.append(s // (10**(v//2)))
                tempArr.append(s % (10**(v//2)))
            else:
                tempArr.append(s*2024)
        arr = tempArr.copy()
    
    return len(arr)


def part2():
    arr = {0: 1, 5601550: 1, 3914: 1, 852: 1, 50706: 1, 68: 1, 6: 1, 645371: 1}
    
    for _ in range(75):
        temp = {}
        for s, c in arr.items():
            if s == 0:
                temp[1] = temp.get(1, 0) + c
            elif (v := len(str(s))) % 2 == 0:
                left, right = divmod(s, 10**(v // 2))
                temp[left] = temp.get(left, 0) + c
                temp[right] = temp.get(right, 0) + c
            else:
                temp[s * 2024] = temp.get(s * 2024, 0) + c
        arr = temp
        print(len(arr))
    
    return sum(arr.values())

print(part2())

