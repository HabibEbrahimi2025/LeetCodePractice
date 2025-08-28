def can_measure(low, high, cups, memo):
    if (low, high) in memo:
        return memo[(low, high)]

    # base case: range covers 0
    if low <= 0 <= high:
        return True

    for L, H in cups:
        new_low = low - H
        new_high = high - L
        if can_measure(new_low, new_high, cups, memo):
            memo[(low, high)] = True
            return True

    memo[(low, high)] = False
    return False

cups=[(200,210), (450, 465), (800, 850)]
low=2100
high=2300

print(can_measure(low,high, cups, {}))