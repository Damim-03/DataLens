from PyQt6.QtWidgets import QMainWindow
from modules.ui_main_window import Ui_MainWindow

class MainView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
