# Author: Chetan Patel
# 30/04/2016
# A simple planel to swap the slashes in text

try:
    from PySide import QtGui, QtCore
    from PySide.QtGui import *
    from PySide.QtCore import *
except ImportError:
    from PySide2 import QtGui, QtCore, QtWidgets
    from PySide2.QtGui import *
    from PySide2.QtCore import *
    from PySide2.QtWidgets import *

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

        self.render_setting_layout = QHBoxLayout()

        self.render_start_frame_label = QLabel("Start Frame: ")
        self.render_end_frame_label = QLabel("End Frame: ")
        self.render_start_frame_textedit = QLineEdit(str(int(nuke.root()["first_frame"].value())))
        self.render_end_frame_textedit = QLineEdit(str(int(nuke.root()["last_frame"].value())))

        self.render_setting_layout.addWidget(self.render_start_frame_label)
        self.render_setting_layout.addWidget(self.render_start_frame_textedit)
        self.render_setting_layout.addWidget(self.render_end_frame_label)
        self.render_setting_layout.addWidget(self.render_end_frame_textedit)

        self.copy_clipboard_button = QPushButton("Copy Cmd To Clipboard")
        self.copy_clipboard_button.setToolTip("Copies the command to the clipboard.")
        self.exe_clipboard_button = QPushButton("Copy Cmd To Clipboard")
        self.exe_clipboard_button.setToolTip("Copies the command to the clipboard.")

        self.copy_clipboard_button.clicked.connect(self.copy_clipboard)
        self.exe_clipboard_button.clicked.connect(self.exe_cmd)

        self.label = QLabel("Path: ")

        self.layout = QVBoxLayout()
        self.layout.addLayout(self.render_setting_layout)

        tableWidget = QTableWidget()
        tableWidget.setRowCount(len(self.writes))
        tableWidget.setColumnCount(5)

        count = 0;
        for w in self.write_group:
            tableWidget.setItem(count, 0, QTableWidgetItem(self.writes[count]["name"].value()))

            chkBoxItem = QTableWidgetItem()
            chkBoxItem.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
            chkBoxItem.setCheckState(Qt.Checked)
            tableWidget.setItem(count, 1, chkBoxItem)


            count += 1




        # for w in self.write_group:
        #     l = QHBoxLayout()
        #     l.addSpacing(25)
        #     for c in w:
        #         l.addWidget(c)
        #     self.layout.addLayout(l)
        self.layout.addWidget(tableWidget)
        self.layout.addWidget(self.label)

        self.layout.addSpacing(25)
        self.layout.addWidget(self.copy_clipboard_button)
        self.layout.addWidget(self.exe_clipboard_button)

        self.setLayout(self.layout)

    # method to swap the slash direction and copy the contents
    # to the clipboard

    def __generate_write_groups(self):

        nodes = nuke.allNodes("Write")
        nodes += nuke.allNodes("WriteGeo")
        return nodes


    def generate_cmd(self):
        cmd_args = ""

    def copy_clipboard(self):
        print "hello"

    def exe_cmd(self):
        print "hello"

# start the panel
def start():

    #app = QApplication(sys.argv)
    start.panel = CmdRender()
    start.panel.show()
    #app.exec_()

#start()
