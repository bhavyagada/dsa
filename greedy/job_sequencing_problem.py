id = [6,3,4,2,5,8,1,7]
deadline = [2,6,6,5,4,2,4,2]
profit = [80,70,65,60,25,22,20,10]

def job_sequence(id, deadline, profit):
    # optimal => TC: O(nlogn + n*max_deadline), SC: O(max_deadline)
    jobs = sorted(zip(id, deadline, profit), key= lambda x : x[2], reverse=True)

    max_deadline = max(deadline)
    schedule = [-1] * (max_deadline + 1)
    total_profit, cnt = 0, 0

    for job in jobs:
        job_id, job_deadline, job_profit = job
        for day in range(job_deadline, 0, -1):
            if schedule[day] == -1:
                schedule[day] += job_id
                total_profit += job_profit
                cnt += 1
                break
    return [cnt, total_profit]
print(job_sequence(id, deadline, profit))

