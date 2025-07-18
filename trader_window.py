import tkinter as tk
from tkinter import messagebox
from trade_order import TradeOrder

class TraderWindow:
    def __init__(self, trader):
        self.trader = trader
        self.window = tk.Toplevel()
        self.window.title(trader.get_name())

        self.symb_entry = self.add_labeled_entry("Stock symbol:", 0)
        self.ns_entry = self.add_labeled_entry("Number of shares:", 1)
        self.price_entry = self.add_labeled_entry("Price (if limit):", 2)

        self.buy_var = tk.BooleanVar(value=True)
        tk.Checkbutton(self.window, text="Buy Order", variable=self.buy_var).grid(row=3, column=0)

        self.market_var = tk.BooleanVar(value=True)
        tk.Checkbutton(self.window, text="Market Order", variable=self.market_var).grid(row=3, column=1)

        tk.Button(self.window, text="Get Quote", command=self.get_quote).grid(row=4, column=0)
        tk.Button(self.window, text="Place Order", command=self.place_order).grid(row=4, column=1)

        self.msg_area = tk.Text(self.window, height=10, width=50)
        self.msg_area.grid(row=5, column=0, columnspan=2)

    def add_labeled_entry(self, label, row):
        tk.Label(self.window, text=label).grid(row=row, column=0)
        entry = tk.Entry(self.window)
        entry.grid(row=row, column=1)
        return entry

    def get_quote(self):
        symbol = self.symb_entry.get().strip().upper()
        if not symbol:
            messagebox.showerror("Error", "Missing stock symbol")
        else:
            self.trader.get_quote(symbol)

    def place_order(self):
        try:
            symbol = self.symb_entry.get().strip().upper()
            num_shares = int(self.ns_entry.get())
            price_str = self.price_entry.get().strip()
            buy = self.buy_var.get()
            market = self.market_var.get()
            price = 0.0 if market else float(price_str)
            order = TradeOrder(self.trader, symbol, buy, market, num_shares, price)
            self.trader.place_order(order)
        except ValueError:
            messagebox.showerror("Error", "Invalid input")

    def show_message(self, msg: str):
        self.msg_area.insert(tk.END, msg + "\n\n")
