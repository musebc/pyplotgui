"""The main window for the PyPlot GUI"""

import sys
from PyQt5.QtWidgets import QAction, QApplication, QMainWindow, QWidget
from PyQt5.QtGui import QIcon


class MainWindow(QMainWindow):
    """Builds the main window of the PyPlot GUI"""
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        """Initialize the UI screen."""
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('views/smalllogo.png'))
        self.statusBar().showMessage('Ready')

        self.showMaximized()


if __name__ == '__main__':

    APP = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(APP.exec_())
