#Name-Olabisi Oyedele
#Date-03/04/2025
#Module 08 Final Project
#Purpose-Pizza Ordering System

import tkinter as tk
from tkinter import messagebox

class PizzaOrderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pizza Ordering System")

        self.size = tk.StringVar()
        self.crust = tk.StringVar()
        self.sauce = tk.StringVar()
        self.cheese = tk.StringVar()
        self.topping_vars = []  # List to hold the BooleanVar for each topping

        self.create_main_menu_window()

    def create_main_menu_window(self):
        # Create the main menu window with options
        self.menu_frame = tk.Frame(self.root)
        self.menu_frame.pack(padx=20, pady=20)

        # Heading
        tk.Label(self.menu_frame, text="Welcome to Pizza Ordering System!", font=("Arial", 16)).grid(row=0, column=0, columnspan=2, pady=10)

        # Button to create custom pizza
        tk.Button(self.menu_frame, text="Create Your Own Pizza", command=self.on_create_custom_pizza).grid(row=1, column=0, pady=10)

        # Button to view predefined pizzas
        tk.Button(self.menu_frame, text="View Predefined Pizzas", command=self.on_view_predefined_pizzas).grid(row=2, column=0, pady=10)

        # Button to exit
        tk.Button(self.menu_frame, text="Exit", command=self.on_exit).grid(row=3, column=0, pady=10)

    def on_create_custom_pizza(self):
        """Callback to move to custom pizza creation screen."""
        self.menu_frame.pack_forget()  # Hide the main menu
        self.create_menu_window()  # Show custom pizza creation window

    def on_view_predefined_pizzas(self):
        """Callback to move to predefined pizza options screen."""
        self.menu_frame.pack_forget()  # Hide the main menu
        self.view_predefined_pizzas()  # Show predefined pizzas window

    def on_exit(self):
        """Callback to confirm exit and close the application."""
        exit_confirm = messagebox.askyesno("Exit", "Are you sure you want to exit?")
        if exit_confirm:
            self.root.quit()

    def create_menu_window(self):
        # Create the menu window with options for custom pizza creation
        self.menu_frame = tk.Frame(self.root)
        self.menu_frame.pack(padx=20, pady=20)

        # Size Selection
        tk.Label(self.menu_frame, text="Select Pizza Size:").grid(row=0, column=0, sticky="w")
        sizes = ["Small", "Medium", "Large"]
        for idx, size in enumerate(sizes):
            tk.Radiobutton(self.menu_frame, text=size, variable=self.size, value=size).grid(row=1, column=idx, sticky="w")

        # Crust Selection
        tk.Label(self.menu_frame, text="Select Crust Type:").grid(row=2, column=0, sticky="w")
        crusts = ["Thin", "Stuffed", "Pan"]
        for idx, crust in enumerate(crusts):
            tk.Radiobutton(self.menu_frame, text=crust, variable=self.crust, value=crust).grid(row=3, column=idx, sticky="w")

        # Sauce Selection
        tk.Label(self.menu_frame, text="Select Sauce:").grid(row=4, column=0, sticky="w")
        sauces = ["Tomato", "BBQ", "Alfredo"]
        for idx, sauce in enumerate(sauces):
            tk.Radiobutton(self.menu_frame, text=sauce, variable=self.sauce, value=sauce).grid(row=5, column=idx, sticky="w")

        # Cheese Selection
        tk.Label(self.menu_frame, text="Select Cheese:").grid(row=6, column=0, sticky="w")
        cheeses = ["Mozzarella", "Cheddar", "Parmesan"]
        for idx, cheese in enumerate(cheeses):
            tk.Radiobutton(self.menu_frame, text=cheese, variable=self.cheese, value=cheese).grid(row=7, column=idx, sticky="w")

        # Topping Selection
        tk.Label(self.menu_frame, text="Select Toppings:").grid(row=8, column=0, sticky="w")
        toppings = ["Pepperoni", "Mushrooms", "Olives", "Onions", "Bacon"]
        
        # Create a BooleanVar for each topping to track the state of each checkbox
        for idx, topping in enumerate(toppings):
            var = tk.BooleanVar()
            chk = tk.Checkbutton(self.menu_frame, text=topping, variable=var)
            chk.grid(row=9, column=idx, sticky="w")
            self.topping_vars.append(var)  # Store the BooleanVar for later use

        # Submit Button
        tk.Button(self.menu_frame, text="Proceed to Order", command=self.on_create_order_summary).grid(row=10, column=0, columnspan=3, pady=10)

    def view_predefined_pizzas(self):
        # Create the predefined pizzas window
        self.predefined_frame = tk.Frame(self.root)
        self.predefined_frame.pack(padx=20, pady=20)

        # Predefined pizza options (hardcoded with sizes)
        predefined_pizzas = [
            ("Margherita", ["Small", "Medium", "Large"], "Thin", "Tomato", "Mozzarella", ["Olives", "Onions"]),
            ("Pepperoni", ["Small", "Medium", "Large"], "Pan", "Tomato", "Mozzarella", ["Pepperoni", "Olives"]),
            ("Veggie", ["Small", "Medium", "Large"], "Stuffed", "Tomato", "Mozzarella", ["Mushrooms", "Olives", "Onions"])
        ]

        row = 0
        for pizza in predefined_pizzas:
            pizza_name = pizza[0]
            sizes = pizza[1]
            
            tk.Label(self.predefined_frame, text=f"{pizza_name}").grid(row=row, column=0, pady=10, sticky="w")
            row += 1
            for size in sizes:
                tk.Button(self.predefined_frame, text=f"Size: {size}", command=lambda p=pizza, s=size: self.on_create_predefined_order(p, s)).grid(row=row, column=0, pady=5)
                row += 1

        # Button to go back to the main menu
        tk.Button(self.predefined_frame, text="Back to Main Menu", command=self.on_back_to_main_menu).grid(row=row, column=0, pady=10)

    def on_create_predefined_order(self, pizza, size):
        """Callback to create order from predefined pizza."""
        self.predefined_frame.pack_forget()  # Hide predefined pizza options
        self.on_create_order_summary(pizza, size)  # Display predefined pizza order summary

    def on_create_order_summary(self, pizza=None, size=None):
        """Callback to create the order summary."""
        # Close the menu window
        self.menu_frame.pack_forget()

        # Create the order summary window
        self.order_frame = tk.Frame(self.root)
        self.order_frame.pack(padx=20, pady=20)

        # Show the order details
        tk.Label(self.order_frame, text="Your Pizza Order Summary:").grid(row=0, column=0, sticky="w", pady=5)
        if pizza and size:
            tk.Label(self.order_frame, text=f"Name: {pizza[0]}").grid(row=1, column=0, sticky="w")
            tk.Label(self.order_frame, text=f"Size: {size}").grid(row=2, column=0, sticky="w")
            tk.Label(self.order_frame, text=f"Crust: {pizza[2]}").grid(row=3, column=0, sticky="w")
            tk.Label(self.order_frame, text=f"Sauce: {pizza[3]}").grid(row=4, column=0, sticky="w")
            tk.Label(self.order_frame, text=f"Cheese: {pizza[4]}").grid(row=5, column=0, sticky="w")
            selected_toppings = ', '.join(pizza[5]) if pizza[5] else "None"
            tk.Label(self.order_frame, text=f"Toppings: {selected_toppings}").grid(row=6, column=0, sticky="w")
            price = self.calculate_price(size, pizza[2], len(pizza[5]))
        else:
            tk.Label(self.order_frame, text=f"Size: {self.size.get()}").grid(row=1, column=0, sticky="w")
            tk.Label(self.order_frame, text=f"Crust: {self.crust.get()}").grid(row=2, column=0, sticky="w")
            tk.Label(self.order_frame, text=f"Sauce: {self.sauce.get()}").grid(row=3, column=0, sticky="w")
            tk.Label(self.order_frame, text=f"Cheese: {self.cheese.get()}").grid(row=4, column=0, sticky="w")
            selected_toppings = [topping for idx, topping in enumerate(["Pepperoni", "Mushrooms", "Olives", "Onions", "Bacon"]) if self.topping_vars[idx].get()]
            if selected_toppings:
                tk.Label(self.order_frame, text=f"Toppings: {', '.join(selected_toppings)}").grid(row=5, column=0, sticky="w")
            else:
                tk.Label(self.order_frame, text="Toppings: None").grid(row=5, column=0, sticky="w")
            price = self.calculate_price(self.size.get(), self.crust.get(), len(selected_toppings))

        tk.Label(self.order_frame, text=f"Total Price: ${price:.2f}").grid(row=7, column=0, sticky="w", pady=10)

        # Button to place order
        tk.Button(self.order_frame, text="Place Order", command=self.on_place_order).grid(row=8, column=0, pady=5)

        # Button to go back to menu
        tk.Button(self.order_frame, text="Back to Menu", command=self.on_back_to_menu).grid(row=8, column=1, pady=5)

    def calculate_price(self, size, crust, num_toppings):
        """Calculate the price based on size, crust, and number of toppings."""
        size_prices = {"Small": 5, "Medium": 7, "Large": 9}
        crust_prices = {"Thin": 1, "Stuffed": 2, "Pan": 1.5}
        topping_price = 1.5

        price = size_prices.get(size, 0) + crust_prices.get(crust, 0)
        price += num_toppings * topping_price  # Add topping price

        return price

    def on_place_order(self):
        """Callback for placing the order."""
        messagebox.showinfo("Order Placed", "Your pizza order has been placed successfully!")
        self.root.quit()

    def on_back_to_menu(self):
        """Callback to go back to the custom pizza menu."""
        self.order_frame.pack_forget()
        self.create_menu_window()

    def on_back_to_main_menu(self):
        """Callback to go back to the main menu."""
        self.predefined_frame.pack_forget()
        self.create_main_menu_window()

# Create the root window
root = tk.Tk()

# Create the PizzaOrderApp instance
app = PizzaOrderApp(root)

# Start the Tkinter event loop
root.mainloop()
