# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_main_window(object):
    def setupUi(self, main_window):
        main_window.setObjectName("main_window")
        main_window.resize(1280, 720)
        main_window.setMinimumSize(QtCore.QSize(1280, 720))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(159, 159, 159))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(63, 63, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(159, 159, 159))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(63, 63, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(63, 63, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(63, 63, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        main_window.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        main_window.setWindowIcon(icon)
        main_window.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.chrome_start = QtWidgets.QPushButton(self.frame)
        self.chrome_start.setMinimumSize(QtCore.QSize(0, 40))
        self.chrome_start.setObjectName("chrome_start")
        self.horizontalLayout.addWidget(self.chrome_start)
        self.chrome_stop = QtWidgets.QPushButton(self.frame)
        self.chrome_stop.setMinimumSize(QtCore.QSize(0, 40))
        self.chrome_stop.setObjectName("chrome_stop")
        self.horizontalLayout.addWidget(self.chrome_stop)
        self.gridLayout.addWidget(self.frame, 0, 1, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.firefox_start = QtWidgets.QPushButton(self.frame_2)
        self.firefox_start.setMinimumSize(QtCore.QSize(0, 40))
        self.firefox_start.setObjectName("firefox_start")
        self.horizontalLayout_2.addWidget(self.firefox_start)
        self.firefox_stop = QtWidgets.QPushButton(self.frame_2)
        self.firefox_stop.setMinimumSize(QtCore.QSize(0, 40))
        self.firefox_stop.setObjectName("firefox_stop")
        self.horizontalLayout_2.addWidget(self.firefox_stop)
        self.gridLayout.addWidget(self.frame_2, 0, 3, 1, 1)
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.formLayout_2 = QtWidgets.QFormLayout(self.frame_4)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_8 = QtWidgets.QLabel(self.frame_4)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.firefox_area = QtWidgets.QLineEdit(self.frame_4)
        self.firefox_area.setObjectName("firefox_area")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.firefox_area)
        self.label_6 = QtWidgets.QLabel(self.frame_4)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.firefox_mission_num = QtWidgets.QLineEdit(self.frame_4)
        self.firefox_mission_num.setObjectName("firefox_mission_num")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.firefox_mission_num)
        self.firefox_mission_submit = QtWidgets.QPushButton(self.frame_4)
        self.firefox_mission_submit.setObjectName("firefox_mission_submit")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.firefox_mission_submit)
        self.gridLayout.addWidget(self.frame_4, 1, 3, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.formLayout = QtWidgets.QFormLayout(self.frame_3)
        self.formLayout.setObjectName("formLayout")
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.chrome_area = QtWidgets.QLineEdit(self.frame_3)
        self.chrome_area.setObjectName("chrome_area")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.chrome_area)
        self.label_4 = QtWidgets.QLabel(self.frame_3)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.chrome_mission_num = QtWidgets.QLineEdit(self.frame_3)
        self.chrome_mission_num.setObjectName("chrome_mission_num")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.chrome_mission_num)
        self.chrome_mission_submit = QtWidgets.QPushButton(self.frame_3)
        self.chrome_mission_submit.setObjectName("chrome_mission_submit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.chrome_mission_submit)
        self.gridLayout.addWidget(self.frame_3, 1, 1, 1, 1)
        self.firefox_log = QtWidgets.QTextBrowser(self.centralwidget)
        self.firefox_log.setObjectName("firefox_log")
        self.gridLayout.addWidget(self.firefox_log, 2, 3, 1, 1)
        self.chrome_log = QtWidgets.QTextBrowser(self.centralwidget)
        self.chrome_log.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.chrome_log.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.chrome_log.setObjectName("chrome_log")
        self.gridLayout.addWidget(self.chrome_log, 2, 1, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 0, 2, 3, 1)
        main_window.setCentralWidget(self.centralwidget)
        self.create_delete_button = QtWidgets.QAction(main_window)
        self.create_delete_button.setObjectName("create_delete_button")
        self.actionf = QtWidgets.QAction(main_window)
        self.actionf.setObjectName("actionf")
        self.actiong = QtWidgets.QAction(main_window)
        self.actiong.setObjectName("actiong")
        self.set_directory_button = QtWidgets.QAction(main_window)
        self.set_directory_button.setObjectName("set_directory_button")
        self.refresh_button = QtWidgets.QAction(main_window)
        self.refresh_button.setObjectName("refresh_button")
        self.scan_button = QtWidgets.QAction(main_window)
        self.scan_button.setObjectName("scan_button")
        self.backup_button = QtWidgets.QAction(main_window)
        self.backup_button.setObjectName("backup_button")
        self.load_button = QtWidgets.QAction(main_window)
        self.load_button.setObjectName("load_button")
        self.edit_action = QtWidgets.QAction(main_window)
        self.edit_action.setObjectName("edit_action")
        self.delete_action = QtWidgets.QAction(main_window)
        self.delete_action.setObjectName("delete_action")
        self.clear_filter_action = QtWidgets.QAction(main_window)
        self.clear_filter_action.setObjectName("clear_filter_action")

        self.retranslateUi(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "Main Window"))
        self.label.setText(_translate("main_window", "CHROME"))
        self.chrome_start.setText(_translate("main_window", "START"))
        self.chrome_stop.setText(_translate("main_window", "STOP"))
        self.label_2.setText(_translate("main_window", "FIREFOX"))
        self.firefox_start.setText(_translate("main_window", "START"))
        self.firefox_stop.setText(_translate("main_window", "STOP"))
        self.label_8.setText(_translate("main_window", "area url"))
        self.label_6.setText(_translate("main_window", "mission #"))
        self.firefox_mission_submit.setText(_translate("main_window", "submit"))
        self.label_3.setText(_translate("main_window", "area url"))
        self.label_4.setText(_translate("main_window", "mission #"))
        self.chrome_mission_submit.setText(_translate("main_window", "submit"))
        self.create_delete_button.setText(_translate("main_window", "Create and Delete"))
        self.actionf.setText(_translate("main_window", "f"))
        self.actiong.setText(_translate("main_window", "g"))
        self.set_directory_button.setText(_translate("main_window", "Set Directory"))
        self.refresh_button.setText(_translate("main_window", "Refresh"))
        self.scan_button.setText(_translate("main_window", "Scan Directory"))
        self.backup_button.setText(_translate("main_window", "Backup Database"))
        self.load_button.setText(_translate("main_window", "Load Backup"))
        self.edit_action.setText(_translate("main_window", "Edit"))
        self.delete_action.setText(_translate("main_window", "Delete"))
        self.clear_filter_action.setText(_translate("main_window", "Clear Filter"))
