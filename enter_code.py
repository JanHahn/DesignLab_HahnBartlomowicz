import sys
from PyQt5.QtWidgets import (QMainWindow, QApplication, QLabel, QPushButton, QStackedWidget, QWidget, QRadioButton,
                             QHBoxLayout,
                             QVBoxLayout, QSizePolicy, QSpacerItem, QLineEdit, QGridLayout)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from wrong_code import WrongCode
from opened_successfully import OpenSuccess


class EnterCode(QWidget):
    def __init__(self, queue, queue2):
        super().__init__()

        self.windowWidth = 1024
        self.windowHeight = 600
        #self.showFullScreen()
        self.queue = queue
        self.queue2 = queue2
        self.label = QLabel("ENTER THE UNLOCK CODE", self)
        self.line_edit = QLineEdit(self)

        self.wrong_code_widget = WrongCode(self.queue, self.queue2)
        self.locker_opened_widget = OpenSuccess(self.queue, self.queue2)

        # Creating all buttons
        self.button_1 = QPushButton("1")
        self.button_2 = QPushButton("2")
        self.button_3 = QPushButton("3")
        self.button_4 = QPushButton("4")
        self.button_5 = QPushButton("5")
        self.button_6 = QPushButton("6")
        self.button_7 = QPushButton("7")
        self.button_8 = QPushButton("8")
        self.button_9 = QPushButton("9")
        self.button_0 = QPushButton("0")
        self.button_hash = QPushButton("#")
        self.button_back = QPushButton("⌫")
        self.return_button = QPushButton("BACK")
        self.confirm_button = QPushButton("CONFIRM")

        # Initializing functions

        self.init_ui()
        self.connecting_return_button()
        self.styling_keyboard()
        self.connecting_keyboard()
        self.layout_managment()
        self.backend_communication()

    def init_ui(self):
        self.setStyleSheet("background-color: #2d2d2d;")
        self.setGeometry(0, 0, self.windowWidth, self.windowHeight)

        self.label.setFont(QFont("Helvetica", 30))
        self.label.setStyleSheet("color: white;"
                            "font-weight: bold;")
        self.label.setAlignment(Qt.AlignCenter | Qt.AlignHCenter)

        self.return_button.setStyleSheet("font-size: 25px;"
                                         "color: #f4f3f0;"
                                         "font-weight: bold;"
                                         "background-color: #162f42")


        self.line_edit.setMinimumHeight(50)
        self.line_edit.setStyleSheet("background-color: #162f42;"
                                     "font-size: 33px;"
                                     "font-weight: bold;"
                                     "color: #f4f3f0;")

    def connecting_return_button(self):
        self.return_button.clicked.connect(self.close)




    def styling_keyboard(self):
        buttons = [self.button_1, self.button_2, self.button_3, self.button_4, self.button_5, self.button_6,
                   self.button_7,
                   self.button_8, self.button_9, self.button_0, self.button_hash, self.button_back]

        for button in buttons:
            button.setStyleSheet("background-color: #6A1B1B;"
                                 "font-size: 22px;"
                                 "color: #f4f3f0;"
                                 "font-weight: bold;")
        self.confirm_button.setStyleSheet("background-color: darkgreen;"
                                 "font-size: 22px;"
                                 "color: #f4f3f0;"
                                 "font-weight: bold;")

    def connecting_keyboard(self):
        self.button_1.clicked.connect(lambda: self.add_tekst("1"))
        self.button_2.clicked.connect(lambda: self.add_tekst("2"))
        self.button_3.clicked.connect(lambda: self.add_tekst("3"))
        self.button_4.clicked.connect(lambda: self.add_tekst("4"))
        self.button_5.clicked.connect(lambda: self.add_tekst("5"))
        self.button_6.clicked.connect(lambda: self.add_tekst("6"))
        self.button_7.clicked.connect(lambda: self.add_tekst("7"))
        self.button_8.clicked.connect(lambda: self.add_tekst("8"))
        self.button_9.clicked.connect(lambda: self.add_tekst("9"))
        self.button_0.clicked.connect(lambda: self.add_tekst("0"))
        self.button_hash.clicked.connect(lambda: self.add_tekst("#"))
        self.button_back.clicked.connect(lambda: self.backspace())

    def add_tekst(self, tekst):
            self.line_edit.insert(tekst)

    def backspace(self):
            self.line_edit.backspace()


    def layout_managment(self):
        # Creating Grid Layout for buttons
        grid_layout = QGridLayout()

        grid_layout.addWidget(self.button_1, 0, 0)
        grid_layout.addWidget(self.button_2, 0, 1)
        grid_layout.addWidget(self.button_3, 0, 2)
        grid_layout.addWidget(self.button_4, 1, 0)
        grid_layout.addWidget(self.button_5, 1, 1)
        grid_layout.addWidget(self.button_6, 1, 2)
        grid_layout.addWidget(self.button_7, 2, 0)
        grid_layout.addWidget(self.button_8, 2, 1)
        grid_layout.addWidget(self.button_9, 2, 2)
        grid_layout.addWidget(self.button_back, 3, 0)
        grid_layout.addWidget(self.button_0, 3, 1)
        grid_layout.addWidget(self.button_hash, 3, 2)

        keyboard_layout = QHBoxLayout()
        keyboard_layout.addStretch(2)
        keyboard_layout.addLayout(grid_layout, 4)
        keyboard_layout.addStretch(2)

        # poziomy layout
        horizontal_layout = QHBoxLayout()
        horizontal_layout.addStretch(5)
        horizontal_layout.addWidget(self.line_edit, 2)
        horizontal_layout.addStretch(5)

        # pionowy layout
        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.label)
        vertical_layout.addStretch(3)
        vertical_layout.addLayout(horizontal_layout)
        vertical_layout.addStretch(3)
        vertical_layout.addLayout(keyboard_layout)

        # Przycisk powrot
        bottom_layout = QHBoxLayout()
        bottom_layout.addWidget(self.return_button)
        bottom_layout.addStretch(1)
        bottom_layout.addWidget(self.confirm_button)

        vertical_layout.addLayout(bottom_layout)

        self.setLayout(vertical_layout)


    def backend_communication(self):
        self.confirm_button.clicked.connect(self.check_code)

    def check_code(self):
        user_input = self.line_edit.text()
        #self.queue.put("code_verification")
        #self.queue.put("2" + user_input)
        with open(self.file_path, 'r') as locker_file:
            text = locker_file.read()
            locker_list = text.split("\n")
            for locker_info in locker_list:
                tab = locker_info.split(':')
                if int(tab[0]) == "2":
                    code = tab[1]
                    if user_input == code:
                        self.locker_opened_function()
                    else:
                        self.wrong_code_function()


    def wrong_code_function(self):
        self.line_edit.clear()
        self.wrong_code_widget.show()
        #self.wrong_code_widget.resize(1024, 600)

    def locker_opened_function(self):
        self.line_edit.clear()
        self.locker_opened_widget.show()
        #self.locker_opened_widget.resize(1024, 600)