class TradeOrder:
    def __init__(self, trader, symbol: str, buy_order: bool,
                 market_order: bool, num_shares: int, price: float):
        self.trader = trader
        self.symbol = symbol
        self.buy_order = buy_order
        self.market_order = market_order
        self.num_shares = num_shares
        self.price = price

    @property
    def is_buy(self) -> bool:
        return self.buy_order

    @property
    def is_sell(self) -> bool:
        return not self.buy_order

    @property
    def is_market(self) -> bool:
        return self.market_order

    @property
    def is_limit(self) -> bool:
        return not self.market_order

    @property
    def get_num_shares(self) -> int:
        return self.num_shares

    @property
    def get_price(self) -> float:
        return self.price

    def __str__(self):
        return f"Order Type : {"Buy" if self.is_buy else "Sell"}, Market/Limit : {"Market" if self.is_market else "Limit"}, Number of Shares : {self.get_num_shares}, Price : {self.get_price}"
