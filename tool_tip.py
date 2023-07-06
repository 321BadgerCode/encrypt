#badger
from tkinter import *
from label import *

class tool_tip(object):
	def __init__(self,widget,text:str):
		self.widget=widget
		self.text=text
		self.tip_window=None
		self.id=None
		self.x=self.y=0

		self.set_create()

	def set_create(self):
		def set_enter(event):
			self.set_show()
		def set_leave(event):
			self.set_hide()
		self.widget.bind('<Enter>',set_enter)
		self.widget.bind('<Leave>',set_leave)

	def set_show(self):
		if self.tip_window or not self.text:
			return

		x,y,cx,cy=self.widget.bbox("insert")
		x=x+self.widget.winfo_rootx()+55
		y=y+cy+self.widget.winfo_rooty()+25
		self.tip_window=tw=Toplevel(self.widget)

		tw.wm_overrideredirect(1)
		tw.wm_geometry("+%d+%d"%(x,y))

		label2=Label(tw,text=self.text,justify=LEFT,background="#ffffff",relief=SOLID,borderwidth=1,font=("tahoma","8","normal"))
		label2.pack(ipadx=1)

	def set_hide(self):
		tw=self.tip_window
		self.tip_window=None
		if tw:
			tw.destroy()