class MainController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        # ربط الأحداث بالوظائف
        self.view.ui.pushButton.clicked.connect(self.button_clicked)

        # تحديث الواجهة من البيانات الحالية
        self.update_view()

    def button_clicked(self):
        self.model.update_label("تم الضغط!")
        self.update_view()

    def update_view(self):
        self.view.ui.label.setText(self.model.label_text)
