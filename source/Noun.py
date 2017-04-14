# -*- coding:utf-8 -*-
try:
	import tkinter as tk
except ImportError:
	import Tkinter as tk


def centerwindow(window,h,w):
	sh = window.winfo_screenheight()
	sw = window.winfo_screenwidth()
	window.geometry('+' + str((sw - w) // 2) + '+' + str((sh - h) // 2))


class Noun(tk.Frame):
	def __init__(self, master, window_widget):
		tk.Frame.__init__(self, master)
		self.window_widget=window_widget

		def countsyllables(word):
			count = 0
			vowels = 'aeiouy'
			if word[0] in vowels:
				count += 1
			for index in range(1, len(word)):
				if word[index] in vowels and word[index - 1] not in vowels:
					count += 1
			if word.endswith('e'):
				count -= 1
			if word.endswith('le'):
				count += 1
			if count == 0:
				count += 1
			return count


		idkmessage = tk.BooleanVar()
		idkmessage.set(False)

		def idk(selection):
			if not idkmessage.get():
				if selection == "I don't know":
					idkmessage.set(True)
					top = tk.Toplevel()
					top.title("")
					#top.overrideredirect(1)
					tk.Label(top, text="""
	If you choose not to provide the gender of the word, the most \n\
	possible gender according to your input will be used to produce the \n\
	result. However, the correctness of the result cannot be ensured. """).pack()
					tk.Button(top, text='I understand', command=lambda: top.destroy()).pack()
					centerwindow(top,98,462)

		def generate(display=True):

			display = display

			def inputerror(arg1=None, arg2=None, arg3=None, arg4=None, arg5=None):
				top = tk.Toplevel()
				top.wm_title('')
				tk.Label(top, text="Could not decline the word.").pack()
				tk.Label(top, text="Please make sure you put in the correct dictionary form.").pack()
				example = tk.Frame(top)
				tk.Label(example, text='for example:').grid(row=0, column=0)
				text = tk.Entry(example)
				text.insert(0, 'logarithmus, logarithmi')
				text.config(state='readonly')
				text.grid(row=0, column=1)
				temp = tk.StringVar()
				menu = tk.OptionMenu(example, temp, 'masculine', )
				temp.set('feminine')
				menu.config(width=8)
				menu.grid(row=0, column=2, sticky='ew')
				example.pack()
				#top.overrideredirect(1)
				top.title("")
				tk.Label(top, text='Please do not forget the comma in between').pack()
				tk.Button(top, text='ok', command=lambda: top.destroy()).pack()
				top.update()
				centerwindow(top,124,368)


			usr_input = self.data.get()
			gender = self.gender.get()

			def nodeclension(arg1=None, arg2=None, arg3=None, arg4=None, arg5=None):
				top = tk.Toplevel()
				top.wm_title('')
				#top.overrideredirect(1)
				tk.Label(top, text="Could not find the corresponding rule to decline the word.\n\
	Please check your input ").pack()
				tk.Button(top, text='Ok', command=lambda: top.destroy()).pack()
				centerwindow(top, 60, 380)
				top.update()



			try:
				assert gender != "gender"
			except AssertionError:
				top = tk.Toplevel()
				top.wm_title('')
				tk.Label(top, text="Please select a gender").pack()
				tk.Button(top, text='ok', command=lambda: top.destroy()).pack()
				centerwindow(top, 50, 152)
				return None

			def clearspace(usr_input):
				temp = ''
				for letter in usr_input:
					if letter != ' ':
						temp += letter
				return temp

			usr_input = clearspace(usr_input)

			def decide_declension(nom, gen):
				declension = 0
				if nom[-1] == 'a' and gen[-2:] == 'ae':
					declension = 1
				elif nom[-2:] == 'us' and gen[-2:] == 'us':
					declension = 4
				elif nom[-2:] == 'us' and gen[-1] == 'i':
					declension = 2
				elif nom[-2:] == 'um' and gen[-1] == 'i':
					declension = 2
				elif nom[-1] == 'r' and gen[-1] == 'i':
					declension = 2
				elif nom[-2:] == 'es' and gen[-2:] == 'ei':
					declension = 5
				elif nom[-1] == 'u' and gen[-2:] == 'us':
					declension = 4
				elif gen[-2:] == 'is':
					declension = 3
				return declension

			def suffix(stem, suffix):
				answer = []
				for e in suffix:
					answer.append(stem + e)
				return answer

			def first(nom, gen, gender):
				stem = gen[:-2]
				answer = suffix(stem, 'a ae ae am ā a ae arum is as is ae'.split())
				self.frame.fill_in_the_answer(answer)

			def second(nom, gen, gender):
				stem = gen[:-1]
				if nom[-2:] == 'um':
					suf = 'um i o um o um a orum is a is a'.split()
				elif nom[-1] == 'r':
					suf = 'r i o um o r i orum is os is i'.split()
				elif nom[-3:] == 'ius':
					suf = ['us', 'i', 'o', 'um', 'o', '', 'i', 'orum', 'is', 'os', 'is', 'i']
				else:
					suf = 'us i o um o e i orum is os is i'.split()
				answer = suffix(stem, suf)
				if nom[-1] == 'r':
					answer[0] = answer[5] = nom
				self.frame.fill_in_the_answer(answer)

			def third(nom, gen, gender):
				stem = gen[:-2]

				def isistem(nom, gen, gender, stem):
					vowels = 'aeiouy'
					if nom == 'canis':
						return False
					if gender == 'neuter':
						if nom[-1] == 'e' or nom[-2:] == 'al' or nom[-2:] == 'ar':
							return True
					elif (nom[-2:] == 'is' or nom[-2:] == 'es') \
							and countsyllables(nom) == countsyllables(gen):
						return True
					elif countsyllables(nom) == 1 and \
							(stem[-1] not in vowels and stem[-2] not in vowels) and \
							(nom[-1] == 's' or nom[-1] == 'x'):
						return True
					return False

				istem = isistem(nom, gen, gender, stem)
				if gender == 'neuter':
					if istem:
						answer = suffix(stem, 'x is i x e x ia ium ibus ia ium ia'.split())
					else:
						answer = suffix(stem, 'x is i x e x a um ibus a ibus a'.split())
					answer[0] = answer[3] = answer[5] = nom
				else:
					answer = suffix(stem, 'x is i em e x es um ibus es ibus es'.split())
					answer[0] = answer[5] = nom
					answer[7] = stem + 'ium' if istem else stem + 'um'
				self.frame.fill_in_the_answer(answer)

			def fourth(nom, gen, gender):
				if gender == 'neuter':
					stem = nom[:-1]
					answer = suffix(stem, 'u ūs u u u u ua uum ibus ua ibus ua'.split())
				else:
					stem = nom[:-2]
					answer = suffix(stem, 'us ūs ui um u us us uum ibus us ibus us'.split())
				self.frame.fill_in_the_answer(answer)

			def fifth(nom, gen, gender):
				stem = nom[:-2]
				answer = suffix(stem, 'es ei ei em e es es erum ebus es ebus es'.split())
				self.frame.fill_in_the_answer(answer)


			###call corresponding function###
			try:
				nom = usr_input.split(',')[0]
				gen = usr_input.split(',')[1]
			except IndexError:
				inputerror()
				return None

			self.declension = str(decide_declension(nom, gen))
			if self.declension == '0':
				nodeclension()
				return None

			self.action = {'1': ['first', first], '2': ['second', second], '3': ['third', third],
						   '4': ['fourth', fourth], '5': ['fifth', fifth]}


			# declension_feedback.config(text='This word belongs to '+action[declension][0]+' declension')
			if display:
				self.build()
				self.action[self.declension][1](nom, gen, gender)

		###interface###
		tk.Label(self, text="Please enter the dictionary form of the word").grid(row=0, columnspan=2)
		exframe=tk.Frame(self)
		tk.Label(exframe, text="e.g. ", ).grid(column=0, row=0)
		tk.Label(exframe, text="logarithmus, logarithmi",font='sf 14 italic').grid(column=1,row=0)
		tk.Label(exframe, text=", masculine", ).grid(column=2, row=0)
		exframe.grid(row=1, columnspan=2)
		self.data = tk.Entry(self)
		self.data.grid(row=2, column=0)
		tk.Button(self, text="Generate", command=generate).grid(row=3, column=0, columnspan=2, )
		self.gender = tk.StringVar()
		self.gender.set('gender')
		self.data.bind('<Return>', lambda x: generate())
		tk.OptionMenu(self, self.gender, 'masculine', 'feminine', 'neuter', "I don't know", command=idk).grid(row=2,
																											  column=1)


	def build(self):
		self.window_widget.withdraw()
		result_panel = tk.Toplevel()
		self.frame = NounFrame(result_panel)
		result_panel.title('')
		result_panel.wm_protocol('WM_DELETE_WINDOW',lambda: (f for f in (result_panel.destroy(),self.window_widget.deiconify())))
		tk.Label(result_panel, text='Declension of the word: ' + self.data.get() + ', ' + self.gender.get(),
				 font=('Times New Roman', 20, 'italic')).pack()

		self.frame.pack()

		tk.Label(result_panel, text='This word belongs to ' + self.action[self.declension][0] + ' declension',
				 font=('Times New Roman', 16)).pack()
		tk.Button(result_panel, text='Back', command=lambda: (f for f in (result_panel.destroy(),self.window_widget.deiconify()))).pack()
		centerwindow(result_panel,271,399)



class NounFrame(tk.Frame):
	def __init__(self,master=None):
		tk.Frame.__init__(self,master)
		tk.Label(self, text='singular').grid(row=1, column=1, )
		tk.Label(self, text='plural').grid(row=1, column=2, )
		answer_width = 15
		###left column###

		self.nom_l = tk.Label(self, text="nominative")
		self.nom_l.grid(row=2, column=0)
		self.gen_l = tk.Label(self, text="genitive")
		self.gen_l.grid(row=3, column=0)
		self.dat_l = tk.Label(self, text="dative")
		self.dat_l.grid(row=4, column=0)
		self.acc_l = tk.Label(self, text="accusative")
		self.acc_l.grid(row=5, column=0)
		self.abl_l = tk.Label(self, text="ablative")
		self.abl_l.grid(row=6, column=0)
		self.voc_l=tk.Label(self, text="vocative")
		self.voc_l.grid(row=7, column=0)

		###singular
		self.nom_s = tk.Entry(self, width=answer_width, state='readonly')
		self.nom_s.grid(row=2, column=1, )
		self.gen_s = tk.Entry(self, width=answer_width, state='readonly')
		self.gen_s.grid(row=3, column=1, )
		self.dat_s = tk.Entry(self, width=answer_width, state='readonly')
		self.dat_s.grid(row=4, column=1, )
		self.acc_s = tk.Entry(self, width=answer_width, state='readonly')
		self.acc_s.grid(row=5, column=1, )
		self.abl_s = tk.Entry(self, width=answer_width, state='readonly')
		self.abl_s.grid(row=6, column=1, )
		self.voc_s = tk.Entry(self, width=answer_width, state='readonly')
		self.voc_s.grid(row=7, column=1, )

		###plural###
		self.nom_p = tk.Entry(self, width=answer_width, state='readonly')
		self.nom_p.grid(row=2, column=2, )
		self.gen_p = tk.Entry(self, width=answer_width, state='readonly')
		self.gen_p.grid(row=3, column=2, )
		self.dat_p = tk.Entry(self, width=answer_width, state='readonly')
		self.dat_p.grid(row=4, column=2, )
		self.acc_p = tk.Entry(self, width=answer_width, state='readonly')
		self.acc_p.grid(row=5, column=2, )
		self.abl_p = tk.Entry(self, width=answer_width, state='readonly')
		self.abl_p.grid(row=6, column=2, )
		self.voc_p = tk.Entry(self, width=answer_width, state='readonly')
		self.voc_p.grid(row=7, column=2, )

	def fill_in_the_answer(self,answers,blanks_name=None):
		all_blanks=(self.nom_s, self.gen_s, self.dat_s, self.acc_s, self.abl_s, self.voc_s, self.nom_p,
		 self.gen_p, self.dat_p, self.acc_p, self.abl_p, self.voc_p) if blanks_name is None else blanks_name
		for blank, answer in zip(all_blanks,answers):
			blank.config(state=tk.NORMAL)
			blank.insert(0,answer)
			blank.config(state='readonly')



def get_declined(nom,gen,gender='m/f'):
	def countsyllables(word):
		count = 0
		vowels = 'aeiouy'
		if word[0] in vowels:
			count += 1
		for index in range(1, len(word)):
			if word[index] in vowels and word[index - 1] not in vowels:
				count += 1
		if word.endswith('e'):
			count -= 1
		if word.endswith('le'):
			count += 1
		if count == 0:
			count += 1
		return count

	def suffix(stem, suffix):
		answer = []
		for e in suffix:
			answer.append(stem + e)
		return answer

	def first(nom, gen, gender):
		stem = gen[:-2]
		answer = suffix(stem, 'a ae ae am ā a ae arum is as is ae'.split())
		return answer

	def second(nom, gen, gender):
		stem = gen[:-1]
		if nom[-2:] == 'um':
			suf = 'um i o um o um a orum is a is a'.split()
		elif nom[-1] == 'r':
			suf = 'r i o um o r i orum is os is i'.split()
		elif nom[-3:] == 'ius':
			suf = ['us', 'i', 'o', 'um', 'o', '', 'i', 'orum', 'is', 'os', 'is', 'i']
		else:
			suf = 'us i o um o e i orum is os is i'.split()
		answer = suffix(stem, suf)
		if nom[-1] == 'r':
			answer[0] = answer[5] = nom

		return answer

	def third(nom, gen, gender):
		stem = gen[:-2]

		def isistem(nom, gen, gender, stem):
			vowels = 'aeiouy'
			if nom == 'canis':
				return False
			if gender == 'neuter':
				if nom[-1] == 'e' or nom[-2:] == 'al' or nom[-2:] == 'ar':
					return True
			elif (nom[-2:] == 'is' or nom[-2:] == 'es') \
					and countsyllables(nom) == countsyllables(gen):
				return True
			elif countsyllables(nom) == 1 and \
					(stem[-1] not in vowels and stem[-2] not in vowels) and \
					(nom[-1] == 's' or nom[-1] == 'x'):
				return True
			return False

		istem = isistem(nom, gen, gender, stem)
		if gender == 'neuter':
			if istem:
				answer = suffix(stem, 'x is i x e x ia ium ibus ia ium ia'.split())
			else:
				answer = suffix(stem, 'x is i x e x a um ibus a ibus a'.split())
			answer[0] = answer[3] = answer[5] = nom
		else:
			answer = suffix(stem, 'x is i em e x es um ibus es ibus es'.split())
			answer[0] = answer[5] = nom
			answer[7] = stem + 'ium' if istem else stem + 'um'
		return answer

	def fourth(nom, gen, gender):
		if gender == 'neuter':
			stem = nom[:-1]
			answer = suffix(stem, 'u ūs u u u u ua uum ibus ua ibus ua'.split())
		else:
			stem = nom[:-2]
			answer = suffix(stem, 'us ūs ui um u us us uum ibus us ibus us'.split())

		return answer

	def fifth(nom, gen, gender):
		stem = nom[:-2]
		answer = suffix(stem, 'es ei ei em e es es erum ebus es ebus es'.split())

		return answer

	def decide_declension(nom, gen):
		declension = 0
		if nom[-1] == 'a' and gen[-2:] == 'ae':
			declension = first
		elif nom[-2:] == 'us' and gen[-2:] == 'us':
			declension = fourth
		elif nom[-2:] == 'us' and gen[-1] == 'i':
			declension = second
		elif nom[-2:] == 'um' and gen[-1] == 'i':
			declension = second
		elif nom[-1] == 'r' and gen[-1] == 'i':
			declension = second
		elif nom[-2:] == 'es' and gen[-2:] == 'ei':
			declension = fifth
		elif nom[-1] == 'u' and gen[-2:] == 'us':
			declension = fourth
		elif gen[-2:] == 'is':
			declension = third
		return declension

	return decide_declension(nom, gen)(nom, gen, gender)


if __name__ == '__main__':
	root = tk.Tk()
	noun = Noun(root,root)
	noun.pack()
	root.attributes('-topmost', True)
	root.bind('<FocusIn>', lambda x: [f for f in (root.attributes('-topmost', False), root.unbind('<FocusIn'))])
	root.mainloop()


