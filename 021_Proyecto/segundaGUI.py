# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import pyodbc

class Ui_frmSegunda(object):
    def setupUi(self, frmSegunda):
        frmSegunda.setObjectName("frmSegunda")
        frmSegunda.resize(636, 333)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("imgs/ico/Bomb.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        frmSegunda.setWindowIcon(icon)        

        self.grpInfo = QtWidgets.QGroupBox(frmSegunda)
        self.grpInfo.setGeometry(QtCore.QRect(20, 20, 591, 301))
        self.grpInfo.setObjectName("grpInfo")
        self.cmbTablas = QtWidgets.QComboBox(self.grpInfo)
        self.cmbTablas.setGeometry(QtCore.QRect(160, 20, 251, 22))
        self.cmbTablas.setObjectName("cmbTablas")
        self.btnCosulta = QtWidgets.QPushButton(self.grpInfo)
        self.btnCosulta.setGeometry(QtCore.QRect(250, 50, 75, 23))
        self.btnCosulta.setObjectName("btnCosulta")
        self.tblDatos = QtWidgets.QTableWidget(self.grpInfo)
        self.tblDatos.setGeometry(QtCore.QRect(10, 90, 561, 192))
        self.tblDatos.setObjectName("tblDatos")
        self.tblDatos.setColumnCount(0)
        self.tblDatos.setRowCount(0)

        self.retranslateUi(frmSegunda)
        QtCore.QMetaObject.connectSlotsByName(frmSegunda)
        #LLENAR EL COMBOBOX
        self.fullCombo()
        #VINCULAR EL PUSHBUTTON
        self.btnCosulta.clicked.connect(self.query)

    def query(self):
        #RECUPERAR DEL COMBOBOX EL ELEMENTO QUE SELECCIONO EL USUARIO
        index = self.cmbTablas.currentIndex()
        if(index != 0):
            self.fullTable(self.cmbTablas.itemText(index))
        else:
            msgbox = QtWidgets.QMessageBox()
            msgbox.setIcon(QtWidgets.QMessageBox.Critical)
            msgbox.setText("Debes de seleccionar una tabla")
            msgbox.setWindowTitle("Error")
            msgbox.exec()
    
    def fullTable(self, nomTabla):
        conn = self.conexionMariaDB()
        if(conn != None):
            sql = "SELECT * FROM "+nomTabla
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
    
    def fullCombo(self):
        try:
            self.cmbTablas.addItem("--- SELECCIONA UNA TABLA ---")
            #CONECTO A MI BASE DE DATOS
            conexion = self.conexionMariaDB()
            if(conexion != None):
                #print("ssiiiiiiii")
                cur = conexion.cursor()
                sql = "show tables;"
                cur.execute(sql)
                #RECUPERO EL CONTENIDO DE MI CONSULTA
                while 1:
                    tbl =cur.fetchone()
                    if not tbl:
                        break
                    else:
                        self.cmbTablas.addItem(tbl[0])
                cur.close()
                conexion.close()
            else: 
                msgbox = QtWidgets.QMessageBox()
                msgbox.setIcon(QtWidgets.QMessageBox.Critical)
                msgbox.setText("Hubo un error en la Base de datos")
                msgbox.setWindowTitle("Error")
                msgbox.exec()                
        except Exception as err:
            msgbox = QtWidgets.QMessageBox()
            msgbox.setIcon(QtWidgets.QMessageBox.Critical)
            msgbox.setText(err)
            msgbox.setWindowTitle("Error")
            msgbox.exec()

    def retranslateUi(self, frmSegunda):
        _translate = QtCore.QCoreApplication.translate
        frmSegunda.setWindowTitle(_translate("frmSegunda","Segunda GUI"))
        self.grpInfo.setTitle(_translate("frmSegunda","Datos"))
        self.btnCosulta.setText(_translate("frmSegunda","Consulta"))

    def conexionMariaDB(self):
        try:
            #print(pyodbc.drivers())
            txt = "DRIVER={MariaDB ODBC 3.1 Driver}; SERVER=localhost; "
            txt += "UID=root; PWD=admin; DATABASE=python; PORT=3306"
            conn = pyodbc.connect(txt)
        except Exception as err:
            conn = None
        return conn

    

class Segunda(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        #OBJETO A LA CLASE Ui_frmPrimera
        self.gui = Ui_frmSegunda()
        self.gui.setupUi(self)