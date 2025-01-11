# count digits
def count_digits(num):
    # brute force => TC: O(log10N + 1), SC: O(1)
    # count = 0
    # while num > 0:
    #     num = num // 10
    #     count += 1
    # return count

    # optimal => TC: O(1), SC: O(1)
    import math
    return int(math.log10(num) + 1)
assert count_digits(1998) == 4
print("count digits:", count_digits(1998))

# reverse a number
def reverse_num(num):
    # optimal => TC: O(log10N + 1), SC: O(1)
    n = abs(num)
    rev = 0
    while n > 0:
        rem = n % 10
        rev = (rev * 10) + rem
        n = n // 10
    return rev if num > 0 else -rev
assert reverse_num(1998) == 8991
print("reverse number:", reverse_num(1998))

# check palindrome
def check_palindrome(num):
    # optimal => TC: O(log10N + 1), SC: O(1)
    if num < 0: return False
    x = num
    rev = 0
    while x > 0:
        rem = x % 10
        rev = (rev * 10) + rem
        x = x // 10
    return num == rev
assert check_palindrome(1998) == False
print("check palindrome:", check_palindrome(1998))

# gcd or hcf
def gcd(n1, n2):
    # brute force => TC: O(min(n1, n2)), SC: O(1)
    # gcd = 1
    # for i in range(1, min(n1,n2) + 1):
    #     if n1 % i == 0 and n2 % i == 0:
    #         gcd = i
    # return gcd

    # better => TC: O(min(n1, n2)), SC: O(1)
    # for i in range(min(n1, n2), 0, -1):
    #     if n1 % i == 0 and n2 % i == 0:
    #         return i
    # return 1

    # optimal => TC: O(min(n1, n2)), SC: O(1)
    while n1 > 0 and n2 > 0:
        if n1 > n2:
            n1 = n1 % n2
        else:
            n2 = n2 % n1
    
    if n1 == 0: return n2
    return n1
assert gcd(20, 15) == 5
print("gcd or hcf:", gcd(20, 15))

# armstrong numbers
def armstrong_number(num):
    # optimal => TC: O(log10N + 1), SC: O(1)
    import math
    count = int(math.log10(num) + 1)
    summ = 0
    x = num
    while x > 0:
        rem = x % 10
        summ += (rem ** count)
        x = x // 10
    return summ == num
assert armstrong_number(153) == True
print("armstrong number:", armstrong_number(153))

# find divisors
def find_divisors(num):
    # brute force => TC: O(n), SC: O(n)
    # divisors = []
    # for i in range(1, num + 1):
    #     if num % i == 0:
    #         divisors.append(i)
    # return divisors

    # optimal => TC: O(sqrt(n)), SC: O(2*sqrt(n))
    import math
    divisors = []
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            divisors.append(i)
            if i != (num // i):
                divisors.append(num // i)
    return divisors
assert sorted(find_divisors(12)) == [1,2,3,4,6,12]
print("find divisors:", sorted(find_divisors(12)))

# check prime
def check_prime(num):
    # brute force => TC: O(n), SC: O(1)
    # cnt = 0
    # for i in range(1, num + 1):
    #     if num % i == 0:
    #         cnt += 1
    # return True if cnt == 2 else False

    # optimal => TC: O(sqrt(n)), SC: O(1)
    import math
    cnt = 0
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            cnt += 1
            if i != (num // i):
                cnt += 1
    return True if cnt == 2 else False
assert check_prime(10) == False
print("check prime:", check_prime(10))
