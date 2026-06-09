class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        for _ in range(quantity):
            self.items.append(title)
        self.previous_transactions.append({
            "title": title,
            "price": price,
            "quantity": quantity
        })

    def apply_discount(self):
        if not self.previous_transactions:
            print("There is no discount to apply.")
            return
        self.total = self.total * ((100 - self.discount) / 100)
        print(f"Your total after {self.discount}% discount is ${self.total:.2f}.")

    def void_last_transaction(self):
        if not self.previous_transactions:
            return
        last = self.previous_transactions.pop()
        self.total -= last["price"] * last["quantity"]
        for _ in range(last["quantity"]):
            self.items.remove(last["title"])
        if self.total < 0:
            self.total = 0.0


            # Test it
register = CashRegister(20)

register.add_item("Apple", 1.50, 3)
register.add_item("Bread", 2.00)
print(register.total)        
print(register.items)        

register.apply_discount()    

register.void_last_transaction()
print(register.total)        
print(register.items)        