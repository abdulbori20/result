import mysql.connector
from mysql.connector import Error
from PyQt5.QtWidgets import *
import styles

import string
import random

from database.database_main import *


class Yangi_Parol_Qoshish_Oynasi(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Yangi Parol Qo'shish Oynasi")
        self.setMinimumSize(800, 600)

        ####1
        self.Sayt_yoki_Programma_Nomi_label = QLabel("Sayt yoki Programma Nomi")
        self.Sayt_yoki_Programma_Nomi_label.setStyleSheet(styles.labels_styles)

        self.Sayt_yoki_Programma_Nomi_input = QLineEdit()
        self.Sayt_yoki_Programma_Nomi_input.setStyleSheet(styles.lines_style)
        self.Sayt_yoki_Programma_Nomi_input.setPlaceholderText("Enter Programm name")
        ####1

        ####2
        self.Login_yoki_Username_label = QLabel("Login yoki Username")
        self.Login_yoki_Username_label.setStyleSheet(styles.labels_styles)

        self.Login_yoki_Username_input = QLineEdit()
        self.Login_yoki_Username_input.setStyleSheet(styles.lines_style)
        self.Login_yoki_Username_input.setPlaceholderText("Enter Login or Username")
        ####2

        ####3
        self.Parol_label = QLabel("Parol")
        self.Parol_label.setStyleSheet(styles.labels_styles)

        self.Parol_input = QLineEdit()
        self.Parol_input.setStyleSheet(styles.lines_style)
        self.Parol_input.setPlaceholderText("Enter Password")

        self.generatsiya_parol = QPushButton("Password Generation")
        self.generatsiya_parol.setStyleSheet(styles.buttons_styles)
        self.generatsiya_parol.clicked.connect(self.parolni_generatsiya_qil)
        ####3

        ####4
        self.Yaratilgan_Sana_label = QLabel("Yaratilgan Sana")
        self.Yaratilgan_Sana_label.setStyleSheet(styles.labels_styles)

        self.Yaratilgan_Sana_input = QLineEdit()
        self.Yaratilgan_Sana_input.setStyleSheet(styles.lines_style)
        self.Yaratilgan_Sana_input.setPlaceholderText("Enter Created Date")
        ####4

        ####5
        self.Malumotlarni_saqlash_btn = QPushButton("Ma'lumotlarni Saqlash")
        self.Malumotlarni_saqlash_btn.setStyleSheet(styles.buttons_styles)
        self.Malumotlarni_saqlash_btn.clicked.connect(self.malumotlarni_saqla)
        ####5

        container = QHBoxLayout()
        container.addWidget(self.Parol_input)
        container.addWidget(self.generatsiya_parol)

        vertical = QVBoxLayout()
        vertical.addWidget(self.Sayt_yoki_Programma_Nomi_label)
        vertical.addWidget(self.Sayt_yoki_Programma_Nomi_input)

        vertical.addWidget(self.Login_yoki_Username_label)
        vertical.addWidget(self.Login_yoki_Username_input)

        vertical.addWidget(self.Parol_label)
        vertical.addLayout(container)

        vertical.addWidget(self.Yaratilgan_Sana_label)
        vertical.addWidget(self.Yaratilgan_Sana_input)

        vertical.addWidget(self.Malumotlarni_saqlash_btn)

        widget = QWidget()
        widget.setLayout(vertical)

        self.setCentralWidget(widget)

    def parolni_generatsiya_qil(self):
        length = 12
        characters = string.ascii_letters + string.digits + string.punctuation
        random_password = ''.join(random.choice(characters) for _ in range(length))
        self.Parol_input.setText(random_password)

    def malumotlarni_saqla(self):
        connection = init_db()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute("""
                    INSERT INTO passwords(sayt_name, login_user, password)
                        VALUES(%s, %s, %s)
                """, (
                    self.Sayt_yoki_Programma_Nomi_input.text(),
                    self.Login_yoki_Username_input.text(),
                    self.Parol_input.text()))

                connection.commit()
                cursor.close()
                connection.close()

                QMessageBox.information(self, "Saqlash Oynasi", "Ma'lumotlar muvaffaqiyatli saqlandi.")
            except Error as e:
                QMessageBox.critical(self, "Xato Oynasi", f"Ma'lumotlarni saqlashda xato yuz berdi: {e}")
        else:
            QMessageBox.critical(self, "Xato Oynasi", "Ma'lumotlar bazasiga ulanishda xato yuz berdi.")