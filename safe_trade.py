from brokerage import Brokerage
from stock_exchange import StockExchange
from trader import Trader
# from login_window import LoginWindow

def main():
    exchange = StockExchange()
    exchange.list_stock("DS", "DanceStudios.com", 12.33)
    exchange.list_stock("NSTL", "Nasty Loops Inc.", 0.25)
    exchange.list_stock("GGGL", "Giggle.com", 10.00)
    exchange.list_stock("MATI", "M and A Travel Inc.", 28.20)
    exchange.list_stock("DDLC", "Dulce De Leche Corp.", 57.50)
    exchange.list_stock("SAFT", "SafeTrade.com Inc.", 322.45)
    # exchange.get_listed_stocks()
    safe_trade = Brokerage(exchange)
    result = safe_trade.get_quote("NSTL")
    print(result)
    trader = Trader("Vihaan", "gfewvwgqwg", safe_trade)
    trader1 = Trader("Koushik Sir", "gfeqwfikbqwfb", safe_trade)
    create_trader_order = trader.create_order("GGGL",True,True,101,3000)
    create_trader_order1 = trader1.create_order("GGGL", False, True, 100, 300)
    safe_trade.place_order(create_trader_order)
    safe_trade.place_order(create_trader_order1)
    print(exchange.get_stock("GGGL"))
    # safe_trade.add_user("stockman", "sesame")
    # safe_trade.login("stockman", "sesame")
    # safe_trade.add_user("mstrade", "bigsecret")
    # safe_trade.login("mstrade", "bigsecret")
    #
    # window = LoginWindow("Safe Trade", safe_trade)
    # window.run()

def official_main():
    is_true = True
    exchange = StockExchange()
    upstox = Brokerage(exchange)
    while is_true:
        print("Welcome to the Trading Application!")
        print("Press 1 to SignUp")
        print("Press 2 to Login")
        print("Press 3 to Quit")
        print("Press 4 to get the names of all the trades")
        print("Press 5 to get the names of the logged traders")
        choice_input = int(input("Please enter your choice : "))
        match choice_input:
            case 1:
                name = input("Enter your name : ").lower()
                password = (input("Enter your password : "))
                result = upstox.add_user(name,password)
                print(result)
            case 2:
                name = input("Enter your name : ").lower()
                password = input("Enter your password : ")
                result = upstox.login(name,password)
                print(result)
            case 3:
                is_true = False
            case 4:
                upstox.get_traders()
            case 5:
                upstox.get_logged_traders()

if __name__ == "__main__":
    official_main()
