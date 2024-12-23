def getIteration(num):
    num = (num ^ (num * 64)) % 16777216
    num = (num ^ (num // 32)) % 16777216
    num = (num ^ (num * 2048)) % 16777216
    return num

def part1():
    total = 0
    cache = dict()
    for line in open("day 22.txt", 'r').read().split():
        num = int(line)
        for x in range(2000):
            if num not in cache:
                cache[num] = getIteration(num)
            num = cache[num] 
        total += num 
    return total

def part2():
    total = 0
    cache = {}
    sequences = dict()
    count = -1
    for line in open("day 22.txt", 'r').read().split():
        count += 1
        num = int(line)
        queue = []
        prev = num % 10

        for _ in range(2000):
            if num not in cache:
                cache[num] = getIteration(num)
            num = cache[num]

            current_digit = num % 10
            change = current_digit - prev
            queue.append(change)

            if len(queue) == 4:
                if tuple(queue) in sequences:
                    if count not in sequences[tuple(queue)]:
                        sequences[tuple(queue)][count] = num%10
                else:      
                    sequences[tuple(queue)] = {count:num%10}
                
                queue.pop(0)

            prev = current_digit

    maxSequence = -1
    for buyersKeys in sequences.values():
        a = sum(buyersKeys.values())
        if a > maxSequence:
            maxSequence = a
        
    return maxSequence

print(part1())
print(part2())
