candidates = [10,1,2,7,6,1,5]
target = 8

def combination_sum(idx, candidates, target, ds, res):
    # TC: O(2^n * k) + O(nlogn), SC: O(n)
    if target == 0:
        res.append(ds.copy())
        return

    for i in range(idx, len(candidates)):
        if i > idx and candidates[i] == candidates[i-1]: continue
        if candidates[i] > target: break

        ds.append(candidates[i])
        combination_sum(i + 1, candidates, target - candidates[i], ds, res)
        ds.pop()

res = []
candidates.sort()
combination_sum(0, candidates, target, [], res)
print(res)

