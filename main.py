import sys
from PyQt5.QtWidgets import (QMainWindow, QApplication, QLabel, QPushButton, QStackedWidget, QWidget, QRadioButton, QHBoxLayout,
                             QVBoxLayout, QSizePolicy, QSpacerItem)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

#hello
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Parameters for the window
        self.windowWidth = 800
        self.windowHeight = 400
        self.setWindowTitle("The Skrytka ")
        self.setGeometry(0, 0, self.windowWidth, self.windowHeight)

        # Creating stacked widget
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        # Creating 3 views
        self.main_menu = self.create_main_menu()
        self.schowaj_paczke = self.create_schowaj_paczke()
        self.odbierz_paczke = self.create_odbierz_paczke()
        self.chce_odebrac = self.create_chce_odebrac()
        self.chce_schowac = self.create_chce_schowac()

        # Adding different views to stacked widget
        self.stacked_widget.addWidget(self.main_menu)
        self.stacked_widget.addWidget(self.schowaj_paczke)
        self.stacked_widget.addWidget(self.odbierz_paczke)
        self.stacked_widget.addWidget(self.chce_odebrac)
        self.stacked_widget.addWidget(self.chce_schowac)


    def create_main_menu(self):
        widget = QWidget(self)
        widget.setStyleSheet("background-color: #d1e8d1;")

        # Greeting label
        label = QLabel("DZIEŃ DOBRY!")
        label.setFont(QFont("Helvetica", 30))
        label.setStyleSheet("color: #0a093b; font-weight: bold;")
        label.setAlignment(Qt.AlignCenter)

        #creating vertical layout
        vertical_layout = QVBoxLayout(widget)
        vertical_layout.addWidget(label, stretch=5)

        # Buttons
        self.button1 = QPushButton("CHCĘ SCHOWAĆ")
        self.button1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.button1.setMinimumHeight(40)
        self.button1.setStyleSheet("color: #0f571e;"
                                   "font-size: 30px;"
                                   "font-weight: bold;"
                                   "background-color: white;")

        self.button2 = QPushButton("CHCĘ ODEBRAĆ")
        self.button2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.button2.setMinimumHeight(40)
        self.button2.setStyleSheet("color: #870925;"
                                   "font-size: 30px;"
                                   "font-weight: bold;"
                                   "background-color: white;")

        #creating horizontal layout (nested layout for button)
        horizontal_layout = QHBoxLayout()
        horizontal_layout.addStretch(2)
        horizontal_layout.addWidget(self.button1, 8)
        horizontal_layout.addStretch(2)
        horizontal_layout.addWidget(self.button2, 8)
        horizontal_layout.addStretch(2)

        #adding horizontal layout with buttons to main vertical layout
        vertical_layout.addLayout(horizontal_layout, stretch=8)
        vertical_layout.addStretch(1)

        widget.setLayout(vertical_layout)

        self.button1.clicked.connect(self.show_chce_schowac)
        self.button2.clicked.connect(self.show_chce_odebrac)

        return widget


    def create_chce_odebrac(self):
        widget = QWidget(self)
        widget.setStyleSheet("background-color: #d1e8d1;")

        # Która szafke wybierasz
        label = QLabel("WYBIERZ SKRYTKĘ", widget)
        label.setFont(QFont("Helvetica", 30))
        label.setGeometry(0, 0, 800, 80)
        label.setStyleSheet("color: #0a093b; font-weight: bold;")
        label.setAlignment(Qt.AlignCenter and Qt.AlignHCenter)

        self.button1 = QPushButton("SKRYTKA 1", widget)
        self.button2 = QPushButton("SKRYTKA 2", widget)

        # Customizing buttons
        self.button1.setGeometry(50, 100, 320, 220)
        self.button1.setStyleSheet("color: black;"
                                   "font-size: 30px;"
                                   "font-weight: bold;"
                                   "background-color: white;")

        self.button2.setGeometry(450, 100, 320, 220)
        self.button2.setStyleSheet("color: black;"
                                   "font-size: 30px;"
                                   "font-weight: bold;"
                                   "background-color: white;")

        self.return_button = QPushButton("POWRÓT", widget)
        self.return_button.setGeometry(650, 340, 140, 50)
        self.return_button.setStyleSheet("font-size: 25px;"
                                         "color: #870925;"
                                         "font-weight: bold;"
                                         "background-color: white;")

        self.return_button.clicked.connect(self.show_main_menu)

        self.button1.clicked.connect(self.show_odbierz_paczke)
        self.button2.clicked.connect(self.show_odbierz_paczke)

        return widget


    def create_chce_schowac(self):
        widget = QWidget(self)
        widget.setStyleSheet("background-color: #d1e8d1;")

        # Która szafke wybierasz
        label = QLabel("WYBIERZ SKRYTKĘ", widget)
        label.setFont(QFont("Helvetica", 30))
        label.setGeometry(0, 0, 800, 80)
        label.setStyleSheet("color: #0a093b; font-weight: bold;")
        label.setAlignment(Qt.AlignCenter and Qt.AlignHCenter)

        self.button1 = QPushButton("SKRYTKA 1", widget)
        self.button2 = QPushButton("SKRYTKA 2", widget)

        # Customizing buttons
        self.button1.setGeometry(50, 100, 320, 220)
        self.button1.setStyleSheet("color: black;"
                                   "font-size: 30px;"
                                   "font-weight: bold;"
                                   "background-color: white;")

        self.button2.setGeometry(450, 100, 320, 220)
        self.button2.setStyleSheet("color: black;"
                                   "font-size: 30px;"
                                   "font-weight: bold;"
                                   "background-color: white;")

        self.return_button = QPushButton("POWRÓT", widget)
        self.return_button.setGeometry(650, 340, 140, 50)
        self.return_button.setStyleSheet("font-size: 25px;"
                                         "color: #870925;"
                                         "font-weight: bold;"
                                         "background-color: white;")

        self.return_button.clicked.connect(self.show_main_menu)
        self.button1.clicked.connect(self.show_schowaj_paczke)
        self.button2.clicked.connect(self.show_schowaj_paczke)
        return widget


    def create_schowaj_paczke(self):
        widget = QWidget(self)
        widget.setStyleSheet("background-color: #d1e8d1;")
        label = QLabel("""<ol style="margin: 0; padding: 0; text-align: left;">
                <li>UMIEŚĆ PRZEDMIOT W SKRYTCE</li>
                <li>ZAMKNIJ SKRYTKĘ</li>
                <li>POCZEKAJ AŻ SKRYTKA WYKRYJE ZAWARTOŚĆ</li>
                <li>PODAJ EMAIL NA KTÓY OTRZYMASZ KOD OTWARCA</li>
            </ol>""", widget)
        label.setGeometry(0, 0, 800, 400)
        label.setFont(QFont("Helvetica", 17))
        label.setStyleSheet("color: #0a093b; font-weight: bold;")
        label.setAlignment(Qt.AlignLeft)
        label.setWordWrap(True)

        self.return_button = QPushButton("POWRÓT", widget)
        self.return_button.setGeometry(690, 365, 100, 30)
        self.return_button.setStyleSheet("font-size: 18px;"
                                         "color: #870925;"
                                         "font-weight: bold;"
                                         "background-color: white;")

        self.return_button.clicked.connect(self.show_chce_schowac)

        return widget


    def create_odbierz_paczke(self):
        widget = QWidget(self)
        widget.setStyleSheet("background-color: #d1e8d1;")
        label = QLabel(f"WPISZ KOD ODBIORU DLA SKRYTKI", widget)
        label.setGeometry(0, 0, 800, 70)
        label.setFont(QFont("Helvetica", 22))
        label.setStyleSheet("color: #0a093b; font-weight: bold;")
        label.setAlignment(Qt.AlignCenter | Qt.AlignHCenter)

        self.return_button = QPushButton("POWRÓT", widget)
        self.return_button.setGeometry(650, 340, 140, 50)
        self.return_button.setStyleSheet("font-size: 25px;"
                                          "color: #870925;"
                                          "font-weight: bold;"
                                          "background-color: white;")

        self.return_button.clicked.connect(self.show_chce_odebrac)

        return widget

    def show_main_menu(self):
        self.stacked_widget.setCurrentWidget(self.main_menu)

    def show_schowaj_paczke(self):
        self.stacked_widget.setCurrentWidget(self.schowaj_paczke)

    def show_odbierz_paczke(self):
        self.stacked_widget.setCurrentWidget(self.odbierz_paczke)
    def show_chce_odebrac(self):
        self.stacked_widget.setCurrentWidget(self.chce_odebrac)

    def show_chce_schowac(self):
        self.stacked_widget.setCurrentWidget(self.chce_schowac)

    def resizeEvent(self, event):
        super().resizeEvent(event)

        # Optional: Customize the button size based on the window size
        button_size = self.width() // 3  # Button size based on one-third of window width
        button_size = self.width()

        # for button in self.buttons:
        #     button.setFixedSize(button_size, button_size)  # Set buttons to be squares

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()