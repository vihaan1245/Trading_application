from stock import Stock

class StockExchange:
    def __init__(self):
        self.stocks = {}
        pass

    def list_stock(self, symbol: str, company: str, price: float):
        self.stocks.update({symbol : Stock(symbol,company,price)})
        pass

    def get_quote(self, symbol: str) -> str:
        if symbol not in self.stocks:
            return f"{symbol} is not there in the stocks"
        else:
            return self.stocks[symbol].get_quote()

    def place_order(self, trade_order):
        self.stocks[trade_order.symbol].place_order(trade_order)
        return "The order has been placed!"

    def get_listed_stocks(self):
        for k,v in self.stocks.items():
            print(f"Symbol : {k}")
            print(f"{v}")
        pass

    def get_stock(self,symbol):
        return self.stocks[symbol]

    def __str__(self):
        pass
