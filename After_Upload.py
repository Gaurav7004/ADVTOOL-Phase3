from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import QFileDialog, QLabel,QMessageBox, QWidget

class Ui_Dialog_Upload(QtWidgets.QDialog):
    def __init__(self):
        # ! Inherited features 
        super(Ui_Dialog_Upload, self).__init__()
        self.setObjectName("Dialog")
        self.resize(371, 131)
        self.setStyleSheet("background-color: rgb(253, 248, 248);")
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 3, 0, 1, 1)

        self.pushButton_2 = QtWidgets.QPushButton(self)
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
        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 2)

        self.listWidget = QtWidgets.QListWidget()
        self.gridLayout.addWidget(self.listWidget, 4, 1, 1, 1)

        self.pushButton = QtWidgets.QPushButton(self)

        self.pushButton.clicked.connect(self.upload_multiples_file)

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
        self.label = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        QtCore.QMetaObject.connectSlotsByName(self)

        self.pushButton_3 = QtWidgets.QPushButton(self)
        self.pushButton_3.clicked.connect(self.accepted)
        self.gridLayout.addWidget(self.pushButton_3, 3, 1, 1, 2)

        self.pushButton_2.setText("Single File Upload")
        self.pushButton.setText("Multiple File Upload")
        self.pushButton_3.setText("Ok")

        self.label_2.setText("* Note - Multiple file upload option will work only with same facility type.")
        self.label.setText("<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">                 Please select </span></p></body></html>")

    ###? SIGNALS
    ###* --------
    def upload_multiples_file(self):
        options = QFileDialog.Options()
        self.fileName,_ = QFileDialog.getOpenFileNames(None, "Open Excel", (QtCore.QDir.homePath()), "Excel (*.xls *.xlsx)")
        print(self.fileName, type(self.fileName))
    def upload_single_file(self):
        self.fileName,_ = QFileDialog.getOpenFileName(None, "Open Excel", (QtCore.QDir.homePath()), "Excel (*.xls *.xlsx)")
        self.fileName = self.fileName.split(maxsplit=0)
        print(self.fileName[0], type(self.fileName))

    def accepted(self):
        self.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Dialog_Upload()
    ui.show()
    sys.exit(app.exec_())

#!
################################!
#!


# from PyQt5 import QtWidgets

# class Window(QtWidgets.QWidget):
#     def __init__(self):
#         super().__init__()
#         self.button = QtWidgets.QPushButton('Choose Files')
#         self.button.clicked.connect(self.handleChooseDirectories)
#         self.listWidget = QtWidgets.QListWidget()
#         layout = QtWidgets.QVBoxLayout(self)
#         layout.addWidget(self.listWidget)
#         layout.addWidget(self.button)

#     def handleChooseDirectories(self):
#         dialog = QtWidgets.QFileDialog(self)
#         dialog.setWindowTitle('Choose Files')
#         dialog.setFileMode(QtWidgets.QFileDialog.ExistingFiles)

#         if dialog.exec_() == QtWidgets.QDialog.Accepted:
#             self.listWidget.addItems(dialog.selectedFiles())

#             lst = []

#             for i in range(self.listWidget.model().rowCount()):
#                 text = (f"{self.listWidget.item(i).text()}\n")
#                 print(i, text)
#                 lst.append(text)

#             print(set(lst))

#         dialog.deleteLater()

# if __name__ == '__main__':

#     app = QtWidgets.QApplication(['Test'])
#     window = Window()
#     window.show()
#     app.exec_()