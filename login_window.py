import tkinter as tk
from tkinter import simpledialog, messagebox
from trader_window import TraderWindow

class LoginWindow:
    def __init__(self, title, server):
        self.server = server
        self.window = tk.Tk()
        self.window.title(title)

        tk.Label(self.window, text="Login name:").grid(row=0, column=0)
        self.name_entry = tk.Entry(self.window)
        self.name_entry.grid(row=0, column=1)

        tk.Label(self.window, text="Password:").grid(row=1, column=0)
        self.password_entry = tk.Entry(self.window, show="*")
        self.password_entry.grid(row=1, column=1)

        login_btn = tk.Button(self.window, text="Login", command=self.try_login)
        login_btn.grid(row=2, column=0)

        reg_btn = tk.Button(self.window, text="New user...", command=self.register)
        reg_btn.grid(row=2, column=1)

    def try_login(self):
        name = self.name_entry.get().strip().lower()
        password = self.password_entry.get().strip().lower()
        result = self.server.login(name, password)
        if result < 0:
            msg = { -1: "User unknown", -2: "Invalid password", -3: "User already logged in" }.get(result, "Unknown error")
            messagebox.showerror("Login failed", msg)

    def register(self):
        while True:
            name = simpledialog.askstring("Register", "Login name (4-10 chars):")
            if not name:
                break
            password = simpledialog.askstring("Register", "Password (2-10 chars):", show='*')
            password2 = simpledialog.askstring("Register", "Confirm password:", show='*')
            if password != password2:
                messagebox.showerror("Error", "Passwords do not match")
                continue
            result = self.server.add_user(name.lower(), password.lower())
            if result == 0:
                messagebox.showinfo("Success", f"User {name} registered.")
                self.name_entry.delete(0, tk.END)
                self.name_entry.insert(0, name)
                self.password_entry.delete(0, tk.END)
                self.password_entry.insert(0, password)
                break
            else:
                error = {
                    -1: "Login name must be 4-10 characters long",
                    -2: "Password must be 2-10 characters long",
                    -3: "Login name already taken"
                }.get(result, "Unknown error")
                messagebox.showerror("Error", error)

    def run(self):
        self.window.mainloop()
