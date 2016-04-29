# Author: Chetan Patel
# 30/04/2016
# A simple planel to swap the slashes in text


from PySide.QtGui import *
from PySide.QtCore import *
import sys


class SwitcherPanel(QWidget):

    def __init__(self):
        super(SwitcherPanel, self).__init__()

        self.clipboard = QApplication.clipboard()

        self.line = QLineEdit()
        self.line.setPlaceholderText("Paste test here...")
        self.line.setText(self.clipboard.text())
        self.line.setMinimumWidth(300)

        self.push = QPushButton("Swap")
        self.push.setToolTip("Swap the slashes.")
        self.push.clicked.connect(self.swap)

        self.label = QLabel("Path: ")

        self.layout = QHBoxLayout()
        self.layout.addWidget(self.label)
        self.layout.addSpacing(25)
        self.layout.addWidget(self.line)
        self.layout.addSpacing(25)
        self.layout.addWidget(self.push)

        self.setLayout(self.layout)

    # method to swap the slash direction and copy the contents
    # to the clipboard

    def swap(self):

        text = self.line.text()
        changed = False
        if '/' in text:
            text = text.replace('/', '\\')
            changed = True
        elif '\\' in text:
            text = text.replace('\\', '/')
            changed = True
        if changed:
            self.line.setText(text)
            self.clipboard.setText(text)


# start the panel
def start():

    #app = QApplication(sys.argv)
    start.panel = SwitcherPanel()
    start.panel.show()
    #app.exec_()

#start()