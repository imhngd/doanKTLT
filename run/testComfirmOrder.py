from PyQt6.QtWidgets import QApplication, QMainWindow

from main.confirm_order import ComfirmOrder

app = QApplication([])
MainWindow = QMainWindow()
mp = ComfirmOrder()
mp.setupUi(MainWindow)
mp.show()
app.exec()