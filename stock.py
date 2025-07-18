from queue import PriorityQueue
import heapq

class Stock:
    def __init__(self, symbol: str, company: str, price: float):
        self.symbol = symbol
        self.company = company
        self.last_price = price
        self.buy_orders = []
        self.sell_orders = []
        self.low_price = price
        self.high_price = price
        self.volume = 0
        pass

    def get_quote(self) -> str:
        return (f"Symbol : {self.symbol} \nCompany : {self.company} \nLast Price : {self.last_price}"
                f"\nLow Price : {self.low_price} \nHigh Price : {self.high_price}")

    def place_order(self, order):
        temp = self.buy_orders if order.is_buy else self.sell_orders
        priority = -order.get_price if order.is_limit and order.is_buy else order.get_price
        heapq.heappush(temp,(priority,id(order),order))
        self.execute_order()

    def execute_order(self):
        while self.buy_orders and self.sell_orders:
            buy = self.buy_orders[0][2]
            sell = self.sell_orders[0][2]
            if buy.is_limit and sell.is_limit and buy.price < sell.price:
                break
            if buy.is_market and sell.is_market:
                trade_price = self.last_price
            elif buy.is_market:
                trade_price = sell.price
            elif sell.is_market:
                trade_price = buy.price
            else:
                trade_price = buy.price

            trade_share_count = 0

            if buy.get_num_shares > sell.get_num_shares:
                buy.num_shares -= sell.num_shares
                self.volume += sell.num_shares
                trade_share_count = sell.num_shares
                heapq.heappop(self.sell_orders)
            elif buy.get_num_shares < sell.get_num_shares:
                sell.num_shares -= buy.get_num_shares
                self.volume += buy.num_shares
                trade_share_count = buy.num_shares
                heapq.heappop(self.buy_orders)
            else:
                heapq.heappop(self.buy_orders)
                heapq.heappop(self.sell_orders)
                trade_share_count = buy.num_shares
                self.volume += buy.num_shares

            self.last_price = trade_price
            self.low_price = min(self.low_price,trade_price)
            self.high_price = max(self.high_price,trade_price)
            print(f"Trader : {buy.trader.name} has received {trade_share_count} on price {trade_price}")
            print(f"Trader : {sell.trader.name} has sold {trade_share_count} on price {trade_price}")

    def __str__(self):
        if self.buy_orders:
            print(f"Stock Symbol for buy orders: {self.symbol}")
            for i,item in enumerate(self.buy_orders):
                print(f"{i+1} : {item[2]}")

        if self.sell_orders:
            print(f"Stock Symbol for sell orders: {self.symbol}")
            for i, item in enumerate(self.sell_orders):
                print(f"{i+1} : {item[2]}")

        return f"Company : {self.company} \nPrice : {self.last_price}"
        pass

