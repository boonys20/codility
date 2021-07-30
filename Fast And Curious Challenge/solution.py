
def Solution(A):
    N = len(A)
    best = 10**14
    for X in range(N):
        cost = 0
        for i in range(N):
            if i <= X:
                cost += A[X] - A[i]
            else:
                cost += A[N-1] - A[i]
        best = min(best, cost)
    return best % (10**9 + 7)

def Da_Best_Solution(A):
    N = len(A)
    cost = 0
    for i in range(1, N):
        cost += A[N-1] - A[i]
    best = cost
    for X in range(N - 1):
        cost -= A[N - 1] - A[X + 1]
        cost += (X + 1) * (A[X + 1] - A[X])
        best = min(best, cost)
    return best % (10**9 + 7)
    

if __name__ == "__main__":
    cities = [[1, 5, 9, 12], [5, 15], [2, 6, 7, 8, 12]];
    for city in cities:
        print(Solution(city))