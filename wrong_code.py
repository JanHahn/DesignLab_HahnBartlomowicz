import sys
from PyQt5.QtWidgets import (QMainWindow, QApplication, QLabel, QPushButton, QStackedWidget, QWidget, QRadioButton,
                             QHBoxLayout,
                             QVBoxLayout, QSizePolicy, QSpacerItem, QLineEdit, QGridLayout)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, QTimer
import time



class WrongCode(QWidget):
    def __init__(self, queue):
        super().__init__()
        self.windowWidth = 1024
        self.windowHeight = 600

        self.QTimer = QTimer()
        self.label = QLabel("Wrong unlock code!")
        self.try_again_button = QPushButton("Try again")
        self.init_ui()
        self.layout_management()
        self.buttons_size_policy()
        self.connecting_finished_button()


    def init_ui(self):
        self.setStyleSheet("background-color: #2d2d2d;")
        self.setGeometry(0, 0, self.windowWidth, self.windowHeight)

        self.label.setFont(QFont("Helvetica", 40))
        self.label.setStyleSheet("color: red; font-weight: bold;")
        self.label.setAlignment(Qt.AlignCenter | Qt.AlignHCenter)
        self.try_again_button.setStyleSheet("font-size: 35px;"
                                         "color: white;"
                                         "font-weight: bold;"
                                         "background-color: #162f42;")

    def buttons_size_policy(self):
        self.try_again_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.try_again_button.setMinimumHeight(20)


    def layout_management(self):

        button_layout = QHBoxLayout()
        button_layout.addStretch(1)
        button_layout.addWidget(self.try_again_button, stretch=3)
        button_layout.addStretch(1)

        main_layout = QVBoxLayout()
        main_layout.addStretch(1)
        main_layout.addWidget(self.label)
        main_layout.addStretch(2)
        main_layout.addLayout(button_layout, stretch=4)
        main_layout.addStretch(2)
        self.setLayout(main_layout)


    def connecting_finished_button(self):
        self.try_again_button.clicked.connect(self.finished_button_clicked)

    def finished_button_clicked(self):
        self.close()


def main():
     app = QApplication(sys.argv)
     window = WrongCode()
     window.show()
     sys.exit(app.exec_())


if __name__ == "__main__":
    main()

