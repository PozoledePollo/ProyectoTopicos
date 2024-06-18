# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import pyodbc

class Ui_frmTercera(object):
    def setupUi(self, frmTercera):
        frmTercera.setObjectName("frmTercera")
        frmTercera.resize(769, 465)
        
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("imgs/ico/Blue key.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        frmTercera.setWindowIcon(icon) 

        self.tblDatos = QtWidgets.QTableWidget(frmTercera)
        self.tblDatos.setGeometry(QtCore.QRect(10, 10, 651, 231))
        self.tblDatos.setObjectName("tblDatos")
        self.tblDatos.setColumnCount(0)
        self.tblDatos.setRowCount(0)
        self.btnBorra = QtWidgets.QPushButton(frmTercera)
        self.btnBorra.setGeometry(QtCore.QRect(670, 20, 75, 23))
        self.btnBorra.setObjectName("btnBorra")
        self.grpComida = QtWidgets.QGroupBox(frmTercera)
        self.grpComida.setGeometry(QtCore.QRect(10, 260, 120, 91))
        self.grpComida.setObjectName("grpComida")
        self.cbChina = QtWidgets.QCheckBox(self.grpComida)
        self.cbChina.setGeometry(QtCore.QRect(20, 20, 70, 17))
        self.cbChina.setObjectName("cbChina")
        self.cbChina.setChecked(True)
        self.cbItaliana = QtWidgets.QCheckBox(self.grpComida)
        self.cbItaliana.setGeometry(QtCore.QRect(20, 50, 70, 17))
        self.cbItaliana.setObjectName("cbItaliana")
        self.calendario = QtWidgets.QCalendarWidget(frmTercera)
        self.calendario.setGeometry(QtCore.QRect(160, 260, 312, 183))
        self.calendario.setObjectName("calendario")
        self.lblFecha = QtWidgets.QLabel(frmTercera)
        self.lblFecha.setGeometry(QtCore.QRect(510, 270, 101, 16))
        self.lblFecha.setObjectName("lblFecha")
        self.edtFecha = QtWidgets.QLineEdit(frmTercera)
        self.edtFecha.setGeometry(QtCore.QRect(500, 290, 141, 20))
        self.edtFecha.setObjectName("edtFecha")
        self.edtFecha.setEnabled(False)
        #
        self.fullTable()
        #borrar logicamente toogled-->alternar(si/no)
        self.btnBorra.clicked.connect(self.delete)
        self.cbChina.toggled.connect(self.c1)
        self.cbItaliana.toggled.connect(self.c2)
        self.calendario.clicked.connect(self.getfechAct)

        #variables de clase
        self.china = None
        self.italiana = 1 # 1 si activo | 0 no activo
        self.fecha = None

        self.retranslateUi(frmTercera)
        QtCore.QMetaObject.connectSlotsByName(frmTercera)

    def getfechAct(self):
        self.fecha = QtCore.QDate.toString(self.calendario.selectedDate())
        self.edtFecha.setText(self.fecha)
        
    def c1(self):
        if(self.cbChina.isChecked()):
            self.china = 1
            print("Alternaste china a si")
        else:
            self.china = 0
            print("Alternaste china a no")

    def c2(self):
        if(self.cbItaliana.isChecked()):
            self.italiana = 1
            print("Alternaste italina a si")
        else:
            self.italiana = 0
            print("Alternaste italiana a no")


    def delete(self):
        #RECUPERAR DEL COMPONENTE TABLE LA FILA
        row = self.tblDatos.currentRow()
        idn = int(self.tblDatos.item(row, 0).text())
        #print(idn)
        msgbox = QtWidgets.QMessageBox()
        msgbox.setIcon(QtWidgets.QMessageBox.Warning)
        msgbox.setText("Deseas borrar este registro ??")
        msgbox.setWindowTitle("Advertencia")
        msgbox.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        resp = msgbox.exec()
        if(resp == QtWidgets.QMessageBox.Yes):
            #BAJA LOGICA
            conn = self.conexionMariaDB()
            if(conn != None):
                cur = conn.cursor()
                cur.execute("UPDATE clientes SET activo = 0 WHERE id = ?", idn)
                conn.commit()
                cur.close()
                conn.close()
                self.fullTable()


    def fullTable(self):
        conn = self.conexionMariaDB()
        if(conn != None):
            sql = "SELECT * FROM clientes WHERE activo = 1"
            cur = conn.cursor()
            cur.execute(sql)
            r = cur.fetchall()
            #filas y columnas
            rows = len(r)
            cols = len(r[0])
            #RECUPERAR LOS HEADERS O NOMBRES DE LOS ATRIBUTOS
            nom = [column[0] for column in cur.description]
            #print(nom)
            self.tblDatos.setColumnCount(cols)
            self.tblDatos.setRowCount(rows)
            item = QtWidgets.QTableWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
            fuente = QtGui.QFont()
            fuente.setBold(True)
            fuente.setPointSize(15)
            fuente.setItalic(True)
            fuente.setWeight(70)
            item.setFont(fuente)
            self.tblDatos.setHorizontalHeaderLabels(nom)
            #LLENO MI TABLA
            for c in range(cols):
                for f in range(rows):
                    self.tblDatos.setItem(f, c, QtWidgets.QTableWidgetItem("%s" % r[f][c]))
            cur.close()
            conn.close()
        else:
            msgbox = QtWidgets.QMessageBox()
            msgbox.setIcon(QtWidgets.QMessageBox.Critical)
            msgbox.setText("Hubo un error en la base de datos")
            msgbox.setWindowTitle("Error")
            msgbox.exec()            

    def conexionMariaDB(self):
        try:
            #print(pyodbc.drivers())
            txt = "DRIVER={MariaDB ODBC 3.1 Driver}; SERVER=localhost; "
            txt += "UID=root; PWD=admin; DATABASE=python; PORT=3306"
            conn = pyodbc.connect(txt)
        except Exception as err:
            conn = None
        return conn

    def retranslateUi(self, frmTercera):
        _translate = QtCore.QCoreApplication.translate
        frmTercera.setWindowTitle(_translate("frmTercera", "Tercera Interfaz"))
        self.btnBorra.setText(_translate("frmTercera", "Borrar"))
        self.grpComida.setTitle(_translate("frmTercera", "Tipo de Comida"))
        self.cbChina.setText(_translate("frmTercera", "China"))
        self.cbItaliana.setText(_translate("frmTercera", "Italiana"))
        self.lblFecha.setText(_translate("frmTercera", "Fecha seleccionada:"))

class Tercera(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        #OBJETO A LA CLASE Ui_frmTercera
        self.gui = Ui_frmTercera()
        self.gui.setupUi(self)