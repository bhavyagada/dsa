def my_pow(x, n):
    def calc(x, n):
        if x == 0: return 0
        if n == 0: return 1

        ret = calc(x, n // 2)
        ret *= ret

        if n % 2 == 1: ret *= x
        return ret
    
    ret = calc(x, abs(n))
    return ret if n >= 0 else 1/ret

x = 2.00000
n = 10
ans = my_pow(x, n)
print(ans)
assert ans == 1024.00000