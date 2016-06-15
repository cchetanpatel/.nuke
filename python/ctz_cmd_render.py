# Author: Chetan Patel
# 30/04/2016
# A simple planel to swap the slashes in text


from PySide.QtGui import *
from PySide.QtCore import *
import sys
import nuke


class CmdRender(QWidget):

    def __init__(self):
        super(CmdRender, self).__init__()

        self.writes = self.__generate_write_groups()

        self.write_group = []

        for write_node in self.writes:
            ctrl = []
            ctrl.append(QCheckBox(write_node["name"].value()))
            ctrl[0].setChecked(True)
            self.write_group.append(ctrl)


        self.push = QPushButton("Genereate command")
        self.push.setToolTip("Generates the command.")
        self.push.clicked.connect(self.generate_cmd)

        self.label = QLabel("Path: ")

        self.layout = QVBoxLayout()
        for w in self.write_group:
            l = QHBoxLayout()
            l.addSpacing(25)
            for c in w:
                l.addWidget(c)
            self.layout.addLayout(l)

        self.layout.addWidget(self.label)

        self.layout.addSpacing(25)
        self.layout.addWidget(self.push)

        self.setLayout(self.layout)

    # method to swap the slash direction and copy the contents
    # to the clipboard

    def __generate_write_groups(self):

        nodes = nuke.allNodes("Write")
        nodes += nuke.allNodes("WriteGeo")
        return nodes


    def generate_cmd(self):
        print "hello"



# start the panel
def start():

    #app = QApplication(sys.argv)
    start.panel = CmdRender()
    start.panel.show()
    #app.exec_()

#start()