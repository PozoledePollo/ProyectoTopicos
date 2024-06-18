# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from primeraGUI import *
from segundaGUI import *
from terceraGUI import *
from Clientes import *
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(251, 108)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("imgs/ico/Free bsd.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 251, 21))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        self.menuGUI = QtWidgets.QMenu(self.menubar)
        self.menuGUI.setObjectName("menuGUI")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionSalir = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("imgs/png/16x16/Cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSalir.setIcon(icon1)
        self.actionSalir.setObjectName("actionSalir")
        self.actionPrimera = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("imgs/png/16x16/Bee.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPrimera.setIcon(icon2)
        self.actionPrimera.setObjectName("actionPrimera")
        self.actionSegunda = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("imgs/png/16x16/Bomb.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSegunda.setIcon(icon3)
        self.actionSegunda.setObjectName("actionSegunda")
        self.actionTercera = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("imgs/png/16x16/Blue key.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionTercera.setIcon(icon4)
        self.actionTercera.setObjectName("actionTercera")
        self.actionClientes = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("imgs/png/16x16/Alien.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClientes.setIcon(icon5)
        self.actionClientes.setObjectName("actionClientes")
        self.menuArchivo.addAction(self.actionSalir)
        self.menuGUI.addAction(self.actionPrimera)
        self.menuGUI.addAction(self.actionSegunda)
        self.menuGUI.addAction(self.actionTercera)
        self.menuGUI.addSeparator()
        self.menuGUI.addAction(self.actionClientes)
        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuGUI.menuAction())
        self.toolBar.addAction(self.actionPrimera)
        self.toolBar.addAction(self.actionSegunda)
        self.toolBar.addAction(self.actionTercera)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionClientes)
        #VINCULAR LAS ACCIONES  CON MIS INTERFACES GRAFICAS DE USUARIO
        self.actionPrimera.triggered.connect(self.primera)
        self.actionSegunda.triggered.connect(self.segunda)
        self.actionTercera.triggered.connect(self.tercera)
        self.actionClientes.triggered.connect(self.clientes)   
        self.actionSalir.triggered.connect(self.exit)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def exit(self):
        self.statusbar.showMessage("SALIR DE LA APLICACION")
        sys.exit(0)

    def primera(self):
        self.statusbar.showMessage("PRIMERA INTERFAZ")
        self.p = Primera()
        self.p.show()

    def segunda(self):
        self.statusbar.showMessage("SEGUNDA INTERFAZ")
        self.s = Segunda()
        self.s.show()

    def tercera(self):
        self.statusbar.showMessage("TERCERA INTERFAZ")
        self.t = Tercera()
        self.t.show()

    def clientes(self):
        self.statusbar.showMessage("CLIENTES INTERFAZ")
        self.c = Cuarta() 
        self.c.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuArchivo.setTitle(_translate("MainWindow", "Archivo"))
        self.menuGUI.setTitle(_translate("MainWindow", "GUI"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionSalir.setText(_translate("MainWindow", "Salir"))
        self.actionSalir.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionPrimera.setText(_translate("MainWindow", "Primera"))
        self.actionPrimera.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.actionSegunda.setText(_translate("MainWindow", "Segunda"))
        self.actionSegunda.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionTercera.setText(_translate("MainWindow", "Tercera"))
        self.actionTercera.setShortcut(_translate("MainWindow", "Ctrl+T"))
        self.actionClientes.setText(_translate("MainWindow", "Clientes"))
        self.actionClientes.setShortcut(_translate("MainWindow", "Ctrl+I"))

    
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
g = Ui_MainWindow()
g.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())
