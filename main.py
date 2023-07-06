#badger
from tkinter import *
from tkinter import messagebox
from os.path import exists
from encrypt import *
from input_box import *
from label import *
from random2 import *
from save import *
from tool_tip import *

def set_encrypt():
	global msg
	global key

	if exists(file_box.get()+".json")==False:
		r1:int=get_random_int(1,10)
		k1:int=get_linear_feedback_shift_register(r1)
		#k2:int=get_salt_hash(encrypt_box.get(),k1)
		key=k1
	else:
		key=int(set_load(file_box.get())["key"],2)

	"""b1:int=int(key_box.get())+key
	b2:str=str(b1)[0:1]+'.'+str(b1)[2::]
	msg=get_encrypt(encrypt_box.get(),round(float(b2)))"""
	msg=get_encrypt(encrypt_box.get(),int(key_box.get())+key)

#function to show message box with encrypted message
def set_show_message()->None:
	try:
		set_encrypt()
		#show message box with encrypted message
		messagebox.showinfo("encrypt message",msg)
		#set encrypt box input to decrypted message
		encrypt_box.delete(0,END)
		encrypt_box.insert(0,msg)
	except:
		messagebox.showerror("error","an error occured in the program!\n\npossible issues:\n1.key isn't an integer.\n2.key is too high.\n3.message had trouble encrypting(maybe due to certain unicode characters in message that aren't supported by encryption algorithm).")

def set_is_load_click()->None:
	try:
		data=set_load(file_box.get())

		encrypt_box.delete(0,END)
		encrypt_box.set_focus_in()
		encrypt_box.insert(0,data["msg"])
	except:
		messagebox.showerror("error","an error occured in the program!\n\npossible issues:\n1.file doesn't exist.\n2.file is corrupted.")

def set_is_encrypt_click()->None:
	set_show_message()

	if a.get()==1:
		set_save(file_box.get(),encrypt_box.get(),key)

def set_is_check()->None:
	if a.get()==0:
		file_box["state"]=DISABLED
	elif a.get()==1:
		file_box["state"]=NORMAL

#create window
win=Tk()
win.wm_title("encrypt")
win.geometry("250x200")
win.iconbitmap(".\\resource\\icon.ico")

#create info label
info_label=Label(win,text="program to encrypt and decrypt messages.")
info_label.pack(pady=20)

#create encrypt box
encrypt_box=input_box(win,"message(string)...")
encrypt_box.pack()

tool_tip(encrypt_box,"message to encrypt/decrypt.")

#create key box
key_box=input_box(win,"key(integer)...")
key_box.pack()

tool_tip(key_box,"# to use for encryption/decryption algorithm.")

#create check box
a=IntVar()

check_box=Checkbutton(win,text="text to file",variable=a,offvalue=0,onvalue=1,command=set_is_check)
check_box.pack()

tool_tip(check_box,"save encrypted message to file.")

#create file box
file_box=input_box(win,"file name(string)...")
file_box["state"]=DISABLED
file_box.pack()

tool_tip(file_box,"file name for file to save encrypted message to.")

#create button
load_button=Button(win,text="load file",command=set_is_load_click)
load_button.pack()
load_button.place(x=50,y=150)

tool_tip(load_button,"load encrypted message from file.")

#create button
encrypt_button=Button(win,text="encrypt/decrypt",command=set_is_encrypt_click)
encrypt_button.pack()
encrypt_button.place(x=120,y=150)

tool_tip(encrypt_button,"encrypt/decrypt message.")

#run window
win.mainloop()
#fix the label class and make compatible for tool_tip class