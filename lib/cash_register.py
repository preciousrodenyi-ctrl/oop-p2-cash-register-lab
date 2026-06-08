class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

    def add_item(self, item, price, quantity=1):
        self.total += price * quantity

        for _ in range(quantity):
            self.items.append(item)

        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity
        })

    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
            return

        self.total = self.total - (self.total * self.discount / 100)

        if self.total == int(self.total):
            total_display = int(self.total)
        else:
            total_display = self.total

        print(f"After the discount, the total comes to ${total_display}.")

    def void_last_transaction(self):
        if not self.previous_transactions:
            return

        last_transaction = self.previous_transactions.pop()

        item = last_transaction["item"]
        price = last_transaction["price"]
        quantity = last_transaction["quantity"]

        self.total -= price * quantity

        for _ in range(quantity):
            if item in self.items:
                self.items.remove(item)
