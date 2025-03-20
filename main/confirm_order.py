from PyQt6.QtWidgets import QTableWidgetItem, QMessageBox

from ui.ComfirmOrder import Ui_MainWindow
from main.OrderDAL import OrderDAL
from main.ProductDAL import ProductDAL


class ComfirmOrder(Ui_MainWindow):
    def __init__(self):
        self.order_dal = OrderDAL()
        self.product_dal = ProductDAL()
        self.list_product = []
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlots()
    def setupSignalAndSlots(self):
        self.pushButtonSearch.clicked.connect(self.search_order)
        self.pushButtonCheckInventory.clicked.connect(self.check_inventory)
        self.pushButtonChangeStatusOrder.clicked.connect(self.change_order_status)
    def clear(self):
        self.lineEditOrderId.setText("")
        self.lineEditId.setText("")
        self.lineEditStatus.setText("")
        self.tableWidgetListProduct.setRowCount(0)
        self.list_product = []
    def change_order_status(self):
        id = self.lineEditOrderId.text()
        self.order_dal.change_status(id)
        msg = QMessageBox()
        msg.setText("Đổi trạng thái thành công")
        msg.setWindowTitle("Thông báo")
        msg.exec()
    def check_inventory(self):
        isChecked = True
        for product in self.list_product:
            need_product = self.product_dal.get_product_by_id(product["id"])
            if product["quantity"] > need_product.quantity:
                isChecked = False
                break
        if isChecked == True:
            msg = QMessageBox()
            msg.setText("Đơn hàng hợp lệ")
            msg.setWindowTitle("Thông báo")
            msg.exec()
        else:
            msg = QMessageBox()
            msg.setText("Đơn hàng không hợp lệ")
            msg.setWindowTitle("Thông báo")
            msg.exec()
    def search_order(self):
        order_id = self.lineEditOrderId.text()
        searched_order = self.order_dal.get_order_by_id(order_id)
        if searched_order == None:
            msg = QMessageBox()
            msg.setText("Không tìm thấy")
            msg.setWindowTitle("thông báo")
        else:
            self.lineEditId.setText(order_id)
            self.lineEditStatus.setText(searched_order.status)
            self.tableWidgetListProduct.setRowCount(0)
            list_product = searched_order.list_product
            for i in range(len(list_product)):
                self.tableWidgetListProduct.insertRow(i)
                current_product = list_product[i]
                self.list_product.append(current_product[0])
                column_id = QTableWidgetItem(current_product[0]["id"])
                column_quantity = QTableWidgetItem(str(current_product[1]))
                column_name = QTableWidgetItem(current_product[0]["name"])
                self.tableWidgetListProduct.setItem(i, 0, column_id)
                self.tableWidgetListProduct.setItem(i, 1, column_quantity)
                self.tableWidgetListProduct.setItem(i, 2, column_name)
    def show(self):
        self.MainWindow.show()
