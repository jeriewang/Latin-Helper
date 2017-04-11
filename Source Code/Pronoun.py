# -*- coding:utf-8 -*-
from Noun import NounFrame
from Adjective import  AdjectiveAllGender
try:
	import tkinter as tk
except ImportError:
	import Tkinter as tk

class PronounFrame(NounFrame):
	def __init__(self,master=None):
		NounFrame.__init__(self,master)
		self.voc_s.grid_forget()
		self.voc_p.grid_forget()
		self.voc_l.grid_forget()

class PronounAllGender(AdjectiveAllGender):
	def __init__(self,master=None):
		AdjectiveAllGender.__init__(self,master)
		for e in (self.masculine,self.feminine,self.neuter):
			e.voc_s.grid_forget()
			e.voc_p.grid_forget()
			e.voc_l.grid_forget()


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
		tk.Button(self,text='Third Person',command=lambda : self.build('Third Person Pronoun',(('is eius ei eum eo ei eorum eis eos eis'.split()),('ea eius ei eam ea eae earum eis eas eis'.split()),('id eius ei id eo ea eorum eis ea eis'.split())),True)).grid(row=1,column=2)


	def build(self,title,answers,allgenders=False):
		self.window_widget.withdraw()
		result_panel=tk.Toplevel()

		tk.Label(result_panel,text=title,font=('Times New Roman',24,'bold')).pack()
		if allgenders:
			centerwindow(result_panel,247,1192)
			frame=PronounAllGender(result_panel)
			frame.masculine.fill_in_the_answer(answers[0],(frame.masculine.nom_s, frame.masculine.gen_s, frame.masculine.dat_s, frame.masculine.acc_s, frame.masculine.abl_s, frame.masculine.nom_p,
		 frame.masculine.gen_p, frame.masculine.dat_p, frame.masculine.acc_p, frame.masculine.abl_p,))
			frame.feminine.fill_in_the_answer(answers[1],(frame.feminine.nom_s, frame.feminine.gen_s, frame.feminine.dat_s, frame.feminine.acc_s, frame.feminine.abl_s, frame.feminine.nom_p,
		 frame.feminine.gen_p, frame.feminine.dat_p, frame.feminine.acc_p, frame.feminine.abl_p,))
			frame.neuter.fill_in_the_answer(answers[2],(frame.neuter.nom_s, frame.neuter.gen_s, frame.neuter.dat_s, frame.neuter.acc_s, frame.neuter.abl_s, frame.neuter.nom_p,
		 frame.neuter.gen_p, frame.neuter.dat_p, frame.neuter.acc_p, frame.neuter.abl_p,))
		else:
			centerwindow(result_panel, 195, 370)
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



