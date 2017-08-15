"""The main window for the PyPlot GUI"""

import sys
import random

from PyQt5.QtWidgets import QApplication
from matplotlib.figure import Figure

from views.edit import PlotEdit
from views.plot import Plot

def create_a_sample_plot():
    figure = Figure(figsize=(5, 4), dpi=100)
    data = [random.random() for i in range(25)]
    subplot = figure.add_subplot(111)
    current_line, = subplot.plot(data, 'r-')
    title = "Unnamed Plot"
    subplot.set_title(title)
    return figure

if __name__ == '__main__':

    APP = QApplication(sys.argv)
    plot = create_a_sample_plot()
    plot_window = Plot(plot)
    edit_window = PlotEdit()
    plot_window.show()
    edit_window.show()
    sys.exit(APP.exec_())
