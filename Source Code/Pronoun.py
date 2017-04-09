# -*- coding:utf-8 -*-
from Noun import NounFrame
try:
	import tkinter as tk
except ImportError:
	import Tkinter as tk

class PronounFrame(NounFrame):
	def __init__(self,master=None):
		NounFrame.__init__(master)
		self.voc_s.grid_forget()
		self.voc_p.grid_forget()
		self.voc_l.grid_forget()

def centerwindow(window,h,w):
	sh = window.winfo_screenheight()
	sw = window.winfo_screenwidth()
	window.geometry('+' + str((sw - w) // 2) + '+' + str((sh - h) // 2))

def getwinfo(widget):
	widget.update()
	print('height= %s, width= %s'% (widget.winfo_height(), widget.winfo_width()))

class Pronoun(tk.Frame):
	def __init__(self,master=None,window_widget=None):
		tk.Frame.__init__(self,master)
		self.window_widget=window_widget
		tk.Label(self,text='Personal Pronouns',font=('Times New Roman',16)).grid(row=0,columnspan=5)
		tk.Button(self,text='First Person',command=lambda : self.build('First Person Pronoun',('ego','meī','mihi','mē','mē','nōs','nostrum','nōbīs','nōs','nōbīs'))).grid(row=1,column=0)
		tk.Button(self,text='Second Person',command=lambda: self.build('Second Person Pronoun','tū,tuī,tibi,tē,tē,vōs,vestrum,vōbīs,vōs,vōbīs'.split(','))).grid(row=1,column=1)

	def build(self,title,answers):
		self.window_widget.withdraw()
		result_panel=tk.Toplevel()
		centerwindow(result_panel, 195, 370)
		tk.Label(result_panel,text=title,font=('Times New Roman',24,'bold')).pack()
		frame=PronounFrame(result_panel)
		frame.fill_in_the_answer(answers,(frame.nom_s, frame.gen_s, frame.dat_s, frame.acc_s, frame.abl_s, frame.nom_p,
		 frame.gen_p, frame.dat_p, frame.acc_p, frame.abl_p,))
		frame.pack()
		quit_protocol=lambda: (f for f in (self.window_widget.deiconify(), result_panel.destroy()))
		result_panel.wm_protocol('WM_DELETE_WINDOW',quit_protocol)
		tk.Button(result_panel, text='Back', command=quit_protocol).pack()

if __name__ == '__main__':
	root=tk.Tk()
	pronoun = Pronoun(root,root)
	pronoun.pack()
	root.attributes('-topmost', True)
	root.bind('<FocusIn>', lambda x: [f for f in (root.attributes('-topmost', False), root.unbind('<FocusIn'))])
	root.mainloop()





