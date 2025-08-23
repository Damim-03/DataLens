import sys
from PyQt6.QtWidgets import QApplication

from model.data_model import DataModel
from view.main_view import MainView
from controller.main_controller import MainController

if __name__ == "__main__":
    app = QApplication(sys.argv)

    model = DataModel()
    view = MainView()
    controller = MainController(model, view)

    view.show()
    sys.exit(app.exec())
