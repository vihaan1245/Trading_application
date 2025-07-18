from trade_order import TradeOrder

class Trader:
    def __init__(self, name: str, password: str, brokerage):
        self.name = name
        self.password = password
        self.brokerage = brokerage
        pass

    @property
    def get_name(self):
        return self.name
        pass

    def create_order(self, symbol : str, buy_order : bool, market_order : bool, num_shares : int, price : float) -> TradeOrder:
        return TradeOrder(self,symbol,buy_order,market_order,num_shares,price)

    def open_window(self):
        pass

    def receive_messages(self):
        pass

    def quit(self):
        exit(0)

    def __lt__(self, other):
        pass

    def __str__(self):
        pass
