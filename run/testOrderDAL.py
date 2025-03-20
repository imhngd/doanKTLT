from main.OrderDAL import OrderDAL

order_dal =OrderDAL()
list_order = order_dal.get_list_order()
for order in list_order:
    print(order)