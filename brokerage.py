from login import Login
from trade_order import TradeOrder
from trader import Trader


class Brokerage(Login):
    def __init__(self, exchange):
        self.traders = {}
        self.logged_traders = ()
        self.exchange = exchange

    def add_user(self, name: str, password: str) -> str:
        if len(name) < 4 or len(name) > 10:
            return "The name is not in the range given (4-10 characters)"
        elif len(password) < 2 or len(password) > 10:
            return "The password is not in the range given (2-10 characters)"
        elif name in self.traders:
            return "The name you have used already exists."
        else:
            self.traders.update({name : Trader(name,password,self)})
            return "Successfully Registered!"

    def login(self, name: str, password: str) -> str:
        if name not in self.traders:
            return "Login Failed\n"
        elif password != self.traders.get(name).password:
            return "Login Failed\n"
        elif name in self.logged_traders:
            return "You are already logged in.\n"
        else:
            self.logged_traders += (name,)
            return "Successfully Login!\n"

    def get_quote(self, symbol : str) -> str:
        return self.exchange.get_quote(symbol)

    def place_order(self, order : TradeOrder):
        self.exchange.place_order(order)

    def get_traders(self):
        for name in self.traders:
            print(f"Name : {name}\n")

    def get_logged_traders(self):
        print("Logged Traders")
        for (name) in self.logged_traders:
            print(f"{name}\n")

    def get_exchange(self):
        pass

    def __str__(self):
        pass
