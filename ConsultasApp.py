import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget, QTableWidgetItem, QVBoxLayout
from PyQt5.QtWidgets import QLineEdit, QComboBox, QPushButton, QTextEdit
from PyQt5.QtGui import QFont
from PyQt5.QtCore import pyqtSlot
import rdflib
import requests
import shutil

g = rdflib.Graph()
g.parse('x.rdf')

qres = g.query(
            """SELECT DISTINCT ?aDescription
                WHERE {
                    ?a rdfs:label ?aDescription .
                }""")

font = QFont("Consolas")

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Prueba RDF'
        self.left = 0
        self.top = 30
        self.width = 1000
        self.height = 500
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        # textedit
        self.text_edit = QTextEdit(self)
        self.text_edit.setCurrentFont(font)
        self.text_edit.setPlaceholderText('Introduce la consulta')

        self.query_response = QTextEdit(self)
        self.query_response.setCurrentFont(font)


        # Search box
        self.query_text = QLineEdit(self)
        self.query_text.setPlaceholderText('Introduce la secuencia')
        self.queryBtn = QPushButton('Busqueda por secuencia', self)
        self.queryBtn.clicked[bool].connect(self.do_search_query)

        self.query_text2 = QLineEdit(self)
        self.query_text2.setPlaceholderText('Introduce el comentario')
        self.queryBtn5 = QPushButton('Busqueda por comentario', self)
        self.queryBtn5.clicked[bool].connect(self.do_search_query_comment)

        self.query_text3 = QLineEdit(self)
        self.query_text3.setPlaceholderText('Introduce la secuencia nueva')

        self.query_text4 = QLineEdit(self)
        self.query_text4.setPlaceholderText('Introduce la secuencia a eliminar')
        self.queryBtn6 = QPushButton('Cambiar cadena', self)
        self.queryBtn6.clicked[bool].connect(self.do_insert_query)

        self.queryBtn1 = QPushButton('Identificadores', self)
        self.queryBtn1.clicked[bool].connect(self.doIdentifierQuery)
        self.queryBtn2 = QPushButton('Etiquetas', self)
        self.queryBtn2.clicked[bool].connect(self.doLabelQuery)
        self.queryBtn3 = QPushButton('Publicaciones', self)
        self.queryBtn3.clicked[bool].connect(self.doPrimaryTopicOfQuery)
        self.queryBtn4 = QPushButton('Comentarios', self)
        self.queryBtn4.clicked[bool].connect(self.doCommentQuery)
        self.bigQueryBtn = QPushButton('Realizar consulta',self)
        self.bigQueryBtn.clicked[bool].connect(self.do_big_query)

        self.query_text5 = QLineEdit(self)
        self.query_text5.setPlaceholderText('Introduce la consulta de UniProt')

        self.APIQueryBtn = QPushButton('Consulta UNIPROT', self)
        self.APIQueryBtn.clicked[bool].connect(self.do_api_query)

        self.query_text6 = QLineEdit(self)
        self.query_text6.setPlaceholderText('Introduce la base de datos a usar')

        self.getRDFBtn = QPushButton('Seleccionar RDF', self)
        self.getRDFBtn.clicked[bool].connect(self.retrieve_rdf)



        # Add box layout, add table to box layout and add box layout to widget
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.text_edit)
        self.layout.addWidget(self.bigQueryBtn)

        self.layout.addWidget(self.queryBtn)
        self.layout.addWidget(self.query_text)

        self.layout.addWidget(self.queryBtn5)
        self.layout.addWidget(self.query_text2)

        self.layout.addWidget(self.queryBtn6)
        self.layout.addWidget(self.query_text3)
        self.layout.addWidget(self.query_text4)

        self.layout.addWidget(self.queryBtn1)
        self.layout.addWidget(self.queryBtn2)
        self.layout.addWidget(self.queryBtn3)
        self.layout.addWidget(self.queryBtn4)

        self.layout.addWidget(self.query_response)
        self.layout.addWidget(self.query_text5)
        self.layout.addWidget(self.APIQueryBtn)
        self.layout.addWidget(self.query_text6)
        self.layout.addWidget(self.getRDFBtn)

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


    def do_api_query(self):
        try:
            self.query_response.setText("Performing query ... " + 'http://www.uniprot.org/uniprot/?%s' % self.query_text5.text())
            r = requests.get(
                'http://www.uniprot.org/uniprot/%s' % self.query_text5.text())
            if r.status_code == 200:
                self.query_response.setText("API returned 200 - Parsing data.")
                self.query_response.setText(r.text)
        except Exception as e:
            self.query_response.setText(e.message)
            print(e.args)

    def retrieve_rdf(self):
        try:
            g.parse('%s.rdf' % self.query_text6.text())
        except Exception as e:
            self.query_response.setText(e.message)
            print(e.args)
        self.query_text6.setText("Base de datos seleccionada, ahora puedes hacer consultas en %s" % self.query_text6.text())


    def do_search_query(self):
        qtext = self.query_text.text()
        qres = g.query(
            """SELECT ?about ?value
               WHERE {
                  ?about rdf:value ?value
                  . FILTER(regex(str(?value), "%s"))
                  }
                  LIMIT 5""" % qtext)
        try:
            if len(qres) == 0:
                return
            for item in qres:
                num_cols = len(item)
                break
            num_rows = len(qres)
            self.tableWidget.setRowCount(num_rows)
            self.tableWidget.setColumnCount(num_cols)
            for idx, row in enumerate(qres):
                for cidx, col in enumerate(row):
                    self.tableWidget.setItem(idx, cidx, QTableWidgetItem(col.title()))
        except Exception as e:
            print(e.args)
            return

    def do_search_query_comment(self):
        qtext = self.query_text2.text()
        qres = g.query(
            """SELECT ?comment ?about
               WHERE {
                  ?about rdfs:comment ?comment
                  . FILTER(regex(str(?comment), "%s"))
                  }
                  LIMIT 5""" % qtext)

        try:
            if len(qres) == 0:
                return
            for item in qres:
                num_cols = len(item)
                break
            num_rows = len(qres)
            self.tableWidget.setRowCount(num_rows)
            self.tableWidget.setColumnCount(num_cols)
            for idx, row in enumerate(qres):
                for cidx, col in enumerate(row):
                    self.tableWidget.setItem(idx, cidx, QTableWidgetItem(col.title()))
        except Exception as e:
            print(e.args)
            return
    def do_big_query(self):
        try:
            q_text = self.text_edit.toPlainText()
            if 'INSERT' in q_text:
                g.update(q_text.replace('\n',''))
                return
            qres = g.query(q_text.replace('\n',''))
            if len(qres) == 0:
                return
            # get number of columns
            # hotfix, does not support indexing :(
            for item in qres:
                num_cols =  len(item)
                break
            # get number of rows
            num_rows = len(qres)
        except Exception as e:
            print(e.args)
            return
        try:
            # set table attribs if possible
            self.tableWidget.setRowCount(num_rows)
            self.tableWidget.setColumnCount(num_cols)
        except Exception as e:
            print(e.args)
        for ridx, row in enumerate(qres):
            for cidx, col in enumerate(row):
                print(col.title())
                self.tableWidget.setItem(ridx, cidx, QTableWidgetItem(col.title()))



    def doLabelQuery(self):

        qres = g.query(
            """SELECT DISTINCT ?aDescription
               WHERE {
                  ?a rdfs:label ?aDescription .
               }""")
        for item in qres:
            num_cols = len(item)
            break
        num_rows = len(qres)
        self.tableWidget.setRowCount(num_rows)
        self.tableWidget.setColumnCount(num_cols)
        for i, res in enumerate(qres):
            self.tableWidget.setItem(i, 0,
                                     QTableWidgetItem(res[0].replace('rdflib.term.Literal(\'', '').replace(')', '')))


    def doPrimaryTopicOfQuery(self):
        qres = g.query(
            """SELECT DISTINCT ?aDescription
               WHERE {
                  ?a rdf:type ?aPub .
                  ?a foaf:primaryTopicOf ?aDescription .
               }""")
        for item in qres:
            num_cols = len(item)
            break
        num_rows = len(qres)
        self.tableWidget.setRowCount(num_rows)
        self.tableWidget.setColumnCount(num_cols)
        for i, res in enumerate(qres):
            self.tableWidget.setItem(i, 0,
                                     QTableWidgetItem(res[0].replace('rdflib.term.Literal(\'', '').replace(')', '')))


    def doIdentifierQuery(self):
        qres = g.query(
            """SELECT DISTINCT ?aDescription
               WHERE {
                  ?a dcterms:identifier ?aDescription .
               }""")
        for item in qres:
            num_cols = len(item)
            break
        num_rows = len(qres)
        self.tableWidget.setRowCount(num_rows)
        self.tableWidget.setColumnCount(num_cols)

        for i, res in enumerate(qres):
            self.tableWidget.setItem(i, 0,
                                     QTableWidgetItem(res[0].replace('rdflib.term.Literal(\'', '').replace(')', '')))


    def doCommentQuery(self):
        qres = g.query(
            """SELECT DISTINCT ?aDescription
               WHERE {
                  ?a rdfs:comment ?aDescription .
               }""")
        for item in qres:
            num_cols = len(item)
            break
        num_rows = len(qres)
        self.tableWidget.setRowCount(num_rows)
        self.tableWidget.setColumnCount(num_cols)
        for i, res in enumerate(qres):
            self.tableWidget.setItem(i, 0,
                                     QTableWidgetItem(res[0].replace('rdflib.term.Literal(\'', '').replace(')', '')))


    def do_insert_query(self):
        qtext1 = self.query_text3.text()
        qtext2 = self.query_text4.text()
        qres = g.update(
            """ DELETE  {?about rdf:value ?value
                        }
                INSERT  {
                        ?about rdf:value "%s" .
                        }
                WHERE   {
                        ?about rdf:value ?value
                        . FILTER(regex(str(?value), "%s"))
                        }""" % (qtext1, qtext2))

        g.serialize(destination='chromosome.rdf')



    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
