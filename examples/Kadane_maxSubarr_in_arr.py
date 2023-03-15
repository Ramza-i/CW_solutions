def kadane(A):
    best = 0
    now = 0
    for i in A:
        now = max(0, now+i)
        best = max(best, now)
    return best

print(kadane(arr))