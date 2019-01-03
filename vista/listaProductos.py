#=============
#IMPORTACIONES
#=============

# Importamos el módulo sys que provee el acceso a funciones y objetos mantenidos por el intérprete.
import sys
# Importamos las herramientas de PyQT que vamos a utilizar
from PyQt5 import QtWidgets, uic, QtGui
# Importamos los elementos que se encuentran dentro del diseñador
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QStackedWidget
# Importamos el modulo uic necesario para levantar un archivo .ui
from PyQt5 import uic
from vista import productos

#====================
#DEFINICION DE CLASES
#====================

#Creacion de la clase vistaLista
class ListaProductos(QtWidgets.QWidget):
	#Inicializacion del Objeto QWidget
	def __init__(self):
		QWidget.__init__(self)

		#Importamos la vista "listaAfiliados" y la alojamos dentro de la variable "vistaLista"
		self.listaProductos = uic.loadUi("ui/listaproductos.ui", self)
		self.nuevo.clicked.connect(self.seleccionarProductos)
	

	def seleccionarProductos(self):
		detalle_productos = productos.Productos()
		detalle_productos.show()