# online store example from the TK
from datetime import datetime
# creating a User


class User:
    def __init__(self, name, is_admin=False):
        self.name = name
        self.is_admin = is_admin


# User types! Admin, Customer, and Vendor

class Admin(User):
    def __init__(self, name):
        super().__init__(name, is_admin=True)


class Customer(User):
    def __init__(self, name):
        super().__init__(name)
        self.purchases = []

    def purchase_product(self, product):
        purchase = Purchase(product, self)
        self.purchases.append(purchase)


class Vendor(User):
    def __init__(self, name):
        super().__init__(name)
        self.products = []

    def create_product(self, product_name, product_price):
        product = Product(product_name, product_price, self)
        self.products.append(product)

# Products and Purchases


class Product:
    def __init__(self, name, price, vendor):
        self.name = name
        self.price = price
        self.vendor = vendor


class Purchase:
    def __init__(self, product, customer):
        self.product = product
        self.customer = customer
        self.purchase_price = product.price
        self.purchase_data = datetime.now()
