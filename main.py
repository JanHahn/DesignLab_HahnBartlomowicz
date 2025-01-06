import sys
from PyQt5.QtWidgets import QApplication
from main_window import MainWindow
from multiprocessing import Process, Queue
from backend import application

def main():

    app = QApplication(sys.argv)
    q = Queue()
    backend = Process(target=application, args=(q,))
    backend.start()
    # Tworzymy i pokazujemy główne menu
    main_menu = MainWindow(q)
    main_menu.show()

    sys.exit(app.exec_())




if __name__ == "__main__":
    main()
