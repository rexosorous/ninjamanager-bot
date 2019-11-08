# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_main_window(object):
    def setupUi(self, main_window):
        main_window.setObjectName("main_window")
        main_window.resize(1149, 450)
        main_window.setMinimumSize(QtCore.QSize(700, 450))
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
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.chrome_log = QtWidgets.QTextBrowser(self.centralwidget)
        self.chrome_log.setMinimumSize(QtCore.QSize(250, 0))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(8)
        self.chrome_log.setFont(font)
        self.chrome_log.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.chrome_log.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.chrome_log.setObjectName("chrome_log")
        self.horizontalLayout_3.addWidget(self.chrome_log)
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setMinimumSize(QtCore.QSize(300, 0))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_9 = QtWidgets.QFrame(self.frame_5)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_4.setContentsMargins(0, 0, -1, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.chrome_log_toggle = QtWidgets.QPushButton(self.frame_9)
        self.chrome_log_toggle.setMaximumSize(QtCore.QSize(25, 16777215))
        self.chrome_log_toggle.setObjectName("chrome_log_toggle")
        self.horizontalLayout_4.addWidget(self.chrome_log_toggle)
        self.label = QtWidgets.QLabel(self.frame_9)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.verticalLayout.addWidget(self.frame_9)
        self.frame = QtWidgets.QFrame(self.frame_5)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.chrome_start = QtWidgets.QPushButton(self.frame)
        self.chrome_start.setMinimumSize(QtCore.QSize(0, 40))
        self.chrome_start.setObjectName("chrome_start")
        self.horizontalLayout.addWidget(self.chrome_start)
        self.chrome_stop = QtWidgets.QPushButton(self.frame)
        self.chrome_stop.setMinimumSize(QtCore.QSize(0, 40))
        self.chrome_stop.setObjectName("chrome_stop")
        self.horizontalLayout.addWidget(self.chrome_stop)
        self.verticalLayout.addWidget(self.frame)
        self.line_2 = QtWidgets.QFrame(self.frame_5)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.label_3 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.frame_11 = QtWidgets.QFrame(self.frame_5)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_11)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 6)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.frame_12 = QtWidgets.QFrame(self.frame_11)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.formLayout_5 = QtWidgets.QFormLayout(self.frame_12)
        self.formLayout_5.setContentsMargins(0, 0, 5, 0)
        self.formLayout_5.setHorizontalSpacing(0)
        self.formLayout_5.setObjectName("formLayout_5")
        self.label_25 = QtWidgets.QLabel(self.frame_12)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_25.setFont(font)
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25.setObjectName("label_25")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.label_25)
        self.label_23 = QtWidgets.QLabel(self.frame_12)
        self.label_23.setObjectName("label_23")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_23)
        self.chrome_area = QtWidgets.QLineEdit(self.frame_12)
        self.chrome_area.setObjectName("chrome_area")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.chrome_area)
        self.label_24 = QtWidgets.QLabel(self.frame_12)
        self.label_24.setObjectName("label_24")
        self.formLayout_5.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_24)
        self.chrome_mission_num = QtWidgets.QLineEdit(self.frame_12)
        self.chrome_mission_num.setObjectName("chrome_mission_num")
        self.formLayout_5.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.chrome_mission_num)
        self.chrome_mission_submit = QtWidgets.QPushButton(self.frame_12)
        self.chrome_mission_submit.setObjectName("chrome_mission_submit")
        self.formLayout_5.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.chrome_mission_submit)
        self.horizontalLayout_6.addWidget(self.frame_12)
        self.frame_3 = QtWidgets.QFrame(self.frame_11)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.formLayout_6 = QtWidgets.QFormLayout(self.frame_3)
        self.formLayout_6.setContentsMargins(0, 0, 0, 0)
        self.formLayout_6.setObjectName("formLayout_6")
        self.label_28 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_28.setFont(font)
        self.label_28.setAlignment(QtCore.Qt.AlignCenter)
        self.label_28.setObjectName("label_28")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.label_28)
        self.label_26 = QtWidgets.QLabel(self.frame_3)
        self.label_26.setObjectName("label_26")
        self.formLayout_6.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_26)
        self.chrome_cooldown_lower = QtWidgets.QLineEdit(self.frame_3)
        self.chrome_cooldown_lower.setObjectName("chrome_cooldown_lower")
        self.formLayout_6.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.chrome_cooldown_lower)
        self.label_27 = QtWidgets.QLabel(self.frame_3)
        self.label_27.setObjectName("label_27")
        self.formLayout_6.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_27)
        self.chrome_cooldown_upper = QtWidgets.QLineEdit(self.frame_3)
        self.chrome_cooldown_upper.setObjectName("chrome_cooldown_upper")
        self.formLayout_6.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.chrome_cooldown_upper)
        self.chrome_cooldown_submit = QtWidgets.QPushButton(self.frame_3)
        self.chrome_cooldown_submit.setObjectName("chrome_cooldown_submit")
        self.formLayout_6.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.chrome_cooldown_submit)
        self.horizontalLayout_6.addWidget(self.frame_3)
        self.verticalLayout.addWidget(self.frame_11)
        self.line_3 = QtWidgets.QFrame(self.frame_5)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.label_13 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.verticalLayout.addWidget(self.label_13)
        self.frame_4 = QtWidgets.QFrame(self.frame_5)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.frame_7 = QtWidgets.QFrame(self.frame_4)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.formLayout_3 = QtWidgets.QFormLayout(self.frame_7)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setVerticalSpacing(14)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_5 = QtWidgets.QLabel(self.frame_7)
        self.label_5.setObjectName("label_5")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.chrome_loop_count = QtWidgets.QLineEdit(self.frame_7)
        self.chrome_loop_count.setReadOnly(True)
        self.chrome_loop_count.setObjectName("chrome_loop_count")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.chrome_loop_count)
        self.label_7 = QtWidgets.QLabel(self.frame_7)
        self.label_7.setObjectName("label_7")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.chrome_gold_gained = QtWidgets.QLineEdit(self.frame_7)
        self.chrome_gold_gained.setReadOnly(True)
        self.chrome_gold_gained.setObjectName("chrome_gold_gained")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.chrome_gold_gained)
        self.label_9 = QtWidgets.QLabel(self.frame_7)
        self.label_9.setObjectName("label_9")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.chrome_arena_battles = QtWidgets.QLineEdit(self.frame_7)
        self.chrome_arena_battles.setReadOnly(True)
        self.chrome_arena_battles.setObjectName("chrome_arena_battles")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.chrome_arena_battles)
        self.label_10 = QtWidgets.QLabel(self.frame_7)
        self.label_10.setObjectName("label_10")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.chrome_world_wins = QtWidgets.QLineEdit(self.frame_7)
        self.chrome_world_wins.setReadOnly(True)
        self.chrome_world_wins.setObjectName("chrome_world_wins")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.chrome_world_wins)
        self.label_11 = QtWidgets.QLabel(self.frame_7)
        self.label_11.setObjectName("label_11")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.chrome_world_losses = QtWidgets.QLineEdit(self.frame_7)
        self.chrome_world_losses.setReadOnly(True)
        self.chrome_world_losses.setObjectName("chrome_world_losses")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.chrome_world_losses)
        self.horizontalLayout_8.addWidget(self.frame_7)
        self.frame_16 = QtWidgets.QFrame(self.frame_4)
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.formLayout = QtWidgets.QFormLayout(self.frame_16)
        self.formLayout.setContentsMargins(6, 0, 0, 0)
        self.formLayout.setHorizontalSpacing(6)
        self.formLayout.setObjectName("formLayout")
        self.label_12 = QtWidgets.QLabel(self.frame_16)
        self.label_12.setObjectName("label_12")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.chrome_items_gained = QtWidgets.QTextEdit(self.frame_16)
        self.chrome_items_gained.setReadOnly(True)
        self.chrome_items_gained.setObjectName("chrome_items_gained")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.chrome_items_gained)
        self.label_6 = QtWidgets.QLabel(self.frame_16)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.chrome_ninjas = QtWidgets.QTextBrowser(self.frame_16)
        self.chrome_ninjas.setObjectName("chrome_ninjas")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.chrome_ninjas)
        self.horizontalLayout_8.addWidget(self.frame_16)
        self.verticalLayout.addWidget(self.frame_4)
        self.horizontalLayout_3.addWidget(self.frame_5)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_3.addWidget(self.line)
        self.frame_6 = QtWidgets.QFrame(self.centralwidget)
        self.frame_6.setMinimumSize(QtCore.QSize(300, 0))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_10 = QtWidgets.QFrame(self.frame_6)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_5.setContentsMargins(0, 0, -1, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.frame_10)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.firefox_log_toggle = QtWidgets.QPushButton(self.frame_10)
        self.firefox_log_toggle.setMaximumSize(QtCore.QSize(25, 16777215))
        self.firefox_log_toggle.setObjectName("firefox_log_toggle")
        self.horizontalLayout_5.addWidget(self.firefox_log_toggle)
        self.verticalLayout_2.addWidget(self.frame_10)
        self.frame_2 = QtWidgets.QFrame(self.frame_6)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.firefox_start = QtWidgets.QPushButton(self.frame_2)
        self.firefox_start.setMinimumSize(QtCore.QSize(0, 40))
        self.firefox_start.setObjectName("firefox_start")
        self.horizontalLayout_2.addWidget(self.firefox_start)
        self.firefox_stop = QtWidgets.QPushButton(self.frame_2)
        self.firefox_stop.setMinimumSize(QtCore.QSize(0, 40))
        self.firefox_stop.setObjectName("firefox_stop")
        self.horizontalLayout_2.addWidget(self.firefox_stop)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.line_4 = QtWidgets.QFrame(self.frame_6)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_2.addWidget(self.line_4)
        self.label_4 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.frame_13 = QtWidgets.QFrame(self.frame_6)
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_13)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 6)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.frame_15 = QtWidgets.QFrame(self.frame_13)
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.formLayout_8 = QtWidgets.QFormLayout(self.frame_15)
        self.formLayout_8.setContentsMargins(0, 0, 5, 0)
        self.formLayout_8.setObjectName("formLayout_8")
        self.label_33 = QtWidgets.QLabel(self.frame_15)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_33.setFont(font)
        self.label_33.setAlignment(QtCore.Qt.AlignCenter)
        self.label_33.setObjectName("label_33")
        self.formLayout_8.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.label_33)
        self.label_31 = QtWidgets.QLabel(self.frame_15)
        self.label_31.setObjectName("label_31")
        self.formLayout_8.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_31)
        self.firefox_area = QtWidgets.QLineEdit(self.frame_15)
        self.firefox_area.setObjectName("firefox_area")
        self.formLayout_8.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.firefox_area)
        self.label_32 = QtWidgets.QLabel(self.frame_15)
        self.label_32.setObjectName("label_32")
        self.formLayout_8.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_32)
        self.firefox_mission_num = QtWidgets.QLineEdit(self.frame_15)
        self.firefox_mission_num.setObjectName("firefox_mission_num")
        self.formLayout_8.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.firefox_mission_num)
        self.firefox_mission_submit = QtWidgets.QPushButton(self.frame_15)
        self.firefox_mission_submit.setObjectName("firefox_mission_submit")
        self.formLayout_8.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.firefox_mission_submit)
        self.horizontalLayout_7.addWidget(self.frame_15)
        self.frame_14 = QtWidgets.QFrame(self.frame_13)
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.formLayout_7 = QtWidgets.QFormLayout(self.frame_14)
        self.formLayout_7.setContentsMargins(0, 0, 0, 0)
        self.formLayout_7.setObjectName("formLayout_7")
        self.label_14 = QtWidgets.QLabel(self.frame_14)
        self.label_14.setObjectName("label_14")
        self.formLayout_7.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.firefox_cooldown_lower = QtWidgets.QLineEdit(self.frame_14)
        self.firefox_cooldown_lower.setObjectName("firefox_cooldown_lower")
        self.formLayout_7.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.firefox_cooldown_lower)
        self.label_29 = QtWidgets.QLabel(self.frame_14)
        self.label_29.setObjectName("label_29")
        self.formLayout_7.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_29)
        self.firefox_cooldown_upper = QtWidgets.QLineEdit(self.frame_14)
        self.firefox_cooldown_upper.setObjectName("firefox_cooldown_upper")
        self.formLayout_7.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.firefox_cooldown_upper)
        self.firefox_cooldown_submit = QtWidgets.QPushButton(self.frame_14)
        self.firefox_cooldown_submit.setObjectName("firefox_cooldown_submit")
        self.formLayout_7.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.firefox_cooldown_submit)
        self.label_30 = QtWidgets.QLabel(self.frame_14)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_30.setFont(font)
        self.label_30.setAlignment(QtCore.Qt.AlignCenter)
        self.label_30.setObjectName("label_30")
        self.formLayout_7.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.label_30)
        self.horizontalLayout_7.addWidget(self.frame_14)
        self.verticalLayout_2.addWidget(self.frame_13)
        self.line_5 = QtWidgets.QFrame(self.frame_6)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.verticalLayout_2.addWidget(self.line_5)
        self.label_18 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_18.setFont(font)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_2.addWidget(self.label_18)
        self.frame_17 = QtWidgets.QFrame(self.frame_6)
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_17)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.frame_8 = QtWidgets.QFrame(self.frame_17)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.formLayout_4 = QtWidgets.QFormLayout(self.frame_8)
        self.formLayout_4.setContentsMargins(-1, 0, 0, 0)
        self.formLayout_4.setVerticalSpacing(14)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_21 = QtWidgets.QLabel(self.frame_8)
        self.label_21.setObjectName("label_21")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_21)
        self.firefox_loop_count = QtWidgets.QLineEdit(self.frame_8)
        self.firefox_loop_count.setReadOnly(True)
        self.firefox_loop_count.setObjectName("firefox_loop_count")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.firefox_loop_count)
        self.label_15 = QtWidgets.QLabel(self.frame_8)
        self.label_15.setObjectName("label_15")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.firefox_gold_gained = QtWidgets.QLineEdit(self.frame_8)
        self.firefox_gold_gained.setReadOnly(True)
        self.firefox_gold_gained.setObjectName("firefox_gold_gained")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.firefox_gold_gained)
        self.label_19 = QtWidgets.QLabel(self.frame_8)
        self.label_19.setObjectName("label_19")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_19)
        self.firefox_arena_battles = QtWidgets.QLineEdit(self.frame_8)
        self.firefox_arena_battles.setReadOnly(True)
        self.firefox_arena_battles.setObjectName("firefox_arena_battles")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.firefox_arena_battles)
        self.label_20 = QtWidgets.QLabel(self.frame_8)
        self.label_20.setObjectName("label_20")
        self.formLayout_4.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_20)
        self.firefox_world_wins = QtWidgets.QLineEdit(self.frame_8)
        self.firefox_world_wins.setReadOnly(True)
        self.firefox_world_wins.setObjectName("firefox_world_wins")
        self.formLayout_4.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.firefox_world_wins)
        self.label_17 = QtWidgets.QLabel(self.frame_8)
        self.label_17.setObjectName("label_17")
        self.formLayout_4.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_17)
        self.firefox_world_losses = QtWidgets.QLineEdit(self.frame_8)
        self.firefox_world_losses.setReadOnly(True)
        self.firefox_world_losses.setObjectName("firefox_world_losses")
        self.formLayout_4.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.firefox_world_losses)
        self.horizontalLayout_9.addWidget(self.frame_8)
        self.frame_18 = QtWidgets.QFrame(self.frame_17)
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.formLayout_2 = QtWidgets.QFormLayout(self.frame_18)
        self.formLayout_2.setContentsMargins(-1, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_16 = QtWidgets.QLabel(self.frame_18)
        self.label_16.setObjectName("label_16")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.firefox_items_gained = QtWidgets.QTextEdit(self.frame_18)
        self.firefox_items_gained.setReadOnly(True)
        self.firefox_items_gained.setObjectName("firefox_items_gained")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.firefox_items_gained)
        self.label_8 = QtWidgets.QLabel(self.frame_18)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.firefox_ninjas = QtWidgets.QTextEdit(self.frame_18)
        self.firefox_ninjas.setReadOnly(True)
        self.firefox_ninjas.setObjectName("firefox_ninjas")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.firefox_ninjas)
        self.horizontalLayout_9.addWidget(self.frame_18)
        self.verticalLayout_2.addWidget(self.frame_17)
        self.horizontalLayout_3.addWidget(self.frame_6)
        self.firefox_log = QtWidgets.QTextBrowser(self.centralwidget)
        self.firefox_log.setMinimumSize(QtCore.QSize(250, 0))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(8)
        self.firefox_log.setFont(font)
        self.firefox_log.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.firefox_log.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.firefox_log.setObjectName("firefox_log")
        self.horizontalLayout_3.addWidget(self.firefox_log)
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
        main_window.setWindowTitle(_translate("main_window", "Ninjamanager Bot"))
        self.chrome_log_toggle.setText(_translate("main_window", "<<"))
        self.label.setText(_translate("main_window", "CHROME"))
        self.chrome_start.setText(_translate("main_window", "START"))
        self.chrome_stop.setText(_translate("main_window", "STOP"))
        self.label_3.setText(_translate("main_window", "OPTIONS"))
        self.label_25.setText(_translate("main_window", "WORLD MISSION"))
        self.label_23.setText(_translate("main_window", "area url"))
        self.label_24.setText(_translate("main_window", "mission #"))
        self.chrome_mission_submit.setText(_translate("main_window", "submit"))
        self.label_28.setText(_translate("main_window", "COOLDOWN"))
        self.label_26.setText(_translate("main_window", "lower"))
        self.label_27.setText(_translate("main_window", "upper"))
        self.chrome_cooldown_submit.setText(_translate("main_window", "submit"))
        self.label_13.setText(_translate("main_window", "INFO"))
        self.label_5.setText(_translate("main_window", "Loop Count"))
        self.label_7.setText(_translate("main_window", "Gold Gained"))
        self.label_9.setText(_translate("main_window", "Arena Battles"))
        self.label_10.setText(_translate("main_window", "World Wins"))
        self.label_11.setText(_translate("main_window", "World Losses"))
        self.label_12.setText(_translate("main_window", "Items Gained"))
        self.label_6.setText(_translate("main_window", "Ninja EXP"))
        self.label_2.setText(_translate("main_window", "FIREFOX"))
        self.firefox_log_toggle.setText(_translate("main_window", ">>"))
        self.firefox_start.setText(_translate("main_window", "START"))
        self.firefox_stop.setText(_translate("main_window", "STOP"))
        self.label_4.setText(_translate("main_window", "OPTIONS"))
        self.label_33.setText(_translate("main_window", "WORLD MISSION"))
        self.label_31.setText(_translate("main_window", "area url"))
        self.label_32.setText(_translate("main_window", "mission #"))
        self.firefox_mission_submit.setText(_translate("main_window", "submit"))
        self.label_14.setText(_translate("main_window", "lower"))
        self.label_29.setText(_translate("main_window", "upper"))
        self.firefox_cooldown_submit.setText(_translate("main_window", "submit"))
        self.label_30.setText(_translate("main_window", "COOLDOWN"))
        self.label_18.setText(_translate("main_window", "INFO"))
        self.label_21.setText(_translate("main_window", "Loop Count"))
        self.label_15.setText(_translate("main_window", "Gold Gained"))
        self.label_19.setText(_translate("main_window", "Arena Battles"))
        self.label_20.setText(_translate("main_window", "World Wins"))
        self.label_17.setText(_translate("main_window", "World Losses"))
        self.label_16.setText(_translate("main_window", "Items Gained"))
        self.label_8.setText(_translate("main_window", "Ninja EXP"))
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
