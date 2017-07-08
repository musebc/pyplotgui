"""The main window for the PyPlot GUI"""

import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QComboBox, QVBoxLayout, QHBoxLayout, QWidget

from views.plot import Plot

class MainWindow(QWidget):
    """Builds the main window of the PyPlot GUI"""
    def __init__(self):
        super().__init__()
        self.left = 150
        self.top = 150
        self.width = 1080
        self.height = 720
        self.init_ui()
        self.title = "Unnamed Plot"

    def init_ui(self):
        """Initialize the UI screen."""

        line_box = QComboBox()
        data_plot = Plot(self, width=5, height=4)
        data_plot.plot(line_box)

        plot_vertical_box = QVBoxLayout()
        plot_vertical_box.addWidget(data_plot)

        plot_button = QPushButton('Plot Data', self)
        plot_button.clicked.connect(lambda: data_plot.plot(line_box))
        color_button = QPushButton('Change Color', self)
        color_button.clicked.connect(lambda: data_plot.color_change(line_box))
        style_button = QPushButton('Change Style', self)
        style_button.clicked.connect(lambda: data_plot.line_style_change(line_box))
        button_vertical_box = QVBoxLayout()
        button_vertical_box.addWidget(line_box)
        button_vertical_box.addStretch(1)
        button_vertical_box.addWidget(color_button)
        button_vertical_box.addWidget(style_button)
        button_vertical_box.addWidget(plot_button)

        main_horizontal_box = QHBoxLayout()
        main_horizontal_box.addLayout(plot_vertical_box)
        main_horizontal_box.addLayout(button_vertical_box)

        self.setLayout(main_horizontal_box)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()


if __name__ == '__main__':

    APP = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(APP.exec_())
