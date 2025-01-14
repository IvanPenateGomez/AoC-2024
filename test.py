import re

values,gates = dict(),dict()

with open("day 24.txt") as f:
    while m := re.match(r"(\w{3}): ([01])", f.readline()):
        wire, val = m.groups()
        values[wire] = int(val)
    while m := re.match(r"(\w{3}) (\w{2,3}) (\w{3}) -> (\w{3})", f.readline()):
        wire1, operator, wire2, result = m.groups()
        gates[result] = (wire1 if wire1<wire2 else wire2, operator, wire2 if wire1<wire2 else wire1)

def determine(gate):
    if gate in values:
        return values[gate]
    elif gate in gates:
        wire1, operator, wire2 = gates[gate]
        match operator:
            case "AND": return determine(wire1)&determine(wire2)
            case "XOR": return determine(wire1)^determine(wire2)
            case "OR" : return determine(wire1)|determine(wire2)
            case _    : raise Exception(f"unknown operator {operator} in {gate}: {gates[gate]}")
    elif not re.match(r"z\d{2}", gate):
        raise Exception(f"unknown non-z gate {gate}")
    else:
        return 0

zxx = [determine(f"z{i:02}") for i in range(100)]
result = sum(z<<i for i,z in enumerate(zxx))
print(f"result: {result}")

visited = set()
def recursiveprint(gate, depth):
    if gate in visited or re.match(r"[xy]\d{2}", gate): return
    visited.add(gate)
    w1, op, w2 = gates[gate]
    prefix="\t"*depth
    print(f"{prefix}{gate}: {w1} {op} {w2}")
    recursiveprint(w1, depth+1)
    recursiveprint(w2, depth+1)


for z in [f"z{i:02}" for i in range(46)]:
    recursiveprint(z, 0)