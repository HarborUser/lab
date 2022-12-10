from PyQt5.QtWidgets import *
from menu import *


QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)





class Controller(QMainWindow, Ui_CT):


    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.setupUi(self)
        self.pushButton.clicked.connect(lambda: self.submit())


    def submit(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_menu_stage()
        self.ui.setupUi(self.window)
        self.window.show()









