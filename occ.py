import sys
from PyQt5.QtWidgets import (
    QApplication,QWidget,QMainWindow,QFormLayout,QDialog,QLineEdit,QGridLayout,QVBoxLayout,QHBoxLayout,QPushButton,QDialogButtonBox
)
from PyQt5.QtCore import Qt

class occMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

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
        okayButton.clicked.connect(.close())
        errorLayout.addWidget(okayButton)
        self.setLayout(errorLayout)

if __name__ =="__main__":
    window=QApplication([])
    window=Error()
    window.show()
    sys.exit(occ.exec())