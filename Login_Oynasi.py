from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import styles
from database.connection import get_connection

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

        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(["Sayt Nomi", "Login/User", "Parol", "Yaratilgan Sana"])

        self.login_list = QTableView()
        self.login_list.setModel(self.model)


        self.qidirish_btn = QPushButton("Qidirish")
        self.qidirish_btn.setStyleSheet(styles.qidirishbtn_styles)
        self.qidirish_btn.clicked.connect(self.login_qidir)

        vertical = QVBoxLayout()
        vertical.addWidget(self.Login_Boyicha_Qidirish_label)
        vertical.addWidget(self.Login_Boyicha_Qidirish_input)

        vertical.addWidget(self.qidirish_btn)

        vertical.addWidget(self.login_list)

        widget = QWidget()
        widget.setLayout(vertical)

        self.setCentralWidget(widget)

    def login_qidir(self):
        query = self.Login_Boyicha_Qidirish_input.text().strip()
        if query:
            connection = get_connection()
            if connection.is_connected():
                try:
                    cursor = connection.cursor()
                    query_string = """
                        SELECT sayt_name, login_user, password, created_date
                        FROM passwords
                        WHERE login_user LIKE %s
                    """
                    cursor.execute(query_string, ('%' + query + '%',))

                    qatorlar = cursor.fetchall()
                    self.model.setRowCount(0)
                    for qator in qatorlar:
                        qator_items = [QStandardItem(str(field)) for field in qator]
                        self.model.appendRow(qator_items)

                    cursor.close()
                    connection.close()
                except Exception as e:
                    QMessageBox.critical(self, "Xato Oynasi", f"Qidirishta xato yuz berdi: {e}")
            else:
                QMessageBox.critical(self, "Xato Oynasi", "Ma'lumotlar bazasiga ulanishda xato yuz berdi.")