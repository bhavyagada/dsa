arr = [1,2,3,4,5]
k = 12

import heapq
def minimize_max_distance_brute(arr, k):
  # brute force => TC: O(nlogn+klogn), TC: O(2(n-1))
  n = len(arr)
  how_many, pq = [0] * (n - 1), []

  for i in range(n - 1):
    heapq.heappush(pq, ((-1)*(arr[i+1] - arr[i]), i))

  for _ in range(1, k + 1):
    tp = heapq.heappop(pq)
    sec_idx = tp[1]
    how_many[sec_idx] += 1
    inidiff = arr[sec_idx + 1] - arr[sec_idx]
    new_sec = inidiff / (how_many[sec_idx] + 1)
    heapq.heappush(pq, (-new_sec, sec_idx))
  return -pq[0][0]
print("minimize max distance (brute force):", minimize_max_distance_brute(arr, k))

def gas_stations_required(dist, arr):
  n = len(arr)
  cnt = 0
  for i in range(1, n):
    num_in_between = ((arr[i] - arr[i-1]) / dist)
    if (arr[i] - arr[i-1]) == dist * num_in_between:
      num_in_between -= 1
    cnt += num_in_between
  return cnt

def minimize_max_distance_optimal(arr, k):
  n = len(arr)
  low, high = 0, 0
  for i in range(n - 1):
    high = max(high, arr[i+1] - arr[i])

  diff = 1e-6
  while high - low > diff:
    mid = (low + high) / 2
    cnt = gas_stations_required(mid, arr)
    if cnt > k:
      low = mid
    else:
      high = mid
  return high # or low
print("minimize max distance (optimal):", minimize_max_distance_optimal(arr, k))
