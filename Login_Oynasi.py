from PyQt5.QtWidgets import *
import styles


class Login_Boyicha_Qidirish_Oynasi(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login Bo’yicha Qidirish Oynasi")
        self.setMinimumSize(800, 600)

        self.Login_Boyicha_Qidirish_label = QLabel("Login Bo’yicha Qidirish")
        self.Login_Boyicha_Qidirish_label.setStyleSheet(styles.labels_styles)

        self.Login_Boyicha_Qidirish_input = QLineEdit()
        self.Login_Boyicha_Qidirish_input.setStyleSheet(styles.lines_style)
        self.Login_Boyicha_Qidirish_input.setPlaceholderText("Enter Login")

        self.login_list = QTableView()

        self.qidirish_btn = QPushButton("Qidirish")
        self.qidirish_btn.setStyleSheet(styles.qidirishbtn_styles)

        vertical = QVBoxLayout()
        vertical.addWidget(self.Login_Boyicha_Qidirish_label)
        vertical.addWidget(self.Login_Boyicha_Qidirish_input)

        vertical.addWidget(self.qidirish_btn)

        vertical.addWidget(self.login_list)

        widget = QWidget()
        widget.setLayout(vertical)

        self.setCentralWidget(widget)