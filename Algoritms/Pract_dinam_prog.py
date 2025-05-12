# Задача 1
print("Задача 1")
def knapsack(W, wt, val, n):
    dp = [[0 for x in range(W + 1)] for x in range(n+1)]
    for i in range(n +1):
        for w in range(W+1):
            if i ==0 and w == 0:
                dp[i][w] = 0
            elif wt[i-1] <= w:
                dp[i][w] = max(val[i-1] + dp[i-1][w-wt[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
    return dp[n][W]
val = [10,500,150]
wt = [50,500,30]
W=580
n=len(val)
print(knapsack(W, wt, val, n))
# Задача 2
print("Задача 2")
def lcs(str1, str2):
    l_str1 = len(str1)
    l_str2 = len(str2)
    dp = [[0]*(l_str2 + 1) for _ in range(l_str1 + 1)]
    for i in range(1, l_str1 + 1):
        for j in range(1, l_str2 + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    res = ""
    i, j = l_str1, l_str2
    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            res = str1[i - 1] + res
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return len(res)
a = "Really"
b= "Usually"
print(lcs(a,b))
# Задача 3
print("Задача 3")
def num_sum(n, k):
    if n == 0:
        return 1
    count = 0
    for d in range(1, min(n, k) + 1):
        count += num_sum(n - d, d)
    return count
n = 5
print(num_sum(n, n))
# Задача 4
print("Задача 4")
def floyd_warshall(graph):
    n = len(graph)
    dist = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                dist[i][j] = 0
            elif graph[i][j] is not None:
                dist[i][j] = graph[i][j]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist
inf = float('inf')
graph = [[0, 3, inf, 7],
    [8, 0, 2, inf],
    [5, inf, 0, 1],
    [2, inf, inf, 0]]
all_pairs_shortest_paths = floyd_warshall(graph)
for row in all_pairs_shortest_paths:
    print(row)