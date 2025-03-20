from model.Order import Order
from tool.DataConnector import MongoDBConnection


class OrderDAL:
    def __init__(self):
        self.list_order = []
        self.connector = MongoDBConnection()
    def get_list_order(self):
        list_order = self.connector.connect("order").find({})
        for order in list_order:
            order_id = order["order_id"]
            date_order = order["date_order"]
            list_product = order["list_product"]
            status = order["status"]
            customer_name = order["customer_name"]
            contact_no = order["contact_no"]
            total = order["total"]
            current_order = Order(order_id, date_order, list_product, status, customer_name, contact_no, total)
            self.list_order.append(current_order)
        return self.list_order
    def store_order(self, new_order):
        collection = self.connector.connect("order")
        collection.insert_one(new_order.__dict__)
    def get_order_by_id(self, order_id):
        self.list_order = self.get_list_order()
        temp_order = None
        for order in self.list_order:
            if order.order_id == order_id:
                temp_order = order
                break
        return temp_order
    def change_status(self, id):
        collection = self.connector.connect("order")
        collection.update_one({"order_id": id}, {"$set": {"status": "Confirmed"}})

