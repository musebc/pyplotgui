"""The main window for the PyPlot GUI"""

import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout
from PyQt5.QtGui import QIcon

from views.plot import Plot
from matplotlib import pyplot as plt
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

class MainWindow(QMainWindow):
    """Builds the main window of the PyPlot GUI"""
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        """Initialize the UI screen."""

        m = Plot(self, width=5, height=4)
        m.move(0,0)
 
        button = QPushButton('Plot Data', self)
        button.setToolTip('Creates a new plot of data.')
        button.clicked.connect(m.plot)
        button.move(500,0)
        button.resize(140,100)
        self.showMaximized()


if __name__ == '__main__':

    APP = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(APP.exec_())
