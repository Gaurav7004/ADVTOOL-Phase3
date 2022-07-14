from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QLabel,QMessageBox, QWidget

class Ui_Dialog_Upload(QtWidgets.QDialog):
    def __init__(self):
        # ! Inherited features 
        super(Ui_Dialog_Upload, self).__init__()
        self.setObjectName("Dialog")
        self.resize(519, 343)
        self.setStyleSheet("background-color: rgb(253, 248, 248);")
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 4)
        self.listWidget = QtWidgets.QListWidget(self)

        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 1, 0, 1, 5)
        self.pushButton_3 = QtWidgets.QPushButton(self)

        ###
        self.pushButton_3.clicked.connect(self.accept)

        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(158, 255, 197);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 2, 2, 1, 2)
        self.label = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 4)
        self.pushButton_4 = QtWidgets.QPushButton(self)

        self.pushButton_4.clicked.connect(self.Clear_List)

        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 159, 156);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 2, 4, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self)

        ###
        self.pushButton_2.clicked.connect(self.upload_single_file)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(158, 255, 197);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 2, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self)

        ##
        self.pushButton.clicked.connect(self.upload_multiples_files)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(158, 255, 197);")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 3, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 3, 1, 1, 4)

        self.pushButton_2.setText("Single File Upload")
        self.pushButton.setText("Multiple Files Upload")
        self.pushButton_3.setText("Ok")
        self.pushButton_4.setText("Clear")
        self.label_2.setText("* Note - Multiple file upload option will work only with same facility type.")
        self.label.setText("<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\"> Please select file / files </span></p></body></html>")


    ###? SIGNALS
    ###* --------
    def upload_multiples_files(self):
        global lst
        dialog = QtWidgets.QFileDialog(self)
        print(dialog)
        dialog.setWindowTitle('Choose Files')
        dialog.setFileMode(QtWidgets.QFileDialog.ExistingFiles)
        dialog.setNameFilters(["Select Excel Files (*.xls *.xlsx)"])

        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            self.listWidget.addItems(dialog.selectedFiles())

            self.fileName = []

            for i in range(self.listWidget.model().rowCount()):
                text = (f"{self.listWidget.item(i).text()}")
                self.fileName.append(text)

        dialog.deleteLater()

    def upload_single_file(self):
        global lst_single_file
        dialog = QtWidgets.QFileDialog(self)
        dialog.setWindowTitle('Choose File')
        dialog.setNameFilters(["Select Excel Files (*.xls *.xlsx)"])

        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            self.listWidget.addItems(dialog.selectedFiles())

            self.fileName = []

            for i in range(self.listWidget.model().rowCount()):
                text = (f"{self.listWidget.item(i).text()}")
                self.fileName.append(text)

        dialog.deleteLater()

    def accepted(self):
        self.close()

    def Clear_List(self):
        self.listWidget.clear()

        try:
            self.fileName.clear()
        except:
            pass
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Dialog_Upload()
    ui.show()
    sys.exit(app.exec_())
