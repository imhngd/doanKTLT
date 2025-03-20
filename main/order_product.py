from PyQt6.QtCore import QDate
from PyQt6.QtWidgets import QTableWidgetItem, QMessageBox

from ui.OrderProduct import Ui_MainWindow
from main.OrderDAL import OrderDAL
from main.ProductDAL import ProductDAL
from model.Order import Order


class OrderProductExt(Ui_MainWindow):
    def __init__(self):
        self.list_product = []
        self.product_dal = ProductDAL()
        self.order_dal = OrderDAL()
        self.count_row = 0
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlots()
    def setupSignalAndSlots(self):
        self.pushButtonNew.clicked.connect(self.new_order)
        self.pushButtonClear.clicked.connect(self.clear)
        self.pushButtonAdd.clicked.connect(self.add_new_product)
        self.pushButtonTotal.clicked.connect(self.total)
        self.pushButtonGenerate.clicked.connect(self.store_order)
    def store_order(self):
        order_id = f"order{len(self.order_dal.get_list_order())+1}"
        date_order = self.dateEdit.date().toString("dd/MM/yyyy")
        list_product = []
        for product in self.list_product:
            list_product.append([product[0].__dict__, product[1]])
        status = "Chưa xác nhận"
        customer_name = self.lineEditCustomer.text()
        contact_no = self.lineEditPhone.text()
        total = int(self.lineEditTotal.text())
        if customer_name == "" and contact_no == "":
            msg = QMessageBox()
            msg.setText("Điền thiếu thông tin!")
            msg.setWindowTitle("Thông báo")
            msg.exec()
            return
        new_order = Order(order_id, date_order, list_product, status, customer_name, contact_no, total)
        self.order_dal.store_order(new_order)
        msg = QMessageBox()
        msg.setText("Đã tạo đơn hàng")
        msg.setWindowTitle("Thông báo")
        msg.exec()
    def total(self):
        total = 0
        for i in range(len(self.list_product)):
            total += self.list_product[i][0].unit_price * self.list_product[i][1]
        self.lineEditTotal.setText(str(total))
        self.lineEditTax.setText(str(0))
        self.lineEditRest.setText(str(total))
    def add_new_product(self):
        product_name = self.lineEditNameProduct.text()
        quantity = int(self.lineEditQuantity.text())
        needed_product = self.product_dal.get_product_by_name(product_name)
        if needed_product == None:
            msg = QMessageBox()
            msg.setText("Không tìm thấy sản phẩm!!!")
            msg.setWindowTitle("Thông báo")
            msg.exec()
        else:
            self.list_product.append([needed_product, quantity])
            self.tableWidgetListProduct.setRowCount(self.count_row)
            self.tableWidgetListProduct.insertRow(self.count_row)
            column_id = QTableWidgetItem(needed_product.id)
            column_name = QTableWidgetItem(needed_product.name)
            column_quantity = QTableWidgetItem(str(quantity))
            column_unit_price = QTableWidgetItem(str(needed_product.unit_price))
            column_total = QTableWidgetItem(str(quantity*needed_product.unit_price))
            self.tableWidgetListProduct.setItem(self.count_row, 0, column_id)
            self.tableWidgetListProduct.setItem(self.count_row, 1, column_name)
            self.tableWidgetListProduct.setItem(self.count_row, 2, column_quantity)
            self.tableWidgetListProduct.setItem(self.count_row, 3, column_unit_price)
            self.tableWidgetListProduct.setItem(self.count_row, 4, column_total)
            self.count_row += 1
    def new_order(self):
        self.clear()
        self.list_product = []
        self.count_row = 0
        self.tableWidgetListProduct.setRowCount(self.count_row)
        self.lineEditTax.setText("")
        self.lineEditRest.setText("")
        self.lineEditCustomer.setText("")
        self.lineEditPhone.setText("")
        self.lineEditTotal.setText("")
    def clear(self):
        self.lineEditNameProduct.setText("")
        self.lineEditQuantity.setText("")
    def show(self):
        self.dateEdit.setDate(QDate.currentDate())
        self.MainWindow.show()