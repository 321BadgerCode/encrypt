#badger
from tkinter import *

class input_box(Entry):
	place_holder:str=''
	place_holder_color:str=''
	default_fg_color:str=''

	def __init__(self,root=None,place_holder:str='',color:str="grey"):
		super().__init__(root)

		self.place_holder=place_holder
		self.place_holder_color=color
		self.default_fg_color=self["fg"]

		self.bind("<FocusIn>",self.set_focus_in)
		self.bind("<FocusOut>",self.set_focus_out)

		self.set_place_holder()
		
	def set_place_holder(self)->None:
		self.insert(0,self.place_holder)
		self["fg"]=self.place_holder_color

	def set_focus_in(self,*args)->None:
		if self["fg"]==self.place_holder_color:
			self.delete('0',"end")
			self["fg"]=self.default_fg_color

	def set_focus_out(self,*args)->None:
		if not self.get():
			self.set_place_holder()