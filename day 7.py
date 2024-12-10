def mySolution():
    def valid(y, xs):
        if len(xs) == 1: return xs[0]==y
        if valid(y,[xs[0]+xs[1]] + xs[2:]):
            return True
        if valid(y,[xs[0]*xs[1]] + xs[2:]):
            return True
        if valid(y,[int(f"{xs[0]}{xs[1]}")] + xs[2:]):
            return True
        return False
        """
        toAdd = set()
        last = xs[-1]
        for a in values:
            toAdd.add(last + a)
            toAdd.add(last * a)
            toAdd.add(int(f"{a}{last}"))
        
        return values.union(toAdd)
        """

    total = 0
    with open("day 7.txt", 'r') as file:
        for line in file:
            result, values = line.split(":")
            result = int(result)
            values = list(map(int, values.split()))
            if valid(result, values):
                total += result

    print(total)

mySolution()