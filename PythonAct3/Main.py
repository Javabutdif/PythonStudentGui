
from tkinter import *


class Student:
	
	def __init__ (self):
		
		self.root = Tk()
		self.root.title('Genabio, Anton James')
		
		#Label Rows
		self.lb_idNo = Label(self.root, text="Id No: ")
		self.lb_idNo.grid(row=0,column=0)
		self.lb_FirstName = Label(self.root, text="First Name: ")
		self.lb_FirstName.grid(row=1,column=0)
		#TextBox Columns
		self.entry_idNo = Entry(self.root)
		self.entry_idNo.grid(row=0,column=1)
		self.entry_firstName = Entry(self.root)
		self.entry_firstName.grid(row=1,column=1)
		
		
		
		
		#Execution
		self.root.mainloop()


def main()->None:
	Student()



if __name__ == "__main__":
	main()