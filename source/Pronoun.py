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

class PronounFrameNoNom(PronounFrame):
	def __init__(self,master=None):
		PronounFrame.__init__(self,master)
		self.nom_s.grid_forget()
		self.nom_p.grid_forget()
		self.nom_l.grid_forget()

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

		tk.Label(self, text='Relative Pronouns', font=('Times New Roman', 16)).grid(row=2, columnspan=5)
		tk.Button(self,text='Relative Pronouns',command=lambda : self.build('Relative Pronouns',('qui cuius cui quem quō quī quorum quibus quōs quibus'.split(),
		                                                                                          'quae cuius cui quam qua quae quarum quibus quas quibus'.split(),'quod cuius cui quod quō quae quorum quibus quae quibus'.split()),True)).grid(row=3,column=1)
		tk.Label(self,text='Interrogative Pronouns',font=('Times New Roman', 16)).grid(row=4, columnspan=5)
		tk.Button(self,text='Interrogative Pronouns',command=lambda : self.build('Interrogative Prnouns',('quis cuius cui quem quo qui quorum quibus quos quibus'.split(),'quis cuius cui quem quo quae quorum quibus quas quibus'.split(),'quid cuius cui quid quo quae quorum quibus quae quibus'.split()),True)).grid(row=5,column=1)

		tk.Label(self, text='Indefinite Pronouns', font=('Times New Roman', 16)).grid(row=6, columnspan=5)
		tk.Button(self,text='Indefininite Pronouns',command=lambda :self.build('Indefinite Pronouns',('quidam,cuiusdam,cuidam,quendam,quodam,quidam,quorundam,quibusdam,quosdam,quibusdam'.split(','),'quaedam cuiusdam cuidam quandam quadam quaedam quarundam quibus quasdam quibusdam'.split(),'quoddam cuiusdam cuidam quoddam quodam quadam quorundam quibusdam quodam quibusdam'.split()),True)).grid(row=7,column=1)

		tk.Label(self, text='Intensive Pronouns', font=('Times New Roman', 16)).grid(row=8, columnspan=5)
		tk.Button(self,text='Intensive Pronouns',command=lambda : self.build('Intensive Pronouns',('ipse ipsius ipsi ipsum ipso ipsi ipsorum ipsis ipsos ipsis'.split(),'ipsa ipsius ipsi ipsam ipsa ipsae ipsarum ipsis ipsas ipsis'.split(),'ipsum ipsius ipsi ipsum ipso ipsa ipsorum ipsis ipsa ipsis'.split()),True)).grid(row=9,column=1)

		tk.Label(self, text='Reflexive Pronouns', font=('Times New Roman', 16)).grid(row=10, columnspan=5)
		tk.Button(self, text='First Person', command=lambda: self.build_no_nom('First Person Pronoun', (
		'meī', 'mihi', 'mē', 'mē', 'nostri', 'nōbīs', 'nōs', 'nōbīs'))).grid(row=11, column=0)
		tk.Button(self, text='Second Person', command=lambda: self.build_no_nom('Second Person Pronoun',
		                                                                 'tuī,tibi,tē,tē,vestri,vōbīs,vōs,vōbīs'.split(
			                                                                 ','))).grid(row=11, column=1)
		tk.Button(self, text='Third Person', command=lambda: self.build_no_nom('Third Person Pronoun',('sui sibi se se sui sibi se se'.split()))).grid(row=11, column=2)
		tk.Label(self, text='Demonstrative Pronouns', font=('Times New Roman', 16)).grid(row=12, columnspan=5)
		tk.Button(self,text='hic, haec, hoc',font=('Sans-serif',12,'italic'),command=lambda: self.build('hic, haec, hoc: this, these',('his huius huic hunc hoc hi horum his hos his'.split(),'haec huius huic hanc haec hae harum his has his'.split(),'hoc huius huic hoc hoc haec horum his haec his'.split()),True)).grid(row=13,column=0)
		tk.Button(self,text='ille, illa, illud',font=('Sans-serif',12,'italic'),command=lambda: self.build('ille, illa, illud: that, those',('ille illius illi illum illo illi illorum illis illos illis'.split(),'illa illius illi illam illa illae illarum illis illas illis'.split(),'illud illius illi illud illo illa illorum illis illa illis'.split()),True)).grid(row=13,column=1)
		tk.Button(self,text='iste ista istud',font=('Sans-serif',12,'italic'),command=lambda: self.build('that, such',('iste istius isti istum isto isti istroum istis istos istis'.split(),'ista istuis isti istam ista istae istarum istis istas istis'.split(),'istud istius isti istud isto ista istorum istis ista istis'.split()),True)).grid(row=13,column=2)
		tk.Button(self,text='idem, eadem, idem',font=('Sans-serif',12,'italic'),command=lambda: self.build('the same',('idem eiusdem eidem eundem eodem eidem eorundem eisdem eosdem eisdem'.split(),'eadem eiusdem eidem eandem eadem eaedem earundem eisdem easdem eisdem'.split(),'idem eiusdem eidem idem eodem eadem eorundem eisdem eadem eisdem'.split()),True)).grid(row=14,column=0)


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

	def build_no_nom(self,title,answers):
		result_panel = tk.Toplevel()
		tk.Label(result_panel, text=title, font=('Times New Roman', 24, 'bold')).pack()
		#centerwindow()
		frame = PronounFrameNoNom(result_panel)
		frame.fill_in_the_answer(answers, ( frame.gen_s, frame.dat_s, frame.acc_s, frame.abl_s,
		                                   frame.gen_p, frame.dat_p, frame.acc_p, frame.abl_p,))
		frame.pack()
		quit_protocol = lambda: (f for f in (self.window_widget.deiconify(), result_panel.destroy()))
		result_panel.wm_protocol('WM_DELETE_WINDOW', quit_protocol)
		tk.Button(result_panel, text='Back', command=quit_protocol).pack()

if __name__ == '__main__':
	root=tk.Tk()
	pronoun = Pronoun(root,root)
	pronoun.pack()
	root.attributes('-topmost', True)
	root.bind('<FocusIn>', lambda x: [f for f in (root.attributes('-topmost', False), root.unbind('<FocusIn'))])
	root.mainloop()



