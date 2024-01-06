

def buy_sell(A):
    max_profit = 0.0
    min_price = float('inf')

    for price in A:
        min_price = min(price, min_price)
        compare = price - min_price
        max_profit = max(compare, max_profit)
    return max_profit

A = [350,150,300,200,100,150]
print(buy_sell(A))