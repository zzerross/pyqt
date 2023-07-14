import sys

from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):
    signal = pyqtSignal(int, str)

    def __init__(self):
        super().__init__()
        self.signal.connect(self.on_signal)
        self.signal.emit(1234, 'hello')

    @staticmethod
    def on_signal(number, message):
        print(number, message)


if __name__ == '__main__':
    application = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    application.exec()
