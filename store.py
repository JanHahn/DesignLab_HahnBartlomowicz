import sys
from PyQt5.QtWidgets import (QMainWindow, QApplication, QLabel, QPushButton, QStackedWidget, QWidget, QRadioButton,
                             QHBoxLayout,
                             QVBoxLayout, QSizePolicy, QSpacerItem, QLineEdit, QGridLayout)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from enter_email import EnterEmail

class ChceSchowac(QWidget):
    def __init__(self, queue):
        super().__init__()

        self.queue = queue
        self.windowWidth = 1024
        self.windowHeight = 600
        self.label = QLabel("CHOOSE THE LOCKER")
        self.locker1_button = QPushButton("LOCKER 1")
        self.locker2_button = QPushButton("LOCKER 2")
        self.back_button = QPushButton("BACK")
        self.flag = 0

        self.widget1 = EnterEmail(self.queue)
        self.widget2 = EnterEmail(self.queue)

        self.initUI()
        self.layout_managment()
        self.scaling_buttons()
        self.return_button()
        self.connecting_buttons()


    def initUI(self):
        self.setStyleSheet("background-color: #2d2d2d;")
        self.setGeometry(0, 0, self.windowWidth, self.windowHeight)

        # Styling Label
        self.label.setFont(QFont("Helvetica", 35))
        self.label.setStyleSheet("color: white; "
                                          "font-weight: bold;")
        self.label.setAlignment(Qt.AlignCenter)

        # Styling buttons
        self.locker1_button.setStyleSheet("color: #f4f3f0;"
                                               "font-size: 33px;"
                                               "font-weight: bold;"
                                               "background-color: #6A1B1B;")

        self.locker2_button.setStyleSheet("color: #f4f3f0;"
                                               "font-size: 33px;"
                                               "font-weight: bold;"
                                               "background-color: #6A1B1B;")

        self.back_button.setGeometry(650, 340, 140, 50)
        self.back_button.setStyleSheet("font-size: 25px;"
                                         "color: #f4f3f0;"
                                         "font-weight: bold;"
                                         "background-color: #162f42;")

    def scaling_buttons(self):
        self.locker2_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.locker2_button.setMinimumHeight(40)

        self.locker1_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.locker1_button.setMinimumHeight(40)

    def layout_managment(self):
        horizontal_layout = QHBoxLayout()
        horizontal_layout.addStretch(2)
        horizontal_layout.addWidget(self.locker1_button, 8)
        horizontal_layout.addStretch(2)
        horizontal_layout.addWidget(self.locker2_button, 8)
        horizontal_layout.addStretch(2)

        bottom_layout = QHBoxLayout()
        bottom_layout.addWidget(self.back_button)
        bottom_layout.addStretch(1)


        main_layout = QVBoxLayout()
        main_layout.addWidget(self.label)
        main_layout.addStretch(1)
        main_layout.addLayout(horizontal_layout, stretch=6)
        main_layout.addStretch(1)
        main_layout.addLayout(bottom_layout)

        self.setLayout(main_layout)


    def return_button(self):
        self.back_button.clicked.connect(self.close)

    def locker1_clicked(self):
        self.flag = 1
        self.widget1.showFullScreen()
        self.widget1.resize(1024, 600)

    def locker2_clicked(self):
        self.flag = 2
        self.widget2.showFullScreen()
        self.widget2.resize(1024, 600)


    def connecting_buttons(self):
        self.locker1_button.clicked.connect(self.locker1_clicked)
        self.locker2_button.clicked.connect(self.locker2_clicked)



    #TODO
    def disabling_buttons(self):
        #jesli ktoras ze skrytek jest zamknieta wyłączyc przycisk
        pass

# def main():
#     app = QApplication(sys.argv)
#     window = ChceSchowac()
#     window.show()
#     sys.exit(app.exec_())
#
#
# if __name__ == "__main__":
#     main()
