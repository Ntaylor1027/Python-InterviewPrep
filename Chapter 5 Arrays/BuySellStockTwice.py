import unittest


def buy_sell_stock_twice(prices):
    max_total_profit, min_price_so_far = 0.0, float('inf')
    first_buy_sell_profits = [0] * len(prices)

    # Forward phase
    # Each day record max profit if we sell that day
    for i, price in enumerate(prices):
        min_price_so_far = min(min_price_so_far, price)
        max_total_profit = max(max_total_profit, price - min_price_so_far)
        first_buy_sell_profits[i] = max_total_profit

    # Backward phase
    # For each day find max profit if we make second buy on that day

    max_price_so_far = float('-inf')
    for i, price in reversed(list(enumerate(prices[1:], 1))):
        max_price_so_far = max(max_price_so_far, price)
        first_buy_sell_profit = first_buy_sell_profits[i-1]
        max_total_profit = max(
            max_total_profit,
            max_price_so_far - price + first_buy_sell_profit
        )

    return max_total_profit


class TestBuySellStockTwice(unittest.TestCase):
    def buy_sell_stock_twice(self):
        A = [12, 11, 13, 9, 12, 8, 14, 13, 15]
        print(f"prices: {A}")
        p = buy_sell_stock_twice(A)
        self.assertEqual(A, 10, "Should be 10")


if __name__ == '__main__':
    # unittest.main()
    A = [12, 11, 13, 9, 12, 8, 14, 13, 15]
    print(f"prices: {A}")
    p = buy_sell_stock_twice(A)
