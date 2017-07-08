"""Plot helper class that builds the subplots."""

from PyQt5.QtWidgets import QSizePolicy

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

import random

class Plot(FigureCanvas):
 
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
 
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
 
        FigureCanvas.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.line_list = []
        self.plot_index = 0
        self.plots = {}
 
 
    def plot(self, line_box, title="Unnamed Plot"):
        data = [random.random() for i in range(25)]
        ax = self.figure.add_subplot(111)
        current_plot, = ax.plot(data, 'r-')
        self.line_list.append(current_plot)
        title = "Unnamed Plot"
        ax.set_title(title)
        line_box.addItem(title)
        self.plots[title] = self.plot_index
        self.plot_index += 1
        self.draw()


    def color_change(self, line_box):
        index = line_box.currentIndex()
        line = self.line_list[index]
        line.set_color('b')
        self.draw()

    def line_style_change(self, line_box):
        index = line_box.currentIndex()
        line = self.line_list[index]
        line.set_linestyle('--')
        self.draw()