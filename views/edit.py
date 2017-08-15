"""The module that contains the plot edit partent widget."""

import logging
import threading

from matplotlib import pyplot as plt
from PyQt5.QtWidgets import (QComboBox, QHBoxLayout, QPushButton, QVBoxLayout,
                             QWidget)

from views.plot import Plot

log = logging.getLogger(__name__)

class PlotEdit(QWidget):
    """
    Class that builds the parent plot editing widget.
    """

    def __init__(self, plot_window=None):
        super().__init__()
        self.left = 150
        self.top = 150
        self.width = 1080
        self.height = 720
        self.line_box = QComboBox()
        self.select_plot()
        self.init_ui()
        self.check_for_plots_thread = threading.Thread(target=self.check_for_plots())
        self.check_for_plots_thread.daemon = True
        self.check_for_plots_thread.start()

    def init_ui(self):
        """Initialize the Edit Widget"""
        plot_window_button = QPushButton('Select Plot Window', self)
        plot_window_button.clicked.connect(self.select_plot)
        plot_button = QPushButton('Plot Data', self)
        plot_button.clicked.connect(self.plot)
        color_button = QPushButton('Change Color', self)
        color_button.clicked.connect(lambda: self.plot_window.color_change(self.line_box))
        style_button = QPushButton('Change Style', self)
        style_button.clicked.connect(lambda: self.plot_window.line_style_change(self.line_box))
        remove_button = QPushButton('Remove Plot', self)
        remove_button.clicked.connect(lambda: self.plot_window.remove_plot(self.line_box))
        button_vertical_box = QVBoxLayout()
        button_vertical_box.addWidget(self.line_box)
        button_vertical_box.addStretch(1)
        button_vertical_box.addWidget(plot_window_button)
        button_vertical_box.addWidget(color_button)
        button_vertical_box.addWidget(style_button)
        button_vertical_box.addWidget(plot_button)
        button_vertical_box.addWidget(remove_button)

        main_horizontal_box = QHBoxLayout()
        main_horizontal_box.addLayout(button_vertical_box)
        self.setLayout(main_horizontal_box)
        self.setGeometry(self.left, self.top, self.width, self.height)

    def check_for_plots(self):
        open_plots = Plot.get_plot_instances()
        for plot in open_plots:
        

    def get_line_box(self):
        """Returns the combo box for referencing the currently selected line."""
        return self.line_box

    def select_plot(self):
        """Function to select the plot to modify."""
        open_plots = Plot.get_plot_instances()
        log.warning("select_plot called.")
        if not open_plots:
            #No Open Plots: Create a new one
            pass
        elif len(open_plots) == 1:
            #Only one plot open, pick that one
            self.plot_window = open_plots[0]
        else:
            #Multiple plots open, hadle that case.
            pass

    def plot(self):
        """Wrapper around the plot function in the Plot class."""

        self.plot_window.plot(self.get_line_box())
        self.plot_window.show()
