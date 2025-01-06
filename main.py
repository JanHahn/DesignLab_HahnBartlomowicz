import sys
from PyQt5.QtWidgets import QApplication
from main_window import MainWindow

def main():
    while True:
        app = QApplication(sys.argv)

        # Tworzymy i pokazujemy główne menu
        main_menu = MainWindow()
        main_menu.show()

        sys.exit(app.exec_())




if __name__ == "__main__":
    main()
