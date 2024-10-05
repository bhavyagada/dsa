def makeRow(r):
    row = [1]
    ans = 1
    for i in range(1, r):
        ans *= (r - i)
        ans //= i
        row.append(ans)
    return row

def generate(numRows):
    res = []
    for i in range(1, numRows+1):
        row = makeRow(i)
        res.append(row)
    return res

print(generate(3))
print(generate(4))
print(generate(5))