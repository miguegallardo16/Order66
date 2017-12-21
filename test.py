import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget, QTableWidgetItem, QVBoxLayout
from PyQt5.QtWidgets import QLineEdit, QComboBox, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import rdflib

g = rdflib.Graph()
g.parse('D:/Users/Migue/PycharmProjects/Estandares/chromosome.rdf')
qres = g.query(
            """SELECT DISTINCT ?aDescription
                WHERE {
                    ?a rdfs:label ?aDescription .
                }""")
class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Prueba RDF'
        self.left = 0
        self.top = 0
        self.width = 500
        self.height = 200
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        # Search box
        self.query_text = QLineEdit(self)
        self.queryBtn = QPushButton('Query labels', self)
        self.queryBtn.clicked[bool].connect(self.doQuery)
        self.queryBtn2 = QPushButton('Query identifiers', self)
        self.queryBtn2.clicked[bool].connect(self.doIdentifierQuery)

        # Combobox
        self.combo = QComboBox(self)
        self.combo.addItem("Query A")
        self.combo.addItem("Query B")
        self.combo.addItem("Query C")
        self.combo.move(50,50)
        self.createTable()

        # Add box layout, add table to box layout and add box layout to widget
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget)
        self.layout.addWidget(self.combo)
        self.layout.addWidget(self.query_text)
        self.layout.addWidget(self.queryBtn)
        self.layout.addWidget(self.queryBtn2)
        self.setLayout(self.layout)

        # Show widget
        self.show()

    def createTable(self):
        # Create table
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(4)
        self.tableWidget.setColumnCount(1)
        """self.tableWidget.setItem(0, 0, QTableWidgetItem("Cell (1,1)"))
        self.tableWidget.setItem(0, 1, QTableWidgetItem("Cell (1,2)"))
        self.tableWidget.setItem(1, 0, QTableWidgetItem("Cell (2,1)"))
        self.tableWidget.setItem(1, 1, QTableWidgetItem("Cell (2,2)"))
        self.tableWidget.setItem(2, 0, QTableWidgetItem("Cell (3,1)"))
        self.tableWidget.setItem(2, 1, QTableWidgetItem("Cell (3,2)"))
        self.tableWidget.setItem(3, 0, QTableWidgetItem("Cell (4,1)"))
        self.tableWidget.setItem(3, 1, QTableWidgetItem("Cell (4,2)"))"""
        self.tableWidget.move(0, 0)

        # table selection change
        self.tableWidget.doubleClicked.connect(self.on_click)


    def doQuery(self):
        qres = g.query(
            """SELECT DISTINCT ?aDescription
                WHERE {
                    ?a rdfs:label ?aDescription .
                }""")
        for i, res in enumerate(qres):
            self.tableWidget.setItem(i, 0, QTableWidgetItem(res[0].replace('rdflib.term.Literal(\'', '').replace(')', '')))
    def doIdentifierQuery(self):
        qres = g.query(
            """SELECT DISTINCT ?aDescription
                WHERE {
                    ?a dcterms:identifier ?aDescription .
                }""")
        for i, res in enumerate(qres):
            self.tableWidget.setItem(i, 0,
                                     QTableWidgetItem(res[0].replace('rdflib.term.Literal(\'', '').replace(')', '')))
    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())