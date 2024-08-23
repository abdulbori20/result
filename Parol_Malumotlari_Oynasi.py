from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from database.connection import get_connection
import styles

class Parol_Malumotlarini_Ozgartirish_Oynasi(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Parol Ma’lumotlarini O’zgartirish Oynasi")
        self.setMinimumSize(800, 600)

        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(["ID", "Sayt Nomi", "Login/User", "Parol", "Yaratilgan Sana"])

        self.parol_malumotlari_list = QTableView(self)
        self.parol_malumotlari_list.setModel(self.model)

        self.load_data()

        self.parol_malumotlarini_ozgartirish_btn = QPushButton("Ma’lumotlarni O’zgartirish")
        self.parol_malumotlarini_ozgartirish_btn.setStyleSheet(styles.qidirishbtn_styles)
        self.parol_malumotlarini_ozgartirish_btn.clicked.connect(self.malumotlarni_ozgartir)

        vertical = QVBoxLayout()
        vertical.addWidget(self.parol_malumotlari_list)
        vertical.addWidget(self.parol_malumotlarini_ozgartirish_btn)
        self.setLayout(vertical)

    def load_data(self):
        connection = get_connection()
        if connection is not None:
            try:
                cursor = connection.cursor()
                cursor.execute("""
                    SELECT id, sayt_name, login_user, password, created_date
                    FROM passwords
                """)
                rows = cursor.fetchall()
                self.model.setRowCount(0)
                for row in rows:
                    row_items = [QStandardItem(str(field)) for field in row]
                    self.model.appendRow(row_items)

                cursor.close()
                connection.close()
            except Exception as e:
                QMessageBox.critical(self, "Xato Oynasi", f"Ma'lumotlarni yuklashda xato yuz berdi: {e}")
        else:
            QMessageBox.critical(self, "Xato Oynasi", "Ma'lumotlar bazasiga ulanishda xato yuz berdi.")

    def malumotlarni_ozgartir(self):
        connection = get_connection()
        if connection is not None:
            try:
                cursor = connection.cursor()
                for row in range(self.model.rowCount()):
                    id_item = self.model.item(row, 0)
                    sayt_item = self.model.item(row, 1)
                    login_item = self.model.item(row, 2)
                    parol_item = self.model.item(row, 3)
                    yaratilgan_sana_item = self.model.item(row, 4)

                    if id_item is not None:
                        cursor.execute("""
                            UPDATE passwords
                            SET sayt_name = %s, login_user = %s, password = %s, created_date = %s
                            WHERE id = %s
                        """, (sayt_item.text(), login_item.text(), parol_item.text(), yaratilgan_sana_item.text(), id_item.text()))

                connection.commit()
                cursor.close()
                connection.close()

                QMessageBox.information(self, "Saqlash Oynasi", "O'zgartirishlar muvaffaqiyatli saqlandi.")
            except Exception as e:
                QMessageBox.critical(self, "Xato Oynasi", f"O'zgartirishlarni saqlashda xato yuz berdi: {e}")
        else:
            QMessageBox.critical(self, "Xato Oynasi", "Ma'lumotlar bazasiga ulanishda xato yuz berdi.")
