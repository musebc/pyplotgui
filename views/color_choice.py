"""
This is a Widget that will allow users to select a color for a variety of options.

Examples are line color, background, etc.
"""

from PyQt5.QtWidgets import QWidget


class ColorChoice(QWidget):
    """ColorChoice is built from the QWidget class and
    will build a popup window that will allow users to
    choose a color for their plot.
    """

    def __init__(self):
        super().__init__()
        self.left = 250
        self.top = 250
        self.width = 350
        self.height = 200
        self.init_ui()

    def init_ui(self):
        """This function creates the UI for choosing a color."""
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()
