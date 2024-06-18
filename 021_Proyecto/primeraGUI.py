# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frmPrimera(object):
    def setupUi(self, frmPrimera):
        frmPrimera.setObjectName("frmPrimera")
        frmPrimera.resize(242, 135)
        
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("imgs/ico/Bee.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        frmPrimera.setWindowIcon(icon)    

        self.grpInfo = QtWidgets.QGroupBox(frmPrimera)
        self.grpInfo.setGeometry(QtCore.QRect(10, 10, 211, 111))
        self.grpInfo.setObjectName("grpInfo")
        self.widget = QtWidgets.QWidget(self.grpInfo)
        self.widget.setGeometry(QtCore.QRect(10, 30, 188, 51))
        self.widget.setObjectName("widget")
        self.lytInfo = QtWidgets.QFormLayout(self.widget)
        self.lytInfo.setContentsMargins(0, 0, 0, 0)
        self.lytInfo.setObjectName("lytInfo")
        self.lblNombre = QtWidgets.QLabel(self.widget)
        self.lblNombre.setObjectName("lblNombre")
        self.lytInfo.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lblNombre)
        self.edtNombre = QtWidgets.QLineEdit(self.widget)
        self.edtNombre.setObjectName("edtNombre")
        self.lytInfo.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.edtNombre)
        self.btnAceptar = QtWidgets.QPushButton(self.widget)
        self.btnAceptar.setObjectName("btnAceptar")
        self.lytInfo.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.btnAceptar)

        self.retranslateUi(frmPrimera)
        QtCore.QMetaObject.connectSlotsByName(frmPrimera)

    def retranslateUi(self, frmPrimera):
        _translate = QtCore.QCoreApplication.translate
        frmPrimera.setWindowTitle(_translate("frmPrimera", "GUI Primera"))
        self.grpInfo.setTitle(_translate("frmPrimera", "Información"))
        self.lblNombre.setText(_translate("frmPrimera", "Nombre:"))
        self.btnAceptar.setText(_translate("frmPrimera", "Aceptar"))

class Primera(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        #OBJETO A LA CLASE Ui_frmPrimera
        self.gui = Ui_frmPrimera()
        self.gui.setupUi(self)
        #VINCULAR EL PUSHBUTTON A UN EVENTO
        self.gui.btnAceptar.clicked.connect(self.aceptar)
    
    def aceptar(self):
        #RECUPERO LO QUE EL USUARIO ME PUSO EN EL EDIT
        txt = self.gui.edtNombre.text()
        #print(txt)
        msgbox = QtWidgets.QMessageBox()
        msgbox.setIcon(QtWidgets.QMessageBox.Information)
        msgbox.setText("Tu nombre es: \n\t"+txt)
        msgbox.setWindowTitle("Información")
        msgbox.exec()
