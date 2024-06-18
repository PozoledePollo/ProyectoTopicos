#Hola!!!!!
# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from Control.Clientes_ctrl import * 
import sys

class Clientes(object):
    def setupUi(self, frmClientes):
        frmClientes.setObjectName("frmClientes")
        frmClientes.resize(788, 439)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("imgs/ico/Alien.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        frmClientes.setWindowIcon(icon)  

        self.tblDatos = QtWidgets.QTableWidget(frmClientes)
        self.tblDatos.setGeometry(QtCore.QRect(10, 10, 761, 141))
        self.tblDatos.setObjectName("tblDatos")
        self.tblDatos.setColumnCount(0)
        self.tblDatos.setRowCount(0)
        self.btnNuevo = QtWidgets.QPushButton(frmClientes)
        self.btnNuevo.setGeometry(QtCore.QRect(240, 160, 75, 23))
        self.btnNuevo.setObjectName("btnNuevo")
        self.btnBorrar = QtWidgets.QPushButton(frmClientes)
        self.btnBorrar.setGeometry(QtCore.QRect(340, 160, 75, 23))
        self.btnBorrar.setObjectName("btnBorrar")
        self.btnActualizar = QtWidgets.QPushButton(frmClientes)
        self.btnActualizar.setGeometry(QtCore.QRect(440, 160, 75, 23))
        self.btnActualizar.setObjectName("btnActualizar")
        self.gprRegistro = QtWidgets.QGroupBox(frmClientes)
        self.gprRegistro.setGeometry(QtCore.QRect(110, 200, 501, 211))
        self.gprRegistro.setObjectName("gprRegistro")
        self.gprRegistro.setVisible(False)
        self.btnGuardar = QtWidgets.QPushButton(self.gprRegistro)
        self.btnGuardar.setGeometry(QtCore.QRect(210, 170, 75, 23))
        self.btnGuardar.setObjectName("btnGuardar")
        self.widget = QtWidgets.QWidget(self.gprRegistro)
        self.widget.setGeometry(QtCore.QRect(10, 30, 226, 119))
        self.widget.setObjectName("widget")
        self.capaNombre = QtWidgets.QGridLayout(self.widget)
        self.capaNombre.setContentsMargins(0, 0, 0, 0)
        self.capaNombre.setObjectName("capaNombre")
        self.lblPrimer = QtWidgets.QLabel(self.widget)
        self.lblPrimer.setObjectName("lblPrimer")
        self.capaNombre.addWidget(self.lblPrimer, 1, 0, 1, 1)
        self.edtSegundo = QtWidgets.QLineEdit(self.widget)
        self.edtSegundo.setObjectName("edtSegundo")
        self.capaNombre.addWidget(self.edtSegundo, 2, 1, 1, 1)
        self.edtNombre = QtWidgets.QLineEdit(self.widget)
        self.edtNombre.setObjectName("edtNombre")
        self.capaNombre.addWidget(self.edtNombre, 0, 1, 1, 1)
        self.edePrimer = QtWidgets.QLineEdit(self.widget)
        self.edePrimer.setObjectName("edePrimer")
        self.capaNombre.addWidget(self.edePrimer, 1, 1, 1, 1)
        self.edtTel = QtWidgets.QLineEdit(self.widget)
        self.edtTel.setObjectName("edtTel")
        self.capaNombre.addWidget(self.edtTel, 3, 1, 1, 1)
        self.lblTel = QtWidgets.QLabel(self.widget)
        self.lblTel.setObjectName("lblTel")
        self.capaNombre.addWidget(self.lblTel, 3, 0, 1, 1)
        self.lblSegundo = QtWidgets.QLabel(self.widget)
        self.lblSegundo.setObjectName("lblSegundo")
        self.capaNombre.addWidget(self.lblSegundo, 2, 0, 1, 1)
        self.lblNombre = QtWidgets.QLabel(self.widget)
        self.lblNombre.setObjectName("lblNombre")
        self.capaNombre.addWidget(self.lblNombre, 0, 0, 1, 1)
        self.widget1 = QtWidgets.QWidget(self.gprRegistro)
        self.widget1.setGeometry(QtCore.QRect(260, 30, 223, 126))
        self.widget1.setObjectName("widget1")
        self.capaDireccion = QtWidgets.QGridLayout(self.widget1)
        self.capaDireccion.setContentsMargins(0, 0, 0, 0)
        self.capaDireccion.setObjectName("capaDireccion")
        self.lblCalle = QtWidgets.QLabel(self.widget1)
        self.lblCalle.setObjectName("lblCalle")
        self.capaDireccion.addWidget(self.lblCalle, 0, 0, 1, 1)
        self.edtCalle = QtWidgets.QLineEdit(self.widget1)
        self.edtCalle.setObjectName("edtCalle")
        self.capaDireccion.addWidget(self.edtCalle, 0, 1, 1, 1)
        self.lblCol = QtWidgets.QLabel(self.widget1)
        self.lblCol.setObjectName("lblCol")
        self.capaDireccion.addWidget(self.lblCol, 1, 0, 1, 1)
        self.edtCol = QtWidgets.QLineEdit(self.widget1)
        self.edtCol.setObjectName("edtCol")
        self.capaDireccion.addWidget(self.edtCol, 1, 1, 1, 1)
        self.lblNum = QtWidgets.QLabel(self.widget1)
        self.lblNum.setObjectName("lblNum")
        self.capaDireccion.addWidget(self.lblNum, 2, 0, 1, 1)
        self.edtNum = QtWidgets.QLineEdit(self.widget1)
        self.edtNum.setObjectName("edtNum")
        self.capaDireccion.addWidget(self.edtNum, 2, 1, 1, 1)
        self.lblCP = QtWidgets.QLabel(self.widget1)
        self.lblCP.setObjectName("lblCP")
        self.capaDireccion.addWidget(self.lblCP, 3, 0, 1, 1)
        self.edtCP = QtWidgets.QLineEdit(self.widget1)
        self.edtCP.setObjectName("edtCP")
        self.capaDireccion.addWidget(self.edtCP, 3, 1, 1, 1)
        self.lblSal = QtWidgets.QLabel(self.widget1)
        self.lblSal.setObjectName("lblSal")
        self.capaDireccion.addWidget(self.lblSal, 4, 0, 1, 1)
        self.edtSal = QtWidgets.QLineEdit(self.widget1)
        self.edtSal.setObjectName("edtSal")
        self.capaDireccion.addWidget(self.edtSal, 4, 1, 1, 1)

        self.retranslateUi(frmClientes)
        QtCore.QMetaObject.connectSlotsByName(frmClientes)
        objCtrl = Clientes_ctrl()
        datos = objCtrl.obtenerDatos()
        self.fullTable(datos)
        #borrar logicamente
        self.tblDatos.setCurrentCell(-1,-1)
        self.btnBorrar.clicked.connect(self.delete)
        self.btnNuevo.clicked.connect(self.insert)
        self.btnGuardar.clicked.connect(self.save)
        self.btnActualizar.clicked.connect(self.update)

    def update(self):
        row = self.tblDatos.currentRow()
        self.idn = int(self.tblDatos.item(row,0).text())
        self.edtNombre.setText(self.tblDatos.item(row,1).text())
        self.edePrimer.setText(self.tblDatos.item(row,2).text())
        self.edtSegundo.setText(self.tblDatos.item(row,3).text())
        self.edtTel.setText(self.tblDatos.item(row,4).text())
        self.edtCalle.setText(self.tblDatos.item(row,5).text())
        self.edtCol.setText(self.tblDatos.item(row,6).text())
        self.edtNum.setText(self.tblDatos.item(row,7).text())
        self.edtCP.setText(self.tblDatos.item(row,8).text())
        self.edtSal.setText(self.tblDatos.item(row,9).text())
        self.edtSal.setEnabled(False)
        self.gprRegistro.setVisible(True)
        self.gprRegistro.setTitle("ACTUALIZAR DATOS")
        self.opc = 2 # ACTUALIZAR

    def msg(self, txt, opc, b):
        msgbox = QtWidgets.QMessageBox()
        match(opc):
            case 1:
                msgbox.setIcon(QtWidgets.QMessageBox.Critical)
                msgbox.setWindowTitle("Error")
            case 2:
                msgbox.setIcon(QtWidgets.QMessageBox.Warning)
                msgbox.setWindowTitle("Advertencia")
                if(b == 1):
                    msgbox.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            case 3:
                msgbox.setIcon(QtWidgets.QMessageBox.Information)
                msgbox.setWindowTitle("Información")
        msgbox.setText(txt)
        if(b == 1):
            return msgbox.exec()
        else:
            msgbox.exec()

    def ubicarMsg(self, m):
        # m[0] = 1 txt | 2 tel | 3 num | 4 salario
        # m[1] = texto o True
        match(m[0]):
            case 1: 
                self.msg(m[1]+" debe tener letras, verificalo!!", 3,0)
            case 2:
                self.msg(m[1]+ "debe tener el siguiente formato: \n nnn-nnn-nnnn", 3,0)
            case 3: 
                self.msg(m[1]+ " debe contener numeros, verificalo!!", 3,0)
            case 4:
                self.msg(m[1]+ " no es un numero con punto decimal", 3,0)
        
        return m[1]        


    def save(self):
        #RECUPERAR LOS DATOS DEL FORMULARIO
        nom = self.edtNombre.text().upper()
        pa = self.edePrimer.text().upper()
        sa = self.edtSegundo.text().upper()
        tel = self.edtTel.text()
        calle = self.edtCalle.text().upper()
        col = self.edtCol.text().upper()
        num = self.edtNum.text()
        cp = self.edtCP.text()
        sal = self.edtSal.text()
        #VALIDACION DE TODOS LOS CAMPOS
        objCtrl = Clientes_ctrl()
        v = objCtrl.validacionDatos(nom, pa, sa, tel, calle, col, num, cp, sal)
        t = self.ubicarMsg(v)
        if(t == True):
            #PUEDO INSERTAR LOS DATOS SIN ANTES SABER
            #QUE OPCION PUSO EL USUARIO
            if(self.opc == 1): #INSERTAR
                si = objCtrl.guardar(nom, pa, sa, tel, calle, col, num, cp, sal)
                if(si != False):
                    self.msg("Se guardo correctamente!", 1,0)
                    datos = objCtrl.obtenerDatos()
                    self.fullTable(datos)
                    self.borrarContenido()
                else:
                    self.msg("No se puede insertar, debido a que ya existe en la base",3)
            elif(self.opc == 2):
                #actualizar
                ok = objCtrl.actualizar(nom, pa, sa, tel, calle, col, num, cp, self.idn)
                if(ok != False):
                    self.msg("Se actualizo correctamente!", 3,0)
                    datos = objCtrl.obtenerDatos()
                    self.fullTable(datos)
                    self.borrarContenido()

    def borrarContenido(self):
        self.edtNombre.setText("")
        self.edePrimer.setText("")
        self.edtSegundo.setText("")
        self.edtTel.setText("")
        self.edtCalle.setText("")
        self.edtCol.setText("")
        self.edtNum.setText("")
        self.edtCP.setText("")
        self.edtSal.setText("")
        self.gprRegistro.setVisible(False)
        self.tblDatos.setCurrentCell(-1,-1)                                                

    def insert(self):
        self.gprRegistro.setVisible(True)
        self.gprRegistro.setTitle("INSERTAR NUEVO REGISTRO")
        self.opc = 1 # opcion 1: insertar nuevo registro

    def delete(self):
        #RECUPERAR DEL COMPONENTE TABLE LA FILA
        row = self.tblDatos.currentRow()
        if(row != -1):
            dato = self.tblDatos.item(row, 1).text()
            resp = self.msg("Deseas borrar a: "+dato+" ??",2,1)
            if(resp == QtWidgets.QMessageBox.Yes):
                #BAJA LOGICA
                objCtrl = Clientes_ctrl()
                v = objCtrl.borrarLogico(int(self.tblDatos.item(row, 0).text()))
                if(v != False):
                    datos = objCtrl.obtenerDatos()
                    self.fullTable(datos)
        else:
            self.msg("Debes de seleccionar una celda de la tabla de datos", 3, 0)

    def fullTable(self, datos):
        if(datos != False):
            #filas y columnas
            nomCols = datos[0]
            info = datos[1]
            rows = len(info)
            cols = len(info[0])
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
            self.tblDatos.setHorizontalHeaderLabels(nomCols)
            #LLENO MI TABLA
            for c in range(cols):
                for f in range(rows):
                    self.tblDatos.setItem(f, c, QtWidgets.QTableWidgetItem("%s" % info[f][c]))
        else:
            self.msg("Hubo un error en la base de datos", 3,0)

    def retranslateUi(self, frmClientes):
        _translate = QtCore.QCoreApplication.translate
        frmClientes.setWindowTitle(_translate("frmClientes", "Cuarta GUI"))
        self.btnNuevo.setText(_translate("frmClientes", "Nuevo"))
        self.btnBorrar.setText(_translate("frmClientes", "Borrar"))
        self.btnActualizar.setText(_translate("frmClientes", "Actualizar"))
        self.gprRegistro.setTitle(_translate("frmClientes", "Guardar nuevo registro"))
        self.btnGuardar.setText(_translate("frmClientes", "Guardar"))
        self.lblPrimer.setText(_translate("frmClientes", "Apellido Paterno: "))
        self.lblTel.setText(_translate("frmClientes", "Telefono:"))
        self.lblSegundo.setText(_translate("frmClientes", "Apellido Materno:"))
        self.lblNombre.setText(_translate("frmClientes", "Nombre: "))
        self.lblCalle.setText(_translate("frmClientes", "Calle :"))
        self.lblCol.setText(_translate("frmClientes", "Colonia :"))
        self.lblNum.setText(_translate("frmClientes", "Numero Exterior:"))
        self.lblCP.setText(_translate("frmClientes", "Código Postal:"))
        self.lblSal.setText(_translate("frmClientes", "Salario :"))


class Cuarta(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        #OBJETO A LA CLASE Ui_frmTercera
        self.gui = Clientes()
        self.gui.setupUi(self)