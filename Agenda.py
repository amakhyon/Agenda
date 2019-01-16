import os
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
		self.addTask_lineEdit.returnPressed.connect(self.add_task)
		self.encourage_label = QLabel(self)
		self.groupBox = QGroupBox('Tasks')
		self.tasksHbox = QHBoxLayout()
		self.rightLayout = QVBoxLayout()
		self.quotes = self.set_qoutes()
		self.get_tasks_btn = QPushButton('get tasks',self)
		self.get_tasks_btn.clicked.connect(self.import_tasks)

		

	def LayoutPosition(self):
		self.groupBox.setLayout(self.rightLayout)
		self.centerLayout.addWidget(self.dailyTasks_label)
		self.centerLayout.addWidget(self.addTask_lineEdit)
		self.centerLayout.addWidget(self.get_tasks_btn)
		self.centerLayout.addWidget(self.encourage_label)
		self.mainLayout.addLayout(self.centerLayout)
		self.mainLayout.addWidget(self.groupBox)
		self.setLayout(self.mainLayout)


	def add_task(self):
		
		label = QLabel(self.addTask_lineEdit.text())
		self.addTask_lineEdit.setText('')
		btn = QPushButton(self)
		btn.setIcon(QtGui.QIcon('close.png'))
		btn.clicked.connect(lambda: self.remove(label,btn))
		hbox = QHBoxLayout()
		hbox.addWidget(label)
		hbox.addWidget(btn)
		self.rightLayout.addLayout(hbox)
		print('yes')
		

	def remove(self,label,btn):
		index = random.randint(0,len(self.quotes)-1)
		self.encourage_label.setText(self.quotes[index])
		print(label.text())
		label.hide()
		btn.hide()

	def import_tasks(self):
		for file in os.listdir():
			if os.path.isfile(file):
				self.addTask_lineEdit.setText(file)
				self.add_task()
	def set_qoutes(self):
		if os.path.isfile('quotes.txt'):
			with open('quotes.txt','r') as file:
				quotes = []
				for line in file:
					quotes.append(line)
			print(quotes)
			return quotes



app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec())
