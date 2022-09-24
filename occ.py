import sys
from PyQt5.QtWidgets import (
    QApplication,QWidget,QMainWindow,QFormLayout,QDialog,QLineEdit,QGridLayout,QVBoxLayout,QHBoxLayout,QPushButton,QDialogButtonBox
)
from PyQt5.QtCore import Qt

#mainwindow
class occMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("OCC")
        self.setFixedSize(640,320)
        self.parentlayout = QVBoxLayout()
        centralWidget = QWidget(self)
        centralWidget.setLayout(self.parentlayout)
        self.setCentralWidget(centralWidget)
        self._display()
        self._form()
        self._add()
        self._button()

    def _display(self):
        self.xdisplay = QLineEdit()
        self.xdisplay.setReadOnly(True)
        self.parentlayout.addWidget(self.xdisplay)
        self.ydisplay = QLineEdit()
        self.ydisplay.setReadOnly(True)
        self.parentlayout.addWidget(self.ydisplay)

    def _form(self):    
        self.formlayout = QFormLayout()
        self.x = QLineEdit()
        self.y = QLineEdit()
        self.x.setFixedWidth(50)
        self.y.setFixedWidth(50)
        self.formlayout.addRow("Ea value : ", self.x)
        self.formlayout.addRow("If value : ",self.y)
        self.parentlayout.addLayout(self.formlayout)

    def _add(self):
        self.add = QPushButton("Add")
        self.parentlayout.addWidget(self.add)
            
    def _button(self):
        self.submit = QPushButton("submit")
        self.clear = QPushButton("clear")
        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.addWidget(self.submit)
        self.buttonLayout.addWidget(self.clear)
        self.parentlayout.addLayout(self.buttonLayout)

    def setDisplayText(self,x,y):
        self.xdisplay.setText(x)
        self.xdisplay.setFocus()
        self.ydisplay.setText(y)
        self.ydisplay.setFocus()

    def displayText(self):
        return self.xdisplay.x(), self.ydisplay.y()

    def clearDisplaytext(self):
        self.setDisplayText("","")



#error dialog box
class Error(QDialog):
    def __init__(self):
        super().__init__()#parent="mainWin"
        self.setWindowTitle("Error")
        #self.setFixedSize(30,15)
        errorLayout = QVBoxLayout()
        errorFLayout = QHBoxLayout()
        errorField = QLineEdit("Error")
        errorField.setAlignment(Qt.AlignmentFlag.AlignCenter)
        errorField.setReadOnly(True)
        errorFLayout.addWidget(errorField)
        errorLayout.addLayout(errorFLayout)
        okayButton = QDialogButtonBox()
        okayButton.setStandardButtons(QDialogButtonBox.StandardButton.Ok)
        okayButton.clicked.connect(lambda:self.close())
        errorLayout.addWidget(okayButton)
        self.setLayout(errorLayout)

if __name__ =="__main__":
    occ=QApplication([])
    window=occMainWindow()
    window.show()
    sys.exit(occ.exec())