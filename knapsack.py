def knapsack(weights, values, capacity):
    n = len(values)
    memo = [[-1 for _ in range(capacity + 1)] for _ in range(n + 1)]

    def knapsack_rec(w, i):
        if i == 0 or w == 0:
            return 0
        if memo[i][w] != -1:
            return memo[i][w]
        if weights[i - 1] <= w:
            memo[i][w] = max(values[i - 1] + knapsack_rec(w - weights[i - 1], i - 1), knapsack_rec(w, i - 1))
        else:
            memo[i][w] = knapsack_rec(w, i - 1)
        return memo[i][w]

    return knapsack_rec(capacity, n)

weights = [50, 55, 56, 57, 58]
values = [50, 55, 56, 57, 58]
capacity = 3
print(knapsack(weights, values, capacity))