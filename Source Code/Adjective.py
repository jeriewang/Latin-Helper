#!/usr/bin/env python
# -*- coding:utf-8 -*-
from Noun import NounFrame

try:
	import tkinter as tk
	import tkinter.ttk as ttk
except ImportError:
	import Tkinter as tk
	import ttk

def centerwindow(window,h,w):
	sh = window.winfo_screenheight()
	sw = window.winfo_screenwidth()
	window.geometry('+' + str((sw - w) // 2) + '+' + str((sh - h) // 2))

def getwinfo(widget):
	widget.update()
	print('height= %s, width= %s'% (widget.winfo_height(), widget.winfo_width()))


class AdjectiveFrame(NounFrame):
	def __init__(self,master=None,gender=''):
		super().__init__(master)
		tk.Label(self,text=gender,font=('Times New Romans',14,'bold')).grid(row=0,column=1,columnspan=2)


class AdjectiveAllGender(tk.Frame):
	def __init__(self,master=None):
		tk.Frame.__init__(self,master)
		self.masculine = AdjectiveFrame(self, 'masculine')
		self.femine = AdjectiveFrame(self, 'femine')
		self.neuter = AdjectiveFrame(self, 'neuter')
		self.masculine.grid(row=1, column=0)
		ttk.Separator(self).grid(row=1, column=1, sticky='ns')
		self.femine.grid(row=1, column=2, padx=20)
		ttk.Separator(self).grid(row=1, column=3, sticky='ns')
		self.neuter.grid(row=1, column=4, padx=20)

	def fill_in_the_answer(self,answers):
		"answers should be a 3 elements tuple or list, goes in order of (m),(s),(n)"
		self.masculine.fill_in_the_answer(answers[0])
		self.femine.fill_in_the_answer(answers[1])
		self.neuter.fill_in_the_answer(answers[2])


def suffix(stem, suffix):
	answer = []
	for e in suffix:
		answer.append(stem + e)
	return answer


class Adjective(tk.Frame):
	def __init__(self,master=None,window_widget=None):
		tk.Frame.__init__(self, master)
		self.window_widget=window_widget
		tk.Label(self,text='Please enter the dictionary form of a adjective.').pack()
		tk.Label(self, text='e.g. celeber, celebris, celebre').pack()
		tk.Label(self, text='However, if two or more parts are the same, they can be omitted.').pack()
		exframe1=tk.Frame(self)
		tk.Label(exframe1, text='e.g.').grid(column=0,row=0)
		exentry1 = tk.Entry(exframe1,width=len('brevis, breve'))
		exentry1.grid(column=1,row=0)
		exentry1.insert(0,'brevis, breve')
		exentry1.config(state='readonly')
		tk.Label(exframe1, text=' for brevis, brevis, breve,').grid(column=2,row=0)
		exframe1.pack()

		exframe2 = tk.Frame(self)
		tk.Label(exframe2, text='or').grid(column=0, row=0)
		exentry2 = tk.Entry(exframe2, width=len('sapiens'))
		exentry2.grid(column=1, row=0)
		exentry2.insert(0, 'sapiens')
		exentry2.config(state='readonly')
		tk.Label(exframe2, text='for sapiens, sapiens, sapiens').grid(column=2, row=0)
		exframe2.pack()

		entry=tk.Frame(self)
		self.entry=tk.Entry(entry,width=30)
		self.entry.bind('<Return>',self.build)
		self.entry.pack(side=tk.LEFT)
		self.entry.config(fg='gray')
		self.entry.insert(0,'This result might not be accurate!')
		self.entry.bind('<FocusIn>',lambda event: (f for f in (self.entry.delete(0,tk.END),self.entry.config(fg='black'),self.entry.unbind('<FocusIn>'))))
		tk.Button(entry,text='generate',command=self.build).pack(side=tk.RIGHT)
		entry.pack()
		self.positive_selection=tk.BooleanVar()
		self.positive_selection.set(1)
		self.superlative_selection = tk.BooleanVar()
		self.comparative_selection = tk.BooleanVar()
		sel=tk.Frame(self)
		tk.Checkbutton(sel,text='positive',variable=self.positive_selection).grid(column=0,row=0)
		tk.Checkbutton(sel, text='comparative', variable=self.comparative_selection).grid(column=1,row=0)
		tk.Checkbutton(sel, text='superlative', variable=self.superlative_selection).grid(column=2,row=0)
		sel.pack()

	def build(self,event=None):
		def first(nom):
			stem = nom[:-1]
			answer = suffix(stem, 'a ae ae am ā a ae arum is as is ae'.split())
			return answer

		def second(nom):
			if nom[-2:] == 'um':
				stem = nom[:-2]
				suf = 'um i o um o um a orum is a is a'.split()
			elif nom[-1] == 'r':
				stem = nom[:-1]
				suf = 'r i o um o r i orum is os is i'.split()
			elif nom[-3:] == 'ius':
				stem = nom[:-3]
				suf = ['us', 'i', 'o', 'um', 'o', '', 'i', 'orum', 'is', 'os', 'is', 'i']
			else:
				stem = nom[:-2]
				suf = 'us i o um o e i orum is os is i'.split()
			answer = suffix(stem, suf)
			if nom[-1] == 'r':
				answer[0] = answer[5] = nom
			return answer

		def third(nom, isistem, isneuter, base=None):
			stem = nom[:-2] if base is None else base
			if isneuter:
				if isistem:
					answer = suffix(stem, 'x is i x i x ia ium ibus ia ium ia'.split())
				else:
					answer = suffix(stem, 'x is i x e x a um ibus a ibus a'.split())
				answer[0] = answer[3] = answer[5] = nom
			else:
				if isistem:
					answer = suffix(stem, 'x is i em i x es um ibus es ibus es'.split())
				else:
					answer = suffix(stem, 'x is i em e x es um ibus es ibus es'.split())
				answer[0] = answer[5] = nom
				answer[7] = stem + 'ium' if isistem else stem + 'um'
			return answer

		def decide_declension(input_):
			if (input_[0][-2:] == 'us' or input_[0][-3:] == 'ius' or input_[0][-1] == 'r') and input_[1][-1] == 'a' and \
							input_[2][-2:] == 'um':
				answerp=[]
				answerc=[]
				answers=[]
				answerp.append(second(input_[0]))
				answerp.append(first(input_[1]))
				answerp.append(second(input_[2]))
				answerc.append(third(input_[1][:-1]+'ior',False,False,input_[1][:-1] + 'ior'))
				answerc.append(third(input_[1][:-1] + 'ior', False, False,input_[1][:-1] + 'ior'))
				answerc.append(third(input_[1][:-1] + 'ius', False, True,input_[1][:-1] + 'ior'))
				answers.append(second(input_[1][:-1]+'issimus' if input_[1][-2] != 'r' else input_[1][:-1]+'rimus'))
				answers.append(first(input_[1][:-1]+'issima' if input_[1][-2] != 'r' else input_[1][:-1]+'rima'))
				answers.append(second(input_[1][:-1]+'issimum' if input_[1][-2] != 'r' else input_[1][:-1]+'rimum'))
				self.positive.fill_in_the_answer(answerp)
				self.comparative.fill_in_the_answer(answerc)
				self.superlative.fill_in_the_answer(answers)
				return 'first & second declension'
			else: #third declension
				top=tk.Toplevel()
				centerwindow(top, 124, 466)
				def varify_blank():
					if manual_stem.get().replace(' ','') != '' or tmpbutton.get():
						top.destroy()
				tk.Label(top,text='The machine detected your input is a third declension adjective. Please').pack()
				tk.Label(top,text='provide the masculine positive genitive, or let the machine decide this.').pack()
				manual_stem=tk.StringVar()
				tk.Entry(top,textvariable=manual_stem).pack()
				tmpbutton=tk.BooleanVar()
				tk.Checkbutton(top,text='Let the machine decide it (very likely to be inaccurate and get weird result!)',variable=tmpbutton).pack()
				tk.Button(top,text='Continue',command=varify_blank).pack()
				top.wm_protocol('WM_DELETE_WINDOW',varify_blank)
				result_panel.withdraw()
				result_panel.wait_window(top)

				if not tmpbutton.get():
					stem = manual_stem.get()[:-2]
				else:
					if input_[0]==input_[1]==input_[2]:
						if input_[0][-2:]=='ox':
							stem=input_[0][:-1]+'c'
						elif input_[0][-2:] == 'ax':
							stem = input_[0][:-1] + 'c'
						elif input_[0][-2:]=='ix':
							stem = input_[0][-2:] +'ic'
						elif input_[0][-2:]=='ex':
							stem = input_[0][-2:] +'ic'
						elif input_[0][-1]=='s':
							stem=input_[0][:-1]+'t'
						else: stem=input_[0][:-2]
					elif input_[0]==input_[1]:
						stem = input_[1][:-2]
					else:
						stem = input_[1][:-2]

				answerp = []
				answerc = []
				answers = []
				answerp.append(third(input_[0], True, False, stem))
				answerp.append(third(input_[1], True, False, stem))
				answerp.append(third(input_[2], True, True, stem))
				answerc.append(third(stem + 'ior', False, False, input_[1][:-1] + 'ior'))
				answerc.append(third(stem + 'ior', False, False, input_[1][:-1] + 'ior'))
				answerc.append(third(stem + 'ius', False, True, input_[1][:-1] + 'ior'))
				answers.append(
						second(stem + 'issimus'))
				answers.append(
						first(stem + 'issima'))
				answers.append(
						second(stem + 'issimum'))
				self.positive.fill_in_the_answer(answerp)
				self.comparative.fill_in_the_answer(answerc)
				self.superlative.fill_in_the_answer(answers)

				result_panel.deiconify()
				return 'third declension'

		quit_protocol = lambda: (f for f in (self.window_widget.deiconify(), result_panel.destroy()))

		self.window_widget.withdraw()

		result_panel=tk.Toplevel()
		tmp=0
		for e in (self.positive_selection.get(),self.comparative_selection.get(),self.superlative_selection.get()):
			if e:
				tmp+=1
		if tmp==1: centerwindow(result_panel,324,1192)
		elif tmp==2: centerwindow(result_panel,583,1192)
		else: centerwindow(result_panel,842,1192)
		del tmp

		self.positive_frame = tk.Frame(result_panel)
		self.comparative_frame = tk.Frame(result_panel)
		self.superlative_frame = tk.Frame(result_panel)
		self.positive=AdjectiveAllGender(self.positive_frame)
		self.comparative=AdjectiveAllGender(self.comparative_frame)
		self.superlative=AdjectiveAllGender(self.superlative_frame)
		input_ = self.entry.get().replace(' ', '').split(',')
		if len(input_) == 0:
			quit_protocol()
			return 'break'
		elif len(input_)== 1:
			input_+=input_+input_
		elif len(input_) == 2:
			input_.insert(0,input_[0])
		try:
			declension = decide_declension(input_)
		except IndexError as err:
			print(err)
			quit_protocol()
			return 'break'
		tk.Label(result_panel, text='Declension of %s (%s)' % (self.entry.get(), declension),font=('Times New Romans', 24, 'bold')).pack()
		tk.Label(self.positive_frame,text='Positive',font=('Times New Romans',16,'bold')).pack(pady=10)
		self.positive.pack()
		tk.Label(self.comparative_frame, text='Comparative', font=('Times New Romans', 16, 'bold')).pack(pady=10)
		self.comparative.pack()
		tk.Label(self.superlative_frame, text='Superlative', font=('Times New Romans', 16, 'bold')).pack(pady=10)
		self.superlative.pack()


		if self.positive_selection.get():
			self.positive_frame.pack()
		if self.comparative_selection.get():
			self.comparative_frame.pack()
		if self.superlative_selection.get():
			self.superlative_frame.pack()
		tk.Button(result_panel, text='Back', command=quit_protocol).pack()

		result_panel.wm_protocol('WM_DELETE_WINDOW',quit_protocol)

if __name__ == '__main__':
	root=tk.Tk()
	adjective = Adjective(root,root)
	adjective.pack()
	root.attributes('-topmost', True)
	root.bind('<FocusIn>', lambda x: [f for f in (root.attributes('-topmost', False), root.unbind('<FocusIn'))])
	root.mainloop()
