class Product:
    def __init__(self, id, name, quantity, unit_price, category, import_date, status, expiration_date, minimum_stock):
        self.id = id
        self.name = name
        self.quantity = quantity
        self.unit_price = unit_price
        self.quantity = quantity
        self.category = category
        self.status = status
        self.expiration_date = expiration_date
        self.minimum_stock = minimum_stock
        self.import_date = import_date
    def __str__(self):
        info = f"Information Product: \n +id: {self.id} \n +name: {self.name} \n +quantity: {self.quantity} \n +unit_price: {self.unit_price}"
        return info