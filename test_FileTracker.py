from PyQt5 import QtCore, QtWidgets

class C(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(C, self).__init__(parent)
        self.te = QtWidgets.QTextEdit()
        button = QtWidgets.QPushButton("Press me")
        button.clicked.connect(self.on_clicked)

        lay = QtWidgets.QVBoxLayout(self)
        lay.addWidget(self.te)
        lay.addWidget(button)

    @QtCore.pyqtSlot()
    def on_clicked(self):
        settings = QtCore.QSettings()
        path = settings.value("Paths/csvfile", QtCore.QDir.rootPath())
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Single File', path, '*.csv')
        if filename:
            self.te.setText(filename)
            finfo = QtCore.QFileInfo(filename)
            settings.setValue("Paths/csvfile", finfo.absoluteDir().absolutePath())

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.c = C()
        button = QtWidgets.QPushButton("Open C Dialog")
        button.clicked.connect(self.c.show)
        self.setCentralWidget(button)

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    QtCore.QCoreApplication.setOrganizationName("MySoft")
    QtCore.QCoreApplication.setOrganizationDomain("mysoft.com")
    QtCore.QCoreApplication.setApplicationName("MyApp")
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())