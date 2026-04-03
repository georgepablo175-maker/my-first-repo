from total_sum import total_sum

def calculate_average(prices):
    total = total_sum(prices)
    return total / len(prices)
