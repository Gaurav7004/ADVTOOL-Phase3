import sys

import threading
from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage

import dash
import dash_core_components as dcc
import dash_html_components as html


def run_dash(data, layout):
    app = dash.Dash()

    app.layout = html.Div(children=[
        html.H1(children='Plots in Dash'),

        html.Div(children='''
            Dash: A web application framework for Python.
        '''),

        dcc.Graph(
            id='example-graph',
            figure={
                'data': data,
                'layout': layout
            })
        ])
    app.run_server(debug=False)


##########################################################################################
class WebEnginePage(QtWebEngineWidgets.QWebEnginePage):
    def createWindow(self, _type):
        page = WebEnginePage(self)
        page.urlChanged.connect(self.on_url_changed)
        return page

    @QtCore.pyqtSlot(QtCore.QUrl)
    def on_url_changed(self, url):
        page = self.sender()
        self.setUrl(url)
        page.deleteLater()

##############################################################################################
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        # ! Inherited features 
        super(MainWindow, self).__init__()
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
        self.pushButton_3.setText("Display Plots")
        self.pushButton_3.clicked.connect(self.open_webbrowser)

        self.browser = QtWebEngineWidgets.QWebEngineView()
        
    def open_webbrowser(self):
        page = WebEnginePage(self.browser)
        self.browser.setPage(page)
        self.browser.load(QtCore.QUrl("http://127.0.0.1:8050/"))
        self.setCentralWidget(self.browser)


if __name__ == '__main__':
    data = [
        {'x': ['JANUARY', 'FEBRUARY', 'MARCH'], 'y': [4, 1, 2], 'type': 'bar', 'name': 'UP'},
        {'x': ['JANUARY', 'FEBRUARY', 'MARCH'], 'y': [2, 4, 5], 'type': 'bar', 'name': u'MP'},
        {'x': ['JANUARY', 'FEBRUARY', 'MARCH'], 'y': [2, 1, 9], 'type': 'bar', 'name': u'AP'},
        {'x': ['JANUARY', 'FEBRUARY', 'MARCH'], 'y': [5, 4, 1], 'type': 'bar', 'name': u'JH'},
        {'x': ['JANUARY', 'FEBRUARY', 'MARCH'], 'y': [2, 9, 11], 'type': 'bar', 'name': u'DL'},
        {'x': ['JANUARY', 'FEBRUARY', 'MARCH'], 'y': [4, 1, 2], 'type': 'bar', 'name': 'UP'},
        {'x': ['JANUARY', 'FEBRUARY', 'MARCH'], 'y': [2, 4, 5], 'type': 'bar', 'name': u'MP'},
        {'x': ['JANUARY', 'FEBRUARY', 'MARCH'], 'y': [2, 1, 9], 'type': 'bar', 'name': u'AP'},
        {'x': ['JANUARY', 'FEBRUARY', 'MARCH'], 'y': [5, 4, 1], 'type': 'bar', 'name': u'JH'},
        {'x': ['JANUARY', 'FEBRUARY', 'MARCH'], 'y': [2, 9, 11], 'type': 'bar', 'name': u'DL'}
    ]

    layout = {
        'title': 'Dash Data Visualization'
    }

    threading.Thread(target=run_dash, args=(data, layout), daemon=True).start()
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())



###! -------------------------------------------------------------------------------------------------------
###! -------------------------------------------------------------------------------------------------------

# import sys
# import threading

# from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets

# import dash
# import dash_core_components as dcc
# import dash_html_components as html
# import plotly.figure_factory as ff


# class QDash(QtCore.QObject):
#     def __init__(self, parent=None):
#         super().__init__(parent)

#         self._app = dash.Dash()
#         self.app.layout = html.Div()

#     @property
#     def app(self):
#         return self._app

#     def update_graph(self, df):
#         fig = ff.create_gantt(df)
#         self.app.layout = html.Div([dcc.Graph(figure=fig)])

#     def run(self, **kwargs):
#         threading.Thread(target=self.app.run_server, kwargs=kwargs, daemon=True).start()


# class Mainwindow(QtWidgets.QMainWindow):
#     def __init__(self, parent=None):
#         super().__init__(parent)

#         self.browser = QtWebEngineWidgets.QWebEngineView()
#         self.table = QtWidgets.QTableWidget()
#         self.button = QtWidgets.QPushButton("Press me")

#         central_widget = QtWidgets.QWidget()
#         self.setCentralWidget(central_widget)
#         lay = QtWidgets.QVBoxLayout(central_widget)
#         lay.addWidget(self.browser, stretch=1)
#         lay.addWidget(self.table, stretch=1)
#         lay.addWidget(self.button)

#         self.resize(640, 480)

#         self.table.setColumnCount(3)
#         self.table.setHorizontalHeaderLabels(("X", "Y1", "Y2"))
#         header = self.table.horizontalHeader()
#         for i in range(self.table.columnCount()):
#             header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)

#         self.qdask = QDash()
#         self.qdask.run(debug=True, use_reloader=False)
#         self.browser.load(QtCore.QUrl("http://127.0.0.1:8050"))

#         self.button.clicked.connect(self.update_figure)

#         current_date = QtCore.QDateTime.currentDateTime()

#         for i in range(3):
#             self.append_row(
#                 task="Task{}".format(i),
#                 start=current_date,
#                 finish=current_date.addDays(i + 1),
#             )

#     @QtCore.pyqtSlot()
#     def update_figure(self):

#         df = []

#         for i in range(self.table.rowCount()):
#             task = self.table.item(i, 0).data(QtCore.Qt.DisplayRole)
#             start = (
#                 self.table.item(i, 1)
#                 .data(QtCore.Qt.DisplayRole)
#                 .toString(QtCore.Qt.ISODateWithMs)
#             )
#             finish = (
#                 self.table.item(i, 2)
#                 .data(QtCore.Qt.DisplayRole)
#                 .toString(QtCore.Qt.ISODateWithMs)
#             )

#             d = dict(Task=task, Start=start, Finish=finish)
#             df.append(d)

#         print(df)

#         self.qdask.update_graph(df)
#         self.browser.reload()

#     def append_row(
#         self,
#         task="",
#         start=QtCore.QDateTime.currentDateTime(),
#         finish=QtCore.QDateTime.currentDateTime(),
#     ):
#         row = self.table.rowCount()
#         self.table.insertRow(row)
#         for column, value in enumerate((task, start, finish)):
#             it = QtWidgets.QTableWidgetItem()
#             it.setData(QtCore.Qt.DisplayRole, value)
#             self.table.setItem(row, column, it)


# if __name__ == "__main__":

#     app = QtWidgets.QApplication(sys.argv)
#     app.setStyle(QtWidgets.QStyleFactory.create("Fusion"))

#     w = Mainwindow()
#     w.show()

#     sys.exit(app.exec_())