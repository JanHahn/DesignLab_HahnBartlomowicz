import sys
from PyQt5.QtWidgets import (QMainWindow, QApplication, QLabel, QPushButton, QStackedWidget, QWidget, QRadioButton,
                             QHBoxLayout,
                             QVBoxLayout, QSizePolicy, QSpacerItem, QLineEdit, QGridLayout)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

#from enter_email import EnterEmail
from locked_successfully import LockSuccess
from mail_sender import send_email
import random


class EmailConfirmation(QWidget):
    def __init__(self, email, queue, backend_info, queue2):
        super().__init__()

        self.backend_info = backend_info
        self.queue = queue
        self.queue2 = queue
        #self.showFullScreen()
        self.windowWidth = 1024
        self.windowHeight = 600
        self.email = email
        self.widget = LockSuccess()
        self.showFullScreen()


        # Creating label, line edit and buttons needed
        self.label = QLabel("Make sure the email is correct")
        self.email_label = QLabel(email)
        self.lock_button = QPushButton("YES, LOCK IN!")
        self.return_button = QPushButton("BACK")

        self.init_ui()
        self.layaout_managment()
        self.buttons_size_policy()
        self.disabling_lock_button()
        self.connecting_buttons()



    def init_ui(self):
        self.setStyleSheet("background-color: #2d2d2d;")
        self.setGeometry(0, 0, self.windowWidth, self.windowHeight)

        self.label.setFont(QFont("Helvetica", 25))
        self.label.setStyleSheet("color: white;"
                            "font-weight: bold;")
        self.label.setAlignment(Qt.AlignCenter | Qt.AlignHCenter)

        self.email_label.setFont(QFont("Helvetica", 25))
        self.email_label.setStyleSheet("color: lightgrey;"
                                 "font-weight: bold;")
        self.email_label.setAlignment(Qt.AlignCenter | Qt.AlignHCenter)

        self.return_button.setStyleSheet("font-size: 25px;"
                                         "color: #f4f3f0;"
                                         "font-weight: bold;"
                                         "background-color: #162f42")

        self.lock_button.setStyleSheet("font-size: 25px;"
                                         "color: white;"
                                         "font-weight: bold;"
                                         "background-color: #6A1B1B;")

    def buttons_size_policy(self):
        self.lock_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.lock_button.setMinimumHeight(40)




    def layaout_managment(self):
        button_layout = QHBoxLayout()
        button_layout.addStretch(1)
        button_layout.addWidget(self.lock_button, stretch=3)
        button_layout.addStretch(1)

        back_button_layout = QHBoxLayout()
        back_button_layout.addStretch(1)
        back_button_layout.addWidget(self.return_button, stretch=3)
        back_button_layout.addStretch(1)

        main_layout = QVBoxLayout()
        main_layout.addStretch(1)
        main_layout.addWidget(self.label)
        main_layout.addStretch(1)
        main_layout.addWidget(self.email_label)
        main_layout.addStretch(2)
        main_layout.addLayout(button_layout, stretch=3)
        main_layout.addStretch(1)
        main_layout.addLayout(back_button_layout, stretch=2)
        main_layout.addStretch(1)

        self.setLayout(main_layout)

    def disabling_lock_button(self):
        if self.email == "No email provided":
            self.lock_button.setDisabled(True)

    def connecting_buttons(self):
        self.lock_button.clicked.connect(self.lock_clicked)
        self.return_button.clicked.connect(self.back_clicked)

    def lock_clicked(self):
        self.queue.put(self.backend_info)
        self.widget.showFullScreen()
        #self.widget.resize(1024, 600)
        new_code = random.randint(1000, 9999)

        send_email(
            sender_email='designlab.locker@gmail.com',
            receiver_email = self.email,  # Dodano przecinek po liście adresów e-mail
            subject='Design Lab Locker',
            body=f'Hello, your unlock code is {new_code} ',
            smtp_server='smtp.gmail.com',  # Adres serwera SMTP (np. dla Gmail: 'smtp.gmail.com')
            port=587,  # Port SMTP (np. dla Gmail: 587)
            login='designlab.locker@gmail.com',
            password='ddfg hdzm ombs faof'
        )

        self.queue.put("new_code")
        self.queue.put(self.backend_info + str(new_code))  #[lockerid + email + new_code]


    def back_clicked(self):
        self.close()

