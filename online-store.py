from datetime import datetime
# BASE CLASS - USER


class User:
    def __init__(self, name, is_admin=False):
        self.name = name
        self.is_admin = is_admin

# SUBCLASSES - ADMIN, CUSTOMER, VENDOR

# Admin - inherits from User and override default is_admin value


class Admin(User):
    def __init__(self, name):
        super().__init__(name, is_admin=True)

# Customer - inherits from User and add an empty list for purchases
# We also leave is_admin to it's default value, False


class Customer(User):
    def __init__(self, name):
        super().__init__(name)
        self.purchases = []

# Vendor same as Customer, but instead of purchase, an empty list for products


class Vendor(User):
    def __init__(self, name):
        super().__init__(name)
        self.products = []


# PRODUCT AND PURCHASE

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
