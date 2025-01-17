import tkinter as tk
def choose():
    
    categories = ["Soups", "Starters", "Biryanis", "Desserts"]

    items = {
        "Soups": [
            {"name": "Tomato Soup", "price": 5.99},
            {"name": "Mushroom Soup", "price": 6.99},
            {"name": "Chicken Noodle Soup", "price": 7.99},
        ],
        "Starters": [
            {"name": "Garlic Bread", "price": 4.99},
            {"name": "Chicken Wings", "price": 8.99},
            {"name": "Mozzarella Sticks", "price": 6.49},
        ],
        "Biryanis": [
            {"name": "Chicken Biryani", "price": 350},
            {"name": "Vegetable Biryani", "price": 250},
            {"name": "Mutton Biryani", "price": 400},
        ],
        "Desserts": [
            {"name": "Gulab Jamun", "price": 50},
            {"name": "Rasgulla", "price": 60},
            {"name": "Ice Cream", "price": 70},
        ]
    }

    selected_items = {category: {} for category in categories}
    global current_category_index 
    current_category_index=0

    def add_to_bill():
        current_category = categories[current_category_index]
        selected_index = listbox.curselection()
        
        if selected_index:
            index = selected_index[0]
            selected_item = items[current_category][index]
            name = selected_item["name"]
            price = selected_item["price"]
            quantity = int(quantity_var.get())

            if name in selected_items[current_category]:
                selected_items[current_category][name]["quantity"] += quantity
            else:
                selected_items[current_category][name] = {"price": price, "quantity": quantity}

            update_bill_listbox()
            update_total()

    def update_bill_listbox():
        current_category = categories[current_category_index]
        bill_listbox.delete(0, tk.END)
        for name, item_data in selected_items[current_category].items():
            price = item_data["price"]
            quantity = item_data["quantity"]
            total_price = price * quantity
            bill_listbox.insert(tk.END, f"{name} x{quantity} - ₹{total_price}")

    def update_total():
        total = sum(sum(item_data["price"] * item_data["quantity"] for item_data in items.values()) for items in selected_items.values())
        total_var.set(f"Total: ₹{total}")

    def next_category():
        
        current_category_index += 1
        if current_category_index < len(categories):
            current_category = categories[current_category_index]
            listbox.delete(0, tk.END)
            for item in items[current_category]:
                listbox.insert(tk.END, item["name"])
            if current_category == "Soups":
                category_label.config(text="Choose any three soups from below:",bg = "white")
            elif current_category == "Starters":
                category_label.config(text="Choose any two starters from below:",bg="white")
            else:
                category_label.config(text=f"Category: {current_category}")
            next_button.config(state=tk.DISABLED)
            back_button.config(state=tk.NORMAL)
            update_bill_listbox()
            update_total()
        if current_category_index == len(categories) - 1:
            next_button.config(text="Finish", command=root.quit)

    def previous_category():
        
        current_category_index -= 1
        if current_category_index >= 0:
            current_category = categories[current_category_index]
            listbox.delete(0, tk.END)
            for item in items[current_category]:
                listbox.insert(tk.END, item["name"])
            if current_category == "Soups":
                category_label.config(text="Choose any three soups from below:")
            elif current_category == "Starters":
                category_label.config(text="Choose any two starters from below:")
            else:
                category_label.config(text=f"Category: {current_category}")
            next_button.config(state=tk.NORMAL)
            back_button.config(state=tk.NORMAL)
            if current_category_index == 0:
                back_button.config(state=tk.DISABLED)
            update_bill_listbox()
            update_total()

    
    root = tk.Tk()
    root.title("Restaurant Menu")
    root.configure(bg='#D2B48C')
    window_width = 500
    window_height = 400
    x = 550
    y = 150
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")


    category_frame = tk.Frame(root)
    category_frame.pack()
    category_frame.configure(bg="#D2B48C")

    category_label = tk.Label(category_frame, text="Choose any three soups from below",bg="white")
    category_label.pack()

    listbox = tk.Listbox(category_frame, selectmode=tk.SINGLE, height=5)
    listbox.pack(pady=10)

    
    quantity_label = tk.Label(category_frame, text="Quantity:")
    quantity_label.pack()
    quantity_var = tk.IntVar()
    quantity_entry = tk.Entry(category_frame, textvariable=quantity_var)
    quantity_entry.pack()


    add_button = tk.Button(category_frame, text="Add to Bill", command=add_to_bill)
    add_button.pack()

    
    bill_listbox = tk.Listbox(category_frame, selectmode=tk.SINGLE, height=5)
    bill_listbox.pack(pady=10)

    
    next_button = tk.Button(category_frame, text="Next", command=next_category)
    next_button.pack(side=tk.RIGHT)

    
    back_button = tk.Button(category_frame, text="Back", command=previous_category, state=tk.DISABLED)
    back_button.pack(side=tk.LEFT)


    total_frame = tk.Frame(root)
    total_frame.pack()

    
    total_var = tk.StringVar()
    total_var.set("Total: ₹0")
    total_label = tk.Label(total_frame, textvariable=total_var)
    total_label.pack()


    current_category = categories[current_category_index]
    for item in items[current_category]:
        listbox.insert(tk.END, item["name"])

    root.mainloop()
