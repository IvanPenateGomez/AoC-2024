program = [2,4,1,2,7,5,4,5,1,3,5,5,0,3,3,0]
VAL = {
    0: 0, 
    1: 1,
    2: 2, 
    3: 3, 
    4: 17122024,# A 
    5: 0,       # B 
    6: 0        # C
}

def part1():
    p = program.copy()
    pc = 0
    output = []

    while pc < len(p):
        opcode, operand = p[pc:pc + 2]
        operand_value = VAL[operand]

        match opcode:
            case 0:  # adv
                VAL[4] //= (2 ** operand_value)
            case 1:  # bxl
                VAL[5] ^= operand
            case 2:  # bst
                VAL[5] = operand_value % 8
            case 3:  # jnz
                if VAL[4] != 0:
                    pc = operand_value
                    continue  # Avoid incrementing `pc` after jump
            case 4:  # bxc
                VAL[5] ^= VAL[6]
            case 5:  # out
                output.append(str(operand_value % 8))
            case 6:  # bdv
                VAL[5] = VAL[4] // (2 ** operand_value)
            case 7:  # cdv
                VAL[6] = VAL[4] // (2 ** operand_value)
            case _:
                raise ValueError(f"Unknown opcode: {opcode}")

        pc += 2

    return ','.join(output)


def part1Debug():
    p = program.copy()
    pc = 0
    output = []

    print("Program:", p)
    print("VAL:", VAL)

    while pc < len(p):
        opcode, operand = p[pc:pc + 2]
        operand_value = VAL[operand]

        print(f"\nPC: {pc}, Opcode: {opcode}, Operand: {operand}, Operand Value: {operand_value}")

        match opcode:
            case 0:  # adv
                print(f"Divide A by 2 ** operand A={VAL[4]}")
                VAL[4] //= (2 ** operand_value)
                print(f"After: {VAL[4]}")

            case 1:  # bxl
                print(f"B XOR operand B={VAL[5]}")
                VAL[5] ^= operand
                print(f"After: {VAL[5]}")

            case 2:  # bst
                print(f"operand value mod 8 - B={VAL[5]}")
                VAL[5] = operand_value % 8
                print(f"After BST - VAL[5]: {VAL[5]}")

            case 3:  # jnz
                print(f"A={VAL[4]}, future pc={operand_value}")
                if VAL[4] != 0:
                    pc = operand_value
                    print(f"jump taken: {pc}")
                    continue  # Avoid incrementing `pc` after jump
                print("no jump, end of program")

            case 4:  # bxc
                print(f"B XOR C , B={VAL[5]}, C={VAL[6]}")
                VAL[5] ^= VAL[6]
                print(f"After{VAL[5]}")

            case 5:  # out
                print(f"OUT operand value mod 8 = {operand_value % 8}")
                output.append(str(operand_value % 8))

            case 6:  # bdv
                print(f"A DIV 2 ** operand value, A={VAL[4]}, B={VAL[5]}")
                VAL[5] = VAL[4] // (2 ** operand_value)
                print(f"After {VAL[5]}")

            case 7:  # cdv
                print(f"A DIV C - A={VAL[4]}, C={VAL[6]}")
                VAL[6] = VAL[4] // (2 ** operand_value)
                print(f"After {VAL[6]}")

            case _:
                raise ValueError(f"opcode error: {opcode}")

        pc += 2

    return ','.join(output)

VAL = {
    0: 0,  # Combo operand 0
    1: 1,  # Combo operand 1
    2: 2,  # Combo operand 2
    3: 3,  # Combo operand 3
    4: 2024,  # A register
    5: 0,  # B register
    6: 0   # C register
}


def test(A):
    B = 0
    C = 0
    output = []

    while A != 0:
        B = A % 8
        B = B ^ 2
        C = A // (2**B)
        B = B ^ C
        B = B ^ 3
        output.append(B % 8)
        A = A // 8
        
    return output == program[-len(output):]

def part2():
    arr = [0]
    for _ in range(len(program)):
        arr = [a for x in range(8) for e in arr if test(a:=((e<<3) + x))]
    return min(arr)
  
print("Part 1:", part1())
print("Part 2:", part2())