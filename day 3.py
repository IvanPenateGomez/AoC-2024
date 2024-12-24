def part1():
    memory = "".join(list(open("day 3.txt",'r').read().split("\n")))
    total_sum = 0
    i = 0
    while i < len(memory):
        if memory[i:i+4] == "mul(":
            i += 4
            x, y = "", ""
            
            while i < len(memory) and memory[i].isdigit():
                x += memory[i]
                i += 1
            
            if i < len(memory) and memory[i] == ',': i += 1
            else: continue
            
            while i < len(memory) and memory[i].isdigit():
                y += memory[i]
                i += 1
            
            if i < len(memory) and memory[i] == ')':
                i += 1
                if x.isdigit() and y.isdigit():
                    total_sum += int(x) * int(y)
            else: continue
        else: i += 1

    return total_sum

def part2():
    memory = "".join(list(open("day 3.txt",'r').read().split("\n")))
    total_sum = 0
    i = 0
    isDo = True
    while i < len(memory):
        if memory[i:i+4] == "mul(" and isDo:
            i += 4
            x, y = "", ""
            
            while i < len(memory) and memory[i].isdigit():
                x += memory[i]
                i += 1
            
            if i < len(memory) and memory[i] == ',': i += 1
            else: continue
            
            while i < len(memory) and memory[i].isdigit():
                y += memory[i]
                i += 1
            
            if i < len(memory) and memory[i] == ')':
                i += 1
                if x.isdigit() and y.isdigit():
                    total_sum += int(x) * int(y)
            else: continue
        elif memory[i:i+4] == "do()": 
            isDo = True
            i += 1
        elif memory[i:i+7] == "don't()": 
            i += 1
            isDo = False 
        else: i += 1

    return total_sum

print("Part 1:" ,part1())
print("Part 2:" ,part2())