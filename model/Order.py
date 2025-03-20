class Order:
    def __init__(self, order_id, date_order, list_product, status, customer_name, contact_no, total):
        self.order_id = order_id
        self.date_order = date_order
        self.list_product = list_product
        self.status = status
        self.customer_name = customer_name
        self.contact_no = contact_no
        self.total = total
    def __str__(self):
        info = f"List product: {self.list_product}"
        return info

