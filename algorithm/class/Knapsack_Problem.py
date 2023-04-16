def knapsack(W, weight, val, n, memo):
    if memo[n][W] is not None:
        return memo[n][W]
    if n == 0 or W == 0:
        memo[n][W] = 0, []
        return 0, []
    if weight[n-1] > W:
        result, items = knapsack(W, weight, val, n-1, memo)
        memo[n][W] = result, items
        return memo[n][W]
    else:
        without_item, items = knapsack(W, weight, val, n-1, memo)
        with_item, items_new = knapsack(W-weight[n-1], weight, val, n-1, memo)
        with_item += val[n-1]
        if with_item > without_item:
            items_new.append(n-1)
            memo[n][W] = with_item, items_new
            return memo[n][W]
        else:
            memo[n][W] = without_item, items
            return memo[n][W]

def fractional_knapsack(capacity, weights, values):
    items = [(values[i], weights[i]) for i in range(len(values))]
    items.sort(reverse=True, key=lambda x: x[0]/x[1])
    result = 0
    knapsack = []
    for value, weight in items:
        if capacity == 0:
            return result, knapsack
        fraction = min(weight, capacity)
        result += fraction * (value / weight)
        capacity -= fraction
        knapsack.append(fraction)
    return result, knapsack

val = [60, 100, 120]
weight = [10, 20, 30]
W = 50
n = len(val)

memo = [[None]*(W+1) for _ in range(n+1)]
item, result = knapsack(W, weight, val, n, memo)

print()
print("item의 수 :", item)
print()
print("result : ", result)

result, knap = fractional_knapsack(W, weight, val)

print()
print("ratio : ", knap)

print()
print("result : ", result)


