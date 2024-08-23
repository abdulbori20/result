from PyQt5.QtWidgets import *
import styles


class Parol_Malumotlarini_Ozgartirish_Oynasi(QDialog):
    def __init__(self):
        super().__init__(self)
        self.setWindowTitle("Parol Ma’lumotlarini O’zgartirish Oynasi")
        self.setMinimumSize(800, 600)

        self.parol_malumotlari_list = QTableView()

        self.parol_malumotlarini_ozgartirish_btn = QPushButton("Ma’lumotlarni O’zgartirish")
        self.parol_malumotlarini_ozgartirish_btn.setStyleSheet(styles.qidirishbtn_styles)
        self.parol_malumotlarini_ozgartirish_btn.clicked.connect(self.malumotlarni_ozgartir)

        vertical = QVBoxLayout()
        vertical.addWidget(self.parol_malumotlari_list)

        vertical.addWidget(self.parol_malumotlarini_ozgartirish_btn)

        self.setLayout(vertical)

    def malumotlarni_ozgartir(self):
        pass