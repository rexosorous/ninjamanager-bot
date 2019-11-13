from PyQt5.QtCore import QObject, pyqtSignal

class Signals(QObject):
    # signals need to be part of a sub-class of QObject
    info_signal = pyqtSignal()
    log_signal = pyqtSignal(str, str)
    ninja_signal = pyqtSignal(dict, str)
    options_signal = pyqtSignal(dict)
    area_signal = pyqtSignal(dict)
    recipe_signal = pyqtSignal(str, str, int)
    pin_signal = pyqtSignal(dict, str)