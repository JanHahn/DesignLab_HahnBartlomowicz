import sys
from PyQt5.QtWidgets import (QMainWindow, QApplication, QLabel, QPushButton, QStackedWidget, QWidget, QRadioButton,
                             QHBoxLayout,
                             QVBoxLayout, QSizePolicy, QSpacerItem, QLineEdit, QGridLayout)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, QTimer
from pick_up import ChceOdebrac
from store import ChceSchowac
from locked_successfully import LockSuccess


class MainWindow(QWidget):
    def __init__(self, queue, queue2):
        super().__init__()

        self.queue = queue
        self.queue2 = queue2
        self.windowWidth = 1024
        self.windowHeight = 600
        self.greeting_label = QLabel("WELCOME TO THE LOCKER")
        self.pick_up_button = QPushButton("PICK UP")
        self.store_button = QPushButton("STORE")
        self.setWindowTitle("Main Menu")

        self.timer1 = QTimer()
        self.timer2 = QTimer()

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

    def button_store_clicked(self):
        self.queue.put("is_free")
        self.timer1.setInterval(100)
        self.timer1.timeout.connect(self.show_store)
        self.timer1.start(100)  # Sprawdzaj kolejkę co 100 ms

    def button_pickup_clicked(self):
        self.queue.put("is_free")
        self.timer2.setInterval(100)
        self.timer2.timeout.connect(self.show_pick_up)
        self.timer2.start(100)  # Sprawdzaj kolejkę co 100 ms


    def connecting_buttons(self):
        self.pick_up_button.clicked.connect(self.button_pickup_clicked)
        self.store_button.clicked.connect(self.button_store_clicked)


    def show_store(self):
        print("frontend sprawdza kolejke")
        if not self.queue2.empty():
            self.timer1.stop()
            print("frontend otrzymal informacje")
            info = self.queue2.get()

            print(f"{info}")
            self.widget_store = ChceSchowac(self.queue, self.queue2, info)
            self.widget_store.showFullScreen()


    def show_pick_up(self):
        print("frontend sprawdza kolejke")
        if not self.queue2.empty():
            self.timer2.stop()
            print("frontend otrzymal informacje")
            info = self.queue2.get()

            print(f"{info}")
            self.widget_pickup = ChceOdebrac(self.queue, self.queue2, info)
            self.widget_pickup.showFullScreen()
        else:
            print("Kolejka jest pusta ")






