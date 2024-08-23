from PyQt5.QtWidgets import *
from database.database_main import init_db
import styles


from Yangi_parol import *
from Sayt_Nomi_Qidirish import *
from Login_Oynasi import *
from Parol_Malumotlari import *

app = QApplication([])
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Asosiy Oyna")
        self.setMinimumSize(500, 500)

        self.oynalar = []

        self.Parol_Qoshish = QPushButton("Yangi Parol Qo’shish")
        self.Parol_Qoshish.clicked.connect(self.yangi_Parol_Qoshish)

        self.Sayt_Nomiga_Kora_Qidirish = QPushButton("Sayt Nomiga Ko’ra Qidirish")
        self.Sayt_Nomiga_Kora_Qidirish.clicked.connect(self.sayt_nomini_qidirish)

        self.Login_Boyicha_Qidirish = QPushButton("Login Bo’yicha Qidirish")
        self.Login_Boyicha_Qidirish.clicked.connect(self.loginni_qidirish)

        self.Parol_Malumotlarini_Ozgartirish = QPushButton("Parol Ma’lumotlarini O’zgartirish")
        self.Parol_Malumotlarini_Ozgartirish.clicked.connect(self.parol_malumotlarini_Ozgartir)

        try:
            self.setStyleSheet(styles.asosiy_oyna_buttonlari)
        except AttributeError:
            print("Still berishda xato sodir boldi.")

        vertical = QVBoxLayout()
        vertical.addWidget(self.Parol_Qoshish)
        vertical.addWidget(self.Sayt_Nomiga_Kora_Qidirish)
        vertical.addWidget(self.Login_Boyicha_Qidirish)
        vertical.addWidget(self.Parol_Malumotlarini_Ozgartirish)

        widget = QWidget()
        widget.setLayout(vertical)

        self.setCentralWidget(widget)

    def yangi_Parol_Qoshish(self):
        yangi_oyna = Yangi_Parol_Qoshish_Oynasi()
        yangi_oyna.show()
        self.oynalar.append(yangi_oyna)

    def sayt_nomini_qidirish(self):
        sayt_nomi_qidirish = Sayt_Nomiga_Kora_Qidirish_Oynasi()
        sayt_nomi_qidirish.show()
        self.oynalar.append(sayt_nomi_qidirish)

    def loginni_qidirish(self):
        login_oyna = Login_Boyicha_Qidirish_Oynasi()
        login_oyna.show()
        self.oynalar.append(login_oyna)

    def parol_malumotlarini_Ozgartir(self):
        parol_oyna = Parol_Malumotlarini_Ozgartirish_Oynasi()
        parol_oyna.show()
        self.oynalar.append(parol_oyna)

init_db()

main = MainWindow()
main.show()


app.exec_()


