
# 0/1 Knapsack using Dynamic Programming

def knapsack(profit, weight, capacity):
    n = len(profit)

    # Create DP table
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Fill DP table
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):

            if weight[i - 1] <= w:
                dp[i][w] = max(
                    profit[i - 1] + dp[i - 1][w - weight[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


# Input
n = int(input("Enter number of items: "))

profit = []
weight = []

for i in range(n):
    p = int(input(f"Enter profit of item {i+1}: "))
    w = int(input(f"Enter weight of item {i+1}: "))

    profit.append(p)
    weight.append(w)

capacity = int(input("Enter knapsack capacity: "))

# Calculate maximum profit
result = knapsack(profit, weight, capacity)

print("Maximum Profit =", result)
