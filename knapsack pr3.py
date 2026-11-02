
# Fractional Knapsack using Greedy Method

def fractional_knapsack(profit, weight, capacity):
    n = len(profit)

    # Calculate profit/weight ratio
    items = []
    for i in range(n):
        ratio = profit[i] / weight[i]
        items.append((ratio, profit[i], weight[i]))

    # Sort items by ratio in descending order
    items.sort(reverse=True)

    total_profit = 0

    for ratio, p, w in items:
        if capacity >= w:
            # Take the complete item
            total_profit += p
            capacity -= w
        else:
            # Take a fraction of the item
            total_profit += ratio * capacity
            capacity = 0
            break

    return total_profit


# Input
n = int(input("Enter number of items: "))

profit = []
weight = []

for i in range(n):
    p = float(input(f"Enter profit of item {i+1}: "))
    w = float(input(f"Enter weight of item {i+1}: "))
    profit.append(p)
    weight.append(w)

capacity = float(input("Enter knapsack capacity: "))

# Calculate maximum profit
result = fractional_knapsack(profit, weight, capacity)

print("Maximum Profit =", result)
