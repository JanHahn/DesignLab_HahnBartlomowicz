import sys
from PyQt5.QtWidgets import (QMainWindow, QApplication, QLabel, QPushButton, QStackedWidget, QWidget, QRadioButton,
                             QHBoxLayout,
                             QVBoxLayout, QSizePolicy, QSpacerItem, QLineEdit, QGridLayout)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from pick_up import ChceOdebrac
from store import ChceSchowac


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.showFullScreen()
        self.windowWidth = 800
        self.windowHeight = 400
        self.greeting_label = QLabel("WELCOME TO THE LOCKER")
        self.pick_up_button = QPushButton("PICK UP")
        self.store_button = QPushButton("STORE")
        self.setWindowTitle("Main Menu")

        self.widget_window1 = ChceSchowac()
        self.widget_window2 = ChceOdebrac()


        self.initUI()
        self.layout_managment()
        self.scaling_buttons()
        self.connecting_buttons()

    def initUI(self):
        self.setStyleSheet("background-color: #2d2d2d;")
        self.setGeometry(0, 0, self.windowWidth, self.windowHeight)

        # Styling Label
        self.greeting_label.setFont(QFont("Helvetica", 35))
        self.greeting_label.setStyleSheet("color: white; "
                                          "font-weight: bold;")
        self.greeting_label.setAlignment(Qt.AlignCenter)

        # Styling buttons
        self.store_button.setStyleSheet("color: #f4f3f0;"
                                               "font-size: 33px;"
                                               "font-weight: bold;"
                                               "background-color: #162f42;")

        self.pick_up_button.setStyleSheet("color: #f4f3f0;"
                                               "font-size: 33px;"
                                               "font-weight: bold;"
                                               "background-color: #6A1B1B;")

    def scaling_buttons(self):
        self.pick_up_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.pick_up_button.setMinimumHeight(40)

        self.store_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.store_button.setMinimumHeight(40)

    def layout_managment(self):
        horizontal_layout = QHBoxLayout()
        horizontal_layout.addStretch(2)
        horizontal_layout.addWidget(self.store_button, 8)
        horizontal_layout.addStretch(2)
        horizontal_layout.addWidget(self.pick_up_button, 8)
        horizontal_layout.addStretch(2)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.greeting_label)
        main_layout.addStretch(1)
        main_layout.addLayout(horizontal_layout, stretch=6)
        main_layout.addStretch(1)

        self.setLayout(main_layout)

    def button_schowac_clicked(self):
        self.widget_window1.showFullScreen()
        self.widget_window1.resize(800, 400)

    def button_odebrac_clicked(self):
        self.widget_window2.showFullScreen()
        self.widget_window2.resize(800, 400)

    def connecting_buttons(self):
        self.pick_up_button.clicked.connect(self.button_odebrac_clicked)
        self.store_button.clicked.connect(self.button_schowac_clicked)




#
#
# def main():
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())
#
#
# if __name__ == "__main__":
#     main()
#
#
