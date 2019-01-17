#this program was written by Assem Makhyon and is free for all 

import os
import sys
import random
import subprocess
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
		self.dailyTasks_label = QLabel('                     Agenda')
		self.dailyTasks_label.setFont(QtGui.QFont('Sanserif',20))
		self.addTask_lineEdit = QLineEdit('add task')
		self.addTask_lineEdit.returnPressed.connect(self.add_task)
		self.encourage_label = QLabel(self)
		self.groupBox = QGroupBox('Tasks')
		self.tasksHbox = QHBoxLayout()
		self.rightLayout = QVBoxLayout()
		self.quotes = self.set_qoutes()
		self.get_tasks_directory_btn = QPushButton('get tasks from directory',self)
		self.get_tasks_file_btn = QPushButton('get tasks from file',self)
		self.get_tasks_file_btn.clicked.connect(self.import_tasks_file)
		self.get_tasks_directory_btn.clicked.connect(self.import_tasks)
		self.clear_all_btn = QPushButton('clear all')
		self.clear_all_btn.clicked.connect(self.clear_all)
		self.btn_container = QHBoxLayout()

		

	def LayoutPosition(self):
		self.groupBox.setLayout(self.rightLayout)
		self.centerLayout.addWidget(self.dailyTasks_label)
		self.centerLayout.addWidget(self.addTask_lineEdit)
		self.btn_container.addWidget(self.get_tasks_directory_btn)
		self.btn_container.addWidget(self.get_tasks_file_btn)
		self.btn_container.addWidget(self.clear_all_btn)
		self.centerLayout.addLayout(self.btn_container)
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
		self.add_to_file(label.text())

	def add_to_file(self,task):
		duplicate = False
		if os.path.isfile('tasks.txt'):
			file = open('tasks.txt','r')
			lines = file.readlines()
			file.close()
			for line in lines:
				if line==task:
					duplicate = True
		if not duplicate:
			file = open('tasks.txt','a')
			file.write(task + '\n')
			print('wrote' + task + ' to file')
			file.close()
		

	def remove(self,label,btn):
		self.remove_from_file(label.text())
		index = random.randint(0,len(self.quotes)-1)
		self.encourage_label.setText(self.quotes[index])
		print(label.text())
		label.hide()
		btn.hide()

	def remove_from_file(self,task):
		if os.path.isfile('tasks.txt'):
			file = open('tasks.txt','r')
			lines = file.readlines()
			file.close()
			file = open('tasks.txt','w')
			for line in lines:
				if line!=task :
					print('task: ' + task + '--line: ' + line)
					file.write(line)
			file.close()
				
	

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
			file.close()
			return quotes
		else:
			quotes = ['Every moment is a fresh beginning. – T.S Eliot','Yesterday you said tomorrow. Just do it. – Nike','All limitations are self-imposed. – Oliver Wendell Holmes']
			return quotes

	def import_tasks_file(self):
		tasks = self.get_tasks()
		for task in tasks:
			if task != '\n':
				self.addTask_lineEdit.setText(task)
				self.add_task()

	def get_tasks(self):
		if os.path.isfile('tasks.txt'):
			with open('tasks.txt','r') as file:
				tasks = []
				for line in file:
					tasks.append(line)
			file.close()
			return tasks
	def clear_all(self):
		subprocess.Popen(['python', 'agenda.py'])
		sys.exit()





app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec())
