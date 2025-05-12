from datetime import datetime

class Money:
    def __init__(self, dollars=0, cents=0):
        if dollars < 0 or cents < 0:
            raise ValueError("Error")
        self.dollars = dollars
        self.cents = cents

    def display(self):
        print(f"${self.dollars}.{self.cents:02d}")

    def set_amount(self, dollars, cents):
        if dollars < 0 or cents < 0:
            raise ValueError("Error")
        self.dollars = dollars
        self.cents = cents

class Product:
    def __init__(self, name, price):
        if price < 0:
            raise ValueError("Error")
        self.name = name
        self.price = price

    def apply_discount(self, amount):
        if amount < 0:
            raise ValueError("Error.")
        self.price -= amount
        if self.price < 0:
            self.price = 0

class Warehouse:
    def __init__(self, name, unit, price, quantity):
        if quantity < 0:
            raise ValueError("Error")
        self.name = name
        self.unit = unit
        self.price = price
        self.quantity = quantity
        self.last_delivery = datetime.now()

    def update_quantity(self, quantity):
        if quantity < 0:
            raise ValueError("Error")
        self.quantity += quantity

class Reporting:
    def __init__(self):
        self.reports = []

    def add_report(self, report_type, product, quantity):
        if quantity < 0:
            raise ValueError("Error")
        self.reports.append({
            "type": report_type,
            "product": product.name,
            "quantity": quantity,
            "date": datetime.now()
        })

    def show_reports(self):
        for report in self.reports:
            print(f"{report['type']} {report['product']} - {report['quantity']} units on {report['date']}")

def main():
    money = Money(100, 50)
    money.display()

    product = Product("Laptop", 1500)
    product.apply_discount(200)
    print(f"Price after discount: {product.price}")

    warehouse = Warehouse("Laptop", "pcs", 1300, 50)
    warehouse.update_quantity(20)
    print(f"Quantity in warehouse: {warehouse.quantity}")

    reporting = Reporting()
    reporting.add_report("incoming", product, 20)
    reporting.add_report("outgoing", product, 10)
    reporting.show_reports()

if __name__ == "__main__":
    main()
