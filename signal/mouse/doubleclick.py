import sys

from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget


class Widget(QWidget):
    signal = pyqtSignal(object)

    def __init__(self):
        super().__init__()
        self.mouseDoubleClickEvent = lambda event: self.signal.emit(event)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        widget = Widget()
        widget.signal.connect(self.on_signal)
        self.setCentralWidget(widget)

    @staticmethod
    def on_signal(event):
        print(event)


if __name__ == '__main__':
    application = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    application.exec()
