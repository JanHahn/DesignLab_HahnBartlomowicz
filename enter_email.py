import sys
from PyQt5.QtWidgets import (QMainWindow, QApplication, QLabel, QPushButton, QStackedWidget, QWidget, QRadioButton,
                             QHBoxLayout,
                             QVBoxLayout, QSizePolicy, QSpacerItem, QLineEdit, QGridLayout)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

from email_confirmation import EmailConfirmation

class EnterEmail(QWidget):
    def __init__(self, queue, locker_id, queue2):
        super().__init__()

        self.locker_id = locker_id
        self.queue = queue
        self.queue2 = queue2
        self.window_width = 1024
        self.window_height = 600
        # Creating label, line edit and buttons needed
        self.label = QLabel()
        self.line_edit = QLineEdit(self)
        self.backspace_button = QPushButton("⌫")
        self.return_button = QPushButton("BACK")
        self.confirm_button = QPushButton("CONFIRM")

        self.keyboard_rows = {
            "numeric": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"],  # 10
            "first_row": ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p"],  # 10
            "second_row": ["a", "s", "d", "f", "g", "h", "j", "k", "l"],  # 9
            "third_row": ["z", "x", "c", "v", "b", "n", "m", "@", "."]  # 9
        }

        self.buttons = {
            "numeric": [],
            "first_row": [],
            "second_row": [],
            "third_row": []
        }

        self.layouts = {
            "numeric": QHBoxLayout(),
            "first_row": QHBoxLayout(),
            "second_row": QHBoxLayout(),
            "third_row": QHBoxLayout()
        }

        self.init_ui()
        self.layout_managment()
        self.connecting_return_button()
        self.creating_keyboard()
        self.connecting_return_button()
        self.connect_confirm_button()



    def init_ui(self):
        self.setStyleSheet("background-color: #2d2d2d;")
        self.setGeometry(0, 0, self.window_width, self.window_height)


        # Styling label
        self.label.setText("""<ol style="margin: 0; padding: 0; text-align: left;">
                       <li>PLACE THE ITEM IN THE LOCKER</li>
                       <li>CLOSE THE</li>
                       <li>PROVIDE THE EMAIL ADDRESS WHERE YOU WILL RECIVE</li>
                        THE UNLOCK CODE</li>
                   </ol>""")

        self.label.setFont(QFont("Helvetica", 18))
        self.label.setStyleSheet("color: white; font-weight: bold;")
        self.label.setAlignment(Qt.AlignLeft)
        self.label.setWordWrap(True)

        # Tworzenie pole tekstowe do wprowadzania kodu

        self.line_edit.setMinimumHeight(50)
        self.line_edit.setStyleSheet("background-color: #6A1B1B;"
                                "font-size: 25px;"
                                "font-weight: bold;"
                                "color: white;")

        # Erase button
        self.backspace_button.setStyleSheet("font-size: 25px;"
                                       "color: #f4f3f0;"
                                       "font-weight: bold;"
                                       "background-color: #162f42")

        self.return_button.setStyleSheet("font-size: 18px;"
                                         "color: #f4f3f0;"
                                         "font-weight: bold;"
                                         "background-color: #6A1B1B")

        self.confirm_button.setStyleSheet("font-size: 18px;"
                                         "color: #f4f3f0;"
                                         "font-weight: bold;"
                                         "background-color: darkgreen;")



    def formating_keyboard(self):
        layouts = {
            "numeric": QHBoxLayout(),
            "first_row": QHBoxLayout(),
            "second_row": QHBoxLayout(),
            "third_row": QHBoxLayout()
        }

        for layout in layouts.values():
            layout.addStretch(2)



    def creating_keyboard(self):
        for layout in self.layouts.values():
            layout.addStretch(2)

        for row_name, keys in self.keyboard_rows.items():
            for key in keys:
                button = QPushButton(key)
                button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                button.setMinimumHeight(50)
                button.setMinimumWidth(90)
                self.buttons[row_name].append(button)
                self.layouts[row_name].addWidget(button)
                button.setStyleSheet("background-color: #162f42;"
                                     "font-size: 22px;"
                                     "color: #f4f3f0;"
                                     "font-weight: bold;")
                button.clicked.connect(lambda checked, tekst=key: self.add_tekst(tekst))

        self.backspace_button.clicked.connect(lambda: self.backspace())

        # Dodawanie odstepow na koncu layoutow klawiatury
        for layout in self.layouts.values():
            layout.addStretch(2)

        # Przycisk return

    def connecting_return_button(self):
        self.return_button.clicked.connect(self.close)

    def add_tekst(self, tekst):
        self.line_edit.insert(tekst)

    def backspace(self):
        self.line_edit.backspace()




    def layout_managment(self):
        # Layout instrukcji
        instrukcja_layout = QHBoxLayout()
        instrukcja_layout.addWidget(self.label)

        # Layout do pola do pisania
        line_edit_layout = QHBoxLayout()
        line_edit_layout.addStretch(3)
        line_edit_layout.addWidget(self.line_edit, 10)
        line_edit_layout.addStretch(1)
        line_edit_layout.addWidget(self.backspace_button)
        line_edit_layout.addStretch(1)

        # Przycisk powrot
        bottom_layout = QHBoxLayout()
        bottom_layout.addWidget(self.return_button)
        bottom_layout.addStretch(1)
        bottom_layout.addWidget(self.confirm_button)

        # Głowny pionowy Layout
        vertical_layout = QVBoxLayout()
        vertical_layout.addLayout(instrukcja_layout)
        vertical_layout.addStretch(1)
        vertical_layout.addLayout(line_edit_layout)
        vertical_layout.addStretch(1)
        vertical_layout.addLayout(self.layouts["numeric"])
        vertical_layout.addLayout(self.layouts["first_row"])
        vertical_layout.addLayout(self.layouts["second_row"])
        vertical_layout.addLayout(self.layouts["third_row"])
        vertical_layout.addLayout(bottom_layout)

        self.setLayout(vertical_layout)

    def confirm_button_clicked(self):
        users_input = self.line_edit.text()

        if len(users_input) == 0:
            users_email = "No email provided"
        else:
            users_email = users_input
            backend_info = self.locker_id + users_email

        self.widget = EmailConfirmation(users_email, self.queue, backend_info, self.queue2)
        self.widget.show()
        #self.widget.resize(1024, 600)
        self.line_edit.clear()

    def connect_confirm_button(self):
        self.confirm_button.clicked.connect(self.confirm_button_clicked)



