from model.Product import Product
from tool.DataConnector import MongoDBConnection


class ProductDAL:
    def __init__(self):
        self.list_product = []
        self.connector = MongoDBConnection()
    def get_list_product(self):
        list_product = self.connector.connect("products_data").find({})
        for product in list_product:
            product_id = product["ProductID"]
            name = product["Name"]
            quantity = product["Quantity"]
            unit_price = product["UnitPrice"]
            category = product["Category"]
            import_date = product["ImportDate"]
            status = product["Status"]
            expiration_date = product["ExpirationDate"]
            minimum_stock = product["MinimumStock"]
            current_product = Product(id=product_id, name=name, quantity=quantity, unit_price=unit_price,
                                      category=category, import_date=import_date, status=status,
                                      expiration_date=expiration_date, minimum_stock=minimum_stock)
            self.list_product.append(current_product)
        return self.list_product
    def get_product_by_id(self, id):
        self.list_product = self.get_list_product()
        temp_product = None
        for product in self.list_product:
            if product.id == id:
                temp_product = product
                break
        return temp_product
    def get_product_by_name(self, name):
        self.list_product = self.get_list_product()
        temp_product = None
        for product in self.list_product:
            if product.name == name:
                temp_product = product
                break
        return temp_product
