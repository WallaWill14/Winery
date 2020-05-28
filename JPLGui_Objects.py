# 
#     _   _____   _____ ___           ______  __ 
#    / | / /   | / ___//   |         / / __ \/ / 
#   /  |/ / /| | \__ \/ /| |    __  / / /_/ / /  
#  / /|  / ___ |___/ / ___ |   / /_/ / ____/ /___
# /_/ |_/_/  |_/____/_/  |_|   \____/_/   /_____/
#
# JPLGui_Objects.py
#
# Collection of PyQt5 wrapper classes that are used in JPLGui_Engine.py
# Each PyQt widget will have its own JPLGui object class
#
# Dependencies
from PyQt5 import QtWidgets, QtCore, QtGui
import pyqtgraph as pg
import pyqt_led

###############################################################################################################

class JPLButton(QtWidgets.QPushButton):
	""" Class used to create a normal Qt push button """
	def __init__(self, parent, id, callback, dim, label):
		# Call parent constructor
		super().__init__(label,parent)

		self.id = id
		self.dim = dim
		self.label = label
		self.red = False

		# Connect callback to button click
		if callback:
			self.clicked.connect(callback)

		# Otherwise, create a toggle button
		else:
			self.enabled = False
			self.clicked.connect(self.toggle)

		# Default size
		self.setFixedWidth(120)


	def toggle(self):
		""" Function makes PyQt Button work as a toggle switch instead. Will simply 
		return true when enabled and false when disabled. Will turn a neon green
		when enabled. Non callback function will execute.
		"""
		# Flip bool value each time its switched
		self.enabled = not self.enabled

		if self.enabled:
			if not self.red:
				self.setStyleSheet('background-color:rgb(57,255,20)' ';color:black')
			else:
				self.setStyleSheet('background-color:rgb(255,0,0)' ';color:black')
		else:
			self.setStyleSheet('')


	def value(self):
		""" Returns true if toggle is enabled """
		try:
			return self.enabled
		except :
			raise TypeError('JPLButton has no return type.')


class JPLLED(pyqt_led.Led):
	""" Class used to create a PyQt LED """
	def __init__(self, parent, id, dim, label, color, shape):
		# Call parent constructor
		super().__init__(parent, on_color=color, shape=shape)

		self.id = id
		self.dim = dim
		self.label = label


		# Default size
		self.setFixedSize(35,35)


	def toggleOn(self):
		""" Toggle LED on """
		self._toggle_on()


	def toggleOff(self):
		""" Toggle LED off """
		self._toggle_off()

	def value(self):
		""" Returns true if on """
		if self.is_on():
			return True
		else:
			return False


class JPLCheckBox(QtWidgets.QCheckBox):
	""" Class used to create a normal Qt push button """
	def __init__(self, parent, id, dim, label):
		# Call parent constructor
		super().__init__(label, parent)

		self.id = id
		self.dim = dim
		self.label = label


		# Default size
		self.setFixedWidth(120)


	def value(self):
		""" Returns True if checked otherwise false """
		return self.isChecked()


class JPLRadioButton(QtWidgets.QRadioButton):
	""" Class used to create a normal Qt push button """
	def __init__(self, parent, id, label):
		# Call parent constructor
		super().__init__(label, parent)

		self.id = id
		self.dim = [1,1]
		self.label = label


		# Disables default state that only allows one radio button to be checked
		self.setAutoExclusive(False)


	def value(self):
		""" Returns True if checked otherwise false """
		return self.isChecked()


class JPLIndicator(QtWidgets.QLineEdit):
	""" Class used to create a normal Qt push button """
	def __init__(self, parent, id, default, dim, label):
		# Call parent constructor
		super().__init__(parent)

		self.id = id
		self.dim = dim
		self.label = label


		# Set defaut readout
		self.setText(default)

		# Users do not have permission to alter indicators
		self.setReadOnly(True)
		self.setStyleSheet('background-color:rgb(103, 111, 112)' ';color:white')
		self.setFixedWidth(120)
		self.setSizePolicy(QtWidgets.QSizePolicy.Fixed,QtWidgets.QSizePolicy.Fixed)



class JPLUserInput(QtWidgets.QLineEdit):
	""" Class used to create a normal Qt push button """
	def __init__(self, parent, id, default, dim, label):
		# Call parent constructor
		super().__init__(parent)

		self.id = id
		self.dim = dim
		self.label = label


		if default: self.setText(default)
		self.setFixedWidth(120)
		self.setSizePolicy(QtWidgets.QSizePolicy.Fixed,QtWidgets.QSizePolicy.Fixed)


	def value(self):
		""" Returns a string with user input """
		return self.text()


class JPLTextBox(QtWidgets.QTextEdit):
	""" Class used to create a normal Qt push button """
	def __init__(self, parent, id, default, dim, label):
		# Call parent constructor
		super().__init__(parent)

		self.id = id
		self.dim = [1,1]
		self.label = label


		if default: self.setText(default)


class JPLSpinBox(QtWidgets.QDoubleSpinBox):
	""" Class used to create a normal Qt push button """
	def __init__(self, parent, id, default, dim, label):
		# Call parent constructor
		super().__init__(parent)

		self.id = id
		self.dim = dim
		self.label = label


		self.setFixedWidth(120)

		self.setDecimals(2)
		self.setSingleStep(1)
		self.setRange(0,50)
		self.setValue(default)


class JPLSlider(QtWidgets.QSlider):
	""" Class used to create a normal Qt push button """
	def __init__(self, parent, id, default, dim, label):
		# Call parent constructor
		self.id = id
		self.dim = [1,1]
		self.label = label



	def value(self):
		""" Returns the current value the slider is set to """
		return self.value()


class JPLComboBox(QtWidgets.QComboBox):
	""" Class used to create a normal Qt push button """
	def __init__(self, parent, id, items, dim, label):
		# Call parent constructor
		super().__init__(parent)

		self.id = id
		self.dim = dim
		self.label = label


		for item in items:
			self.addItem(item)

		self.setFixedWidth(120)



	def value(self):
		""" Returns the string of the item that is currently selected """
		return self.currentText()
			
class JPLLoggingBox(QtWidgets.QTextBrowser):
	""" Class used to create a box which logs actions in real time """
	def __init__(self, parent, label, dim, id=None):
		# Call parent constructor
		super().__init__(parent)
		# Labels do not require an ID
		self.dim = dim
		self.id = id
		self.label = label

		self.setFixedWidth(200)


class JPLLabel(QtWidgets.QLabel):
	""" Class used to create a normal Qt push button """
	def __init__(self, parent, label, dim, id=None):
		# Call parent constructor
		super().__init__(parent)
		# Labels do not require an ID
		self.dim = dim
		self.id = id
		self.label = label


		self.setText(label)


class JPLFileDialog(QtWidgets.QFileDialog):
	""" Class used to create a normal Qt push button """
	def __init__(self, parent, id, dim, label):
		# Call parent constructor
		super().__init__(parent)


class JPLImage(QtWidgets.QLabel):
	""" Class used to create a normal Qt push button """
	def __init__(self, parent, id, image):
		# Call parent constructor
		super().__init__(parent)
		# Labels do not require an ID
		self.id = id
		self.dim = [1,1]

		self.setPixmap(QtGui.QPixmap(image).scaled(100, 100, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation))
		self.setFixedSize(100,100)


class JPLPlot(pg.GraphicsLayoutWidget):
	""" Class used to create a normal Qt push button """
	def __init__(self, parent, id, numCurves, labels):
		# Call parent constructor
		super().__init__(parent)

		self.id = id
		self.dim = [4,4]
		# List that holds curves in a plot
		self.curves = []

		# Available colors for plot (up to 8 colors)
		colors = ['w','b','g','r','c','m','y','w']

		# Create plot object
		self.axe = self.addPlot()

		# Create a list to contain all curves
		for curve in range(0,numCurves):
			self.curves.append(self.axe.plot(pen=colors[curve]))

		# Set title and axis labels
		self.axe.setTitle(labels[0])
		self.axe.setLabel('bottom',labels[1])
		self.axe.setLabel('left',labels[2])

		# Set Fixed Size 
		self.setFixedSize(350,350)


	def updatePlot(self, x, *y):
		""" Update Plot Object. Will take up to "n" number of arguments.
		Will plot as many items specified against one x axis only
		"""
		for index,_y in enumerate(y):
			self.curves[index].setData(x,_y)
		

class JPLStackPlot(pg.GraphicsLayoutWidget):

	def __init__():
		# Call parent constructor
		# Set dim and id
		pass


class JPLDivies():
	""" Class used to create a normal Qt push button """
	def __init__(self, type, size=None, name=None):

		self.type = type
		self.size = size
		self.name = name


def showDialog(title, message, icontype):
	""" """
	if isinstance(icontype,str):
		if icontype.lower() == 'critical':
			icontype = 3
		elif icontype.lower() == 'warning':
			icontype = 2
		elif icontype.lower() == 'information':
			icontype = 1

	msgBox = QtWidgets.QMessageBox()
	msgBox.setIcon(icontype)
	msgBox.setText(message)
	msgBox.setFixedWidth(300)
	msgBox.setWindowTitle(title)
	msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
	msgBox.setWindowModality(True)
	#msgBox.buttonClicked.connect(msgButtonClick)

	returnValue = msgBox.exec()
	if returnValue == QtWidgets.QMessageBox.Ok:
		msgBox.close()