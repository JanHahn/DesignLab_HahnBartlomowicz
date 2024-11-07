import sys
from PyQt5.QtWidgets import (QMainWindow, QApplication, QLabel, QPushButton, QStackedWidget, QWidget, QRadioButton,
                             QHBoxLayout,
                             QVBoxLayout, QSizePolicy, QSpacerItem, QLineEdit, QGridLayout)
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
        widget.setStyleSheet("background-color: #2d2d2d;")

        # Greeting label
        label = QLabel("DZIEŃ DOBRY!")
        label.setFont(QFont("Helvetica", 35))
        label.setStyleSheet("color: white; "
                            "font-weight: bold;")
        label.setAlignment(Qt.AlignCenter)

        #creating vertical layout
        vertical_layout = QVBoxLayout(widget)
        vertical_layout.addWidget(label, stretch=5)

        # Buttons
        self.button1 = QPushButton("CHCĘ SCHOWAĆ")
        self.button1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.button1.setMinimumHeight(40)
        self.button1.setStyleSheet("color: #f4f3f0;"
                                   "font-size: 33px;"
                                   "font-weight: bold;"
                                   "background-color: #007f5f;")

        self.button2 = QPushButton("CHCĘ ODEBRAĆ")
        self.button2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.button2.setMinimumHeight(40)
        self.button2.setStyleSheet("color: #f4f3f0;"
                                   "font-size: 33px;"
                                   "font-weight: bold;"
                                   "background-color: #8b0000;")

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
        widget.setStyleSheet("background-color: #2d2d2d;")

        # Która szafke wybierasz
        label = QLabel("WYBIERZ SKRYTKĘ", widget)
        label.setFont(QFont("Helvetica", 35))
        label.setGeometry(0, 0, 800, 80)
        label.setStyleSheet("color: white; font-weight: bold;")
        label.setAlignment(Qt.AlignCenter and Qt.AlignHCenter)

        self.button1 = QPushButton("SKRYTKA 1", widget)
        self.button2 = QPushButton("SKRYTKA 2", widget)

        # Customizing buttons
        self.button1.setGeometry(50, 100, 320, 220)
        self.button1.setStyleSheet("color: #f4f3f0;"
                                   "font-size: 35px;"
                                   "font-weight: bold;"
                                   "background-color: #8b0000;")

        self.button2.setGeometry(450, 100, 320, 220)
        self.button2.setStyleSheet("color: #f4f3f0;"
                                   "font-size: 35px;"
                                   "font-weight: bold;"
                                   "background-color: #8b0000;")

        self.return_button = QPushButton("POWRÓT", widget)
        self.return_button.setGeometry(650, 340, 140, 50)
        self.return_button.setStyleSheet("font-size: 25px;"
                                         "color: #f4f3f0;"
                                         "font-weight: bold;"
                                         "background-color: #007f5f;")

        self.return_button.clicked.connect(self.show_main_menu)

        self.button1.clicked.connect(self.show_odbierz_paczke)
        self.button2.clicked.connect(self.show_odbierz_paczke)

        return widget


    def create_chce_schowac(self):
        widget = QWidget(self)
        widget.setStyleSheet("background-color: #2d2d2d;")

        # Która szafke wybierasz
        label = QLabel("WYBIERZ SKRYTKĘ", widget)
        label.setFont(QFont("Helvetica", 35))
        label.setGeometry(0, 0, 800, 80)
        label.setStyleSheet("color: white; font-weight: bold;")
        label.setAlignment(Qt.AlignCenter and Qt.AlignHCenter)

        self.button1 = QPushButton("SKRYTKA 1", widget)
        self.button2 = QPushButton("SKRYTKA 2", widget)

        # Customizing buttons
        self.button1.setGeometry(50, 100, 320, 220)
        self.button1.setStyleSheet("color: #f4f3f0;"
                                   "font-size: 35px;"
                                   "font-weight: bold;"
                                   "background-color: #007f5f;")

        self.button2.setGeometry(450, 100, 320, 220)
        self.button2.setStyleSheet("color: #f4f3f0;"
                                   "font-size: 35px;"
                                   "font-weight: bold;"
                                   "background-color: #007f5f;")

        self.return_button = QPushButton("POWRÓT", widget)
        self.return_button.setGeometry(650, 340, 140, 50)
        self.return_button.setStyleSheet("font-size: 25px;"
                                         "color: #f4f3f0;"
                                         "font-weight: bold;"
                                         "background-color: #8b0000;")

        self.return_button.clicked.connect(self.show_main_menu)
        self.button1.clicked.connect(self.show_schowaj_paczke)
        self.button2.clicked.connect(self.show_schowaj_paczke)
        return widget




    def create_schowaj_paczke(self):
        widget = QWidget(self)
        widget.setStyleSheet("background-color: #2d2d2d;")
        label = QLabel("""<ol style="margin: 0; padding: 0; text-align: left;">
                <li>UMIEŚĆ PRZEDMIOT W SKRYTCE</li>
                <li>ZAMKNIJ SKRYTKĘ</li>
                <li>POCZEKAJ AŻ SKRYTKA WYKRYJE ZAWARTOŚĆ</li>
                <li>PODAJ EMAIL NA KTÓY OTRZYMASZ KOD OTWARCA</li>
            </ol>""", widget)
        label.setGeometry(0, 0, 800, 400)
        label.setFont(QFont("Helvetica", 20))
        label.setStyleSheet("color: white; font-weight: bold;")
        label.setAlignment(Qt.AlignLeft)
        label.setWordWrap(True)

        # Tworzymy pole tekstowe do wprowadzania kodu
        self.line_edit = QLineEdit(widget)
        self.line_edit.setMinimumHeight(50)
        self.line_edit.setStyleSheet("background-color: #8b0000;"
                                     "font-size: 25px;"
                                     "font-weight: bold;"
                                     "color: white;")
        #tymczasowo:
        self.line_edit.setGeometry(150, 150, 500, 30)

        #Przyciski klawiatury


        self.return_button = QPushButton("POWRÓT", widget)
        self.return_button.setGeometry(690, 365, 100, 30)
        self.return_button.setStyleSheet("font-size: 18px;"
                                         "color: #f4f3f0;"
                                         "font-weight: bold;"
                                         "background-color: #8b0000")

        self.return_button.clicked.connect(self.show_chce_schowac)

        return widget

    def create_odbierz_paczke(self):

        widget = QWidget(self)
        widget.setStyleSheet("background-color: #2d2d2d;")


        label = QLabel("WPISZ KOD ODBIORU DLA SKRYTKI", widget)

        label.setFont(QFont("Helvetica", 30))
        label.setStyleSheet("color: white;"
                            "font-weight: bold;")
        label.setAlignment(Qt.AlignCenter | Qt.AlignHCenter)

        # Tworzymy przycisk "POWRÓT"
        self.return_button = QPushButton("POWRÓT", widget)
        self.return_button.setStyleSheet("font-size: 25px;"
                                         "color: #f4f3f0;"
                                         "font-weight: bold;"
                                         "background-color: #007f5f")
        self.return_button.clicked.connect(self.show_chce_odebrac)

        # Tworzymy pole tekstowe do wprowadzania kodu
        self.line_edit = QLineEdit(widget)
        self.line_edit.setMinimumHeight(50)
        self.line_edit.setStyleSheet("background-color: #007f5f;"
                                     "font-size: 33px;"
                                     "font-weight: bold;"
                                     "color: #f4f3f0;")


        self.button_1 = QPushButton("1", widget)
        self.button_2 = QPushButton("2", widget)
        self.button_3 = QPushButton("3", widget)
        self.button_4 = QPushButton("4", widget)
        self.button_5 = QPushButton("5", widget)
        self.button_6 = QPushButton("6", widget)
        self.button_7 = QPushButton("7", widget)
        self.button_8 = QPushButton("8", widget)
        self.button_9 = QPushButton("9", widget)
        self.button_0 = QPushButton("0", widget)
        self.button_enter = QPushButton("OK", widget)
        self.button_back = QPushButton("⌫", widget)

        buttons = [self.button_1, self.button_2, self.button_3, self.button_4, self.button_5, self.button_6, self.button_7,
        self.button_8, self.button_9, self.button_0, self.button_enter, self.button_back]

        for button in buttons:
            button.setStyleSheet("background-color: #8b0000;"
                                 "font-size: 22px;"
                                 "color: #f4f3f0;"
                                 "font-weight: bold;")


        def add_tekst(tekst):
            self.line_edit.insert(tekst)
        def backspace():
            self.line_edit.backspace()

        self.button_1.clicked.connect(lambda: add_tekst("1"))
        self.button_2.clicked.connect(lambda: add_tekst("2"))
        self.button_3.clicked.connect(lambda: add_tekst("3"))
        self.button_4.clicked.connect(lambda: add_tekst("4"))
        self.button_5.clicked.connect(lambda: add_tekst("5"))
        self.button_6.clicked.connect(lambda: add_tekst("6"))
        self.button_7.clicked.connect(lambda: add_tekst("7"))
        self.button_8.clicked.connect(lambda: add_tekst("8"))
        self.button_9.clicked.connect(lambda: add_tekst("9"))
        self.button_0.clicked.connect(lambda: add_tekst("0"))
        self.button_back.clicked.connect(lambda: backspace())





        #Creating Grid Layout for buttons
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
        grid_layout.addWidget(self.button_back,3, 0)
        grid_layout.addWidget(self.button_0, 3, 1)
        grid_layout.addWidget(self.button_enter, 3, 2)



        klawaitura_layout = QHBoxLayout()

        klawaitura_layout.addStretch(2)
        klawaitura_layout.addLayout(grid_layout, 4)
        klawaitura_layout.addStretch(2)



        #poziomy layout
        horizontal_layout = QHBoxLayout()
        horizontal_layout.addStretch(5)
        horizontal_layout.addWidget(self.line_edit, 2)
        horizontal_layout.addStretch(5)


        #pionowy layout
        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(label)
        vertical_layout.addStretch(3)
        vertical_layout.addLayout(horizontal_layout)
        vertical_layout.addStretch(3)
        vertical_layout.addLayout(klawaitura_layout)

        #Przycisk powrot
        bottom_layout = QHBoxLayout()
        bottom_layout.addStretch(1)
        bottom_layout.addWidget(self.return_button)

        vertical_layout.addLayout(bottom_layout)

        widget.setLayout(vertical_layout)

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