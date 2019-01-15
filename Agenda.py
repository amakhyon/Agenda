import sys
import random
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import *

class Window(QWidget):
	def __init__(self):
		
		super().__init__()
		self.createLayout()
		self.LayoutPosition()
		self.show()



	def createLayout(self):
		self.counter = 0
		self.setWindowTitle('Agenda')
		self.setGeometry(950,100,500,500)
		self.mainLayout = QHBoxLayout()
		self.centerLayout = QVBoxLayout()
		self.dailyTasks_label = QLabel('Tasks')
		self.dailyTasks_label.setFont(QtGui.QFont('Sanserif',20))
		self.addTask_lineEdit = QLineEdit('add task')
		self.addTask_lineEdit.returnPressed.connect(self.typed)
		self.encourage_label = QLabel(self)
		self.groupBox = QGroupBox('Tasks')
		self.tasksHbox = QHBoxLayout()
		self.leftLayout = QVBoxLayout()
		self.quotes = ['It doesn’t matter how slow you go as long as you don’t stop','And you ask ‘What if I fall?’ Oh but my darling, what if you fly?',
		'Fall seven times, stand up eight','It is not the mountain we conquer but ourselves','Trust yourself. You know more than you think you do','Screw it, let’s do it',
		'Keep going. Be all in','If you want it, work for it','You can if you think you can','Do it with passion or not at all.','At the end of hardship comes happiness.']
		

	def LayoutPosition(self):
		self.groupBox.setLayout(self.leftLayout)
		self.centerLayout.addWidget(self.dailyTasks_label)
		self.centerLayout.addWidget(self.addTask_lineEdit)
		self.centerLayout.addWidget(self.encourage_label)
		#self.mainLayout.addStretch(1)
		self.mainLayout.addLayout(self.centerLayout)
		self.mainLayout.addWidget(self.groupBox)
		self.setLayout(self.mainLayout)


	def typed(self):
		
		label = QLabel(self.addTask_lineEdit.text())
		self.addTask_lineEdit.setText('')
		btn = QPushButton(self)
		btn.setIcon(QtGui.QIcon('close.png'))
		btn.clicked.connect(lambda: self.remove(hbox,label,btn))
		hbox = QHBoxLayout()
		hbox.addWidget(label)
		hbox.addWidget(btn)
		self.leftLayout.addLayout(hbox)
		
		print('yes')
		

	def remove(self,hbox,label,btn):
		index = random.randint(0,len(self.quotes)-1)
		self.encourage_label.setText(self.quotes[index])
		label.hide()
		btn.hide()
		


app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec())
