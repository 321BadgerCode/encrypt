#badger
from tkinter import *

class label(Label):
	def __init__(self,root,text:str='',fg:str="#000000",bg:str="#ffffff",border_width:int=1,font=("tahoma","8","normal"),justify=LEFT,relief=SOLID):
		super().__init__(root,text=text,foreground=fg,background=bg,borderwidth=border_width,font=font,justify=justify,relief=relief)