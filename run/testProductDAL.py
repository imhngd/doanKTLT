from main.ProductDAL import ProductDAL

product_dal = ProductDAL()
product_dal.update_quantity_product("FD009", 2)
print("successfully")