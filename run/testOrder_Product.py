from PyQt6.QtWidgets import QApplication, QMainWindow

from main.order_product import OrderProductExt

app = QApplication([])
MainWindow = QMainWindow()
mp = OrderProductExt()
mp.setupUi(MainWindow)
mp.show()
app.exec()




