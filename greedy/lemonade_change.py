bills = [5,5,5,10,20]

def possible_change(bills):
    # optimal => TC: O(n), SC: O(1)
    five, ten = 0, 0
    for bill in bills:
        if bill == 5:
            five += 1
        elif bill == 10:
            if five == 0: return False
            ten += 1
            five -= 1
        else:
            if ten and five:
                ten -= 1
                five -= 1
            elif five >= 3:
                five -= 3
            else:
                return False
    return True
print(possible_change(bills))
