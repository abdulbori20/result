from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from database.database_main import *
import styles
from database.connection import get_connection


class Sayt_Nomiga_Kora_Qidirish_Oynasi(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sayt Nomiga Ko’ra Qidirish Oynasi")
        self.setMinimumSize(800, 600)

        self.Sayt_yoki_Programma_Nomi_label = QLabel("Sayt yoki Programma Nomi")
        self.Sayt_yoki_Programma_Nomi_label.setStyleSheet(styles.labels_styles)

        self.Sayt_yoki_Programma_Nomi_input = QLineEdit()
        self.Sayt_yoki_Programma_Nomi_input.setStyleSheet(styles.lines_style)
        self.Sayt_yoki_Programma_Nomi_input.setPlaceholderText("Enter Site or Programm Name")

        self.Qidirish_btn = QPushButton("Qidirish")
        self.Qidirish_btn.setStyleSheet(styles.qidirishbtn_styles)
        self.Qidirish_btn.clicked.connect(self.Sayt_nomini_qidir)

        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(["Sayt Nomi", "Login/User", "Parol", "Yaratilgan Sana"])

        self.malumotlar_listi = QTableView()
        self.malumotlar_listi.setModel(self.model)

        vertical = QVBoxLayout()
        vertical.addWidget(self.Sayt_yoki_Programma_Nomi_label)
        vertical.addWidget(self.Sayt_yoki_Programma_Nomi_input)

        vertical.addWidget(self.Qidirish_btn)

        vertical.addWidget(self.malumotlar_listi)

        widget = QWidget()
        widget.setLayout(vertical)

        self.setCentralWidget(widget)

    def Sayt_nomini_qidir(self):
        query = self.Sayt_yoki_Programma_Nomi_input.text().strip()
        if query:
            connection = get_connection()
            if connection.is_connected():
                try:
                    cursor = connection.cursor()
                    query_string = """
                        SELECT sayt_name, login_user, password, created_date
                        FROM passwords 
                        WHERE sayt_name LIKE %s
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