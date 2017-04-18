# -*- coding:utf-8 -*-
try:
	import tkinter as tk
except ImportError:
	import Tkinter as tk



def centerwindow(window,h,w):
	sh = window.winfo_screenheight()
	sw = window.winfo_screenwidth()
	window.geometry('+' + str((sw - w) // 2) + '+' + str((sh - h) // 2))

class Verb(tk.Frame):
	def __init__(self,master,window_widget):
		"""the window widget should be either a Tk or a Toplevel holding Verb for calling window_widget.withdraw later in the code"""
		endings_indicative={'active':{'1':{'present':['o','as','at','amus','atis','ant'],
		                        'imperfect':['abam','abas','abat','abamus','abatis','abant'],
		                        'future':['abo','abis','abit','abimus','abitis','abunt'],
		                        'perfect':['i','isti','it','imus','istis','erunt'],
		                        'pluperfect':['eram','eras','erat','eramus','eratis','erant'],
		                        'future perfect':['ero','eris','erit','erimus','eritis','erint']},
		                   '2':{'present':['eo','es','et','emus','etis','ent'],
		                        'imperfect':['ebam','ebas','ebat','ebamus','ebatis','ebant'],
		                        'future':['ebo','ebis','ebit','ebimus','ebitis','ebunt'],
		                        'perfect':['i','isti','it','imus','istis','erunt'],
		                        'pluperfect':['eram','eras','erat','eramus','eratis','erant'],
		                        'future perfect':['ero','eris','erit','erimus','eritis','erint']},
		                   '3':{'present':['o','is','it','imus','itis','unt'],
		                        'imperfect':['ebam','ebas','ebat','ebamus','ebatis','ebant'],
		                        'future':['am','es','et','emus','etis','ent'],
		                        'perfect':['i','isti','it','imus','istis','erunt'],
		                        'pluperfect':['eram','eras','erat','eramus','eratis','erant'],
		                        'future perfect':['ero','eris','erit','erimus','eritis','erint']},
		                   '3io':{'present':['io','is','it','imus','itis','iunt'],
		                        'imperfect':['iebam','iebas','iebat','iebamus','iebatis','iebant'],
		                        'future':['iam','ies','iet','iemus','ietis','ient'],
		                        'perfect':['i','isti','it','imus','istis','erunt'],
		                        'pluperfect':['eram','eras','erat','eramus','eratis','erant'],
		                        'future perfect':['ero','eris','erit','erimus','eritis','erint']},
		                   '4':{'present':['io','is','it','imus','itis','iunt'],
		                        'imperfect':['iebam','iebas','iebat','iebamus','iebatis','iebant'],
		                        'future':['am','es','et','emus','etis','ent'],
		                        'perfect':['i','isti','it','imus','istis','erunt'],
		                        'pluperfect':['eram','eras','erat','eramus','eratis','erant'],
		                        'future perfect':['ero','eris','erit','erimus','eritis','erint']}},
		         'passive':{'1':{'present':['or','aris','atur','amur','amini','antur'],
		                         'imperfect':['abar','abaris','abatur','abamur','abamini','abantur'],
		                         'future':['abor','aberis','abitur','abimur','abimini','abuntur'],
		                         'perfect':[' sum',' es',' est',' sumus',' estis',' sunt'],
		                         'pluperfect':[' eram',' eras',' erat', ' eramus',' eratis',' erant'],
		                         'future perfect':[' ero',' eris',' erit',' erimus',' eritis',' erunt']},
		                    '2':{'present':['eor','eris','etur','ebur','emini','entur'],
		                         'imperfect':['ebar','ebaris','ebatur','ebamur','ebamini','ebantur'],
		                         'future':['ebor','eberis','ebitur','ebimur','ebimini','ebuntur'],
		                         'perfect':[' sum',' es',' est',' sumus',' estis',' sunt'],
		                         'pluperfect':[' eram',' eras',' erat', ' eramus',' eratis',' erant'],
		                         'future perfect':[' ero',' eris',' erit',' erimus',' eritis',' erunt']},
		                    '3':{'present':['or','eris','itur','imur','imini','untur'],
		                         'imperfect':['ebar','ebaris','ebatur','ebamur','ebamini','ebantur'],
		                         'future':['ar','eris','etur','emur','emini','entur'],
		                         'perfect':[' sum',' es',' est',' sumus',' estis',' sunt'],
		                         'pluperfect':[' eram',' eras',' erat', ' eramus',' eratis',' erant'],
		                         'future perfect':[' ero',' eris',' erit',' erimus',' eritis',' erunt']},
		                    '3io':{'present':['ior','ieris','itur','imur','imini','iuntur'],
		                           'imperfect':['iebar','iebaris','iebatur','iebamur','iebamini','iebantur'],
		                           'future':['iar','ieris','ietur','iemur','iemini','ientur'],
		                           'perfect':[' sum',' es',' est',' sumus',' estis',' sunt'],
		                           'pluperfect':[' eram',' eras',' erat', ' eramus',' eratis',' erant'],
		                           'future perfect':[' ero',' eris',' erit',' erimus',' eritis',' erunt']},
		                    '4':{'present':['ior','ieris','itur','imur','imini','iuntur'],
		                         'imperfect':['iebar','iebaris','iebatur','iebamur','iebamini','iebantur'],
		                         'future':['iar','ieris','ietur','iemur','iemini','ientur'],
		                         'perfect':[' sum',' es',' est',' sumus',' estis',' sunt'],
		                         'pluperfect':[' eram',' eras',' erat', ' eramus',' eratis',' erant'],
		                         'future perfect':[' ero',' eris',' erit',' erimus',' eritis',' erunt']}}}

		endings_subjunctive={'active': {
					   '1': {'present': ['em','es','et','emus','etis','ent'],
			                 'imperfect': ['arem','ares','aret','aremust','aretis','arent'],
			                 'future':[],
			                 'perfect': ['averim','averis','averit','averimus','averitis','averint'],
			                 'pluperfect': ['avissem','avisses','avisset','avissemus','avissetis','avissent'],
					         'future perfect':['','','','','','']},
			           '2': {'present': ['eam','eas','eat','eamus','eatis','eant'],
			                 'imperfect': ['erem','eres','emaret','eremus','eretis','erent'],
			                 'future': ['','','','','',''],
			                 'perfect': ['erim','eris','erit','erimus','ritis','erint'],
			                 'pluperfect': ['issem','isses','isset','issemus','issetis','issent'],
			                 'future perfect': ['','','','','','']},
			           '3': {'present': ['am','as','at','amus','atis','ant'],
			                 'imperfect': ['erem', 'eres', 'eret','eremus', 'eretis','erent'],
			                 'future': [],
			                 'perfect': ['erim','eris','erit','erimus','ritis','erint'],
			                 'pluperfect': ['issem','isses','isset','issemus','issetis','issent'],
			                 'future perfect': []},
			           '3io': {'present': ['iam','ias','iat','iamus','iatis','iant'],
			                   'imperfect': ['erem', 'eres', 'eret','eremus', 'eretis','erent'],
			                   'future': [],
			                   'perfect': ['erim','eris','erit','erimus','ritis','erint'],
			                   'pluperfect': ['issem','isses','isset','issemus','issetis','issent'],
			                   'future perfect': []},
			           '4': {'present': ['iam','ias','iat','iamus','iatis','iant'],
			                 'imperfect': ['irem','ires','iret','iremus','iretis','irent'],
			                 'future': [],
			                 'perfect': ['erim','eris','erit','erimus','ritis','erint'],
			                 'pluperfect': ['issem','isses','isset','issemus','issetis','issent'],
			                 'future perfect': []}},
			'passive': {'1': {'present': ['er','eris','etur','emur','emini','entur'],
			                  'imperfect': ['arer','areris','aretur','aremur','aremini','arentur'],
			                  'future': [],
			                  'perfect': [' sim',' sis',' sit',' simus',' sitis',' sint'],
			                  'pluperfect': [' essem',' esses',' esset', ' essemus',' essetis',' essent'],
			                  'future perfect': []},
			            '2': {'present': ['ear','earis','eatur','eamur','eamini','eantur'],
			                  'imperfect': ['erer','ereris','eretur','eremur','eremini','erentur'],
			                  'future': [],
			                  'perfect': [' sim',' sis',' sit',' simus',' sitis',' sint'],
			                  'pluperfect': [' essem',' esses',' esset', ' essemus',' essetis',' essent'],
			                  'future perfect': []},
			            '3': {'present': ['ar','aris','atur','amur','amini','antur'],
			                  'imperfect': ['erer','ereris','eretur','eremur','eremini','erentur'],
			                  'future': [],
			                  'perfect': [' sim',' sis',' sit',' simus',' sitis',' sint'],
			                  'pluperfect': [' essem',' esses',' esset', ' essemus',' essetis',' essent'],
			                  'future perfect': []},
			            '3io': {'present': ['iar','iaris','iatur','iamur','iamini','iantur'],
			                    'imperfect': ['erer','ereris','eretur','eremur','eremini','erentur'],
			                    'future': [],
			                    'perfect': [' sim',' sis',' sit',' simus',' sitis',' sint'],
			                    'pluperfect': [' essem',' esses',' esset', ' essemus',' essetis',' essent'],
			                    'future perfect': []},
			            '4': {'present': ['iar','iaris','iatur','iamur','iamini','iantur'],
			                  'imperfect': ['irer','ireris','iretur','iremur','iremini','irentur'],
			                  'future': [],
			                  'perfect': [' sim',' sis',' sit',' simus',' sitis',' sint'],
			                  'pluperfect': [' essem',' esses',' esset', ' essemus',' essetis',' essent'],
			                  'future perfect': []}}
			}
		tk.Frame.__init__(self,master)
		def decide_conjugation(first_principle_part,second_principle_part):
			conjugation=0
			if second_principle_part[-3:] == 'are':
				conjugation=1
			elif second_principle_part[-3:]=='ire':
				conjugation=4
			elif second_principle_part[-3:]=='ere':
				if first_principle_part[-2:]=='eo':
					conjugation=2
				elif first_principle_part[-2]=='i':
					conjugation='3io'
				else:
					conjugation=3
			return str(conjugation)

		def fill_in_the_blank(target,content):
			target.config(state=tk.NORMAL)
			target.delete(0,'end')
			target.insert(0,str(content))
			target.config(state='readonly')

		def apply_to_all(function,argument1,argument2):
			for e1,e2 in zip(argument1,argument2):
				function(e1,e2)

		def conjugate(principle_part,stem_ending_index,ending):
			if stem_ending_index == 0:
				stem=principle_part[:]
			else:
				stem=principle_part[:stem_ending_index]
			answer=[]
			for e in ending:
				answer.append(stem+e)
			return answer

		class AllTenses(tk.Frame):
			def build(self,mood,title,class_of_selection):
				#self.config(pady=10)
				first_row_frame=tk.Frame(self)
				second_row_frame=tk.Frame(self)
				self.title=title

				tk.Label(self,text=title,font=('Times New Roman',24,'bold')).pack()

				self.present=VerbHolder(first_row_frame,'present',class_of_selection.present.get())
				self.imperfect=VerbHolder(first_row_frame,'imperfect',class_of_selection.imperfect.get())
				self.future=VerbHolder(first_row_frame,'future',class_of_selection.future.get())
				self.perfect=VerbHolder(second_row_frame,'perfect',class_of_selection.perfect.get())
				self.pluperfect=VerbHolder(second_row_frame,'pluperfect',class_of_selection.pluperfect.get())
				self.futureperfect=VerbHolder(second_row_frame,'future perfect',class_of_selection.futureperfect.get())

				first_row=(self.present,self.imperfect,self.future)
				second_row=(self.perfect,self.pluperfect,self.futureperfect)
				i=j=0

				for element in first_row:
					if element.isactive:
						i+=1
						element.grid(row=0,column=i)
				for element in second_row:
					if element.isactive:
						j+=1
						element.grid(row=0,column=j)
				first_row_frame.pack()
				second_row_frame.pack()

			def __init__(self,master,mood,title,endings,class_of_selection,isactive=True):
				tk.Frame.__init__(self,master)
				self.isactive=isactive
				self.endings=endings
				if isactive:
					self.build(mood,title,class_of_selection)

			def fill_answer(self,first_principle_part,second_principle_part,third_principle_part=None,fourth_principle_part=None):
				if not hasattr(self,'title'):
					return None
				list_of_non_perfect_tense=(self.present,self.imperfect,self.future,)
				list_of_perfect_tense=(self.perfect,self.pluperfect,self.futureperfect)#only active perfect tenses require third principle part
				conjugation=decide_conjugation(first_principle_part,second_principle_part)
				for element in list_of_non_perfect_tense:
					ending=self.endings[self.title][conjugation][element.title]
					element.fill(conjugate(second_principle_part,-3,ending))
				if self.title=='active':
					if hasattr(self,'perfect') or hasattr(self,'pluperfect') or hasattr(self,'futureperfect'):
						if third_principle_part is not None:
							for element in list_of_perfect_tense:
								ending=self.endings[self.title][conjugation][element.title]
								element.fill(conjugate(third_principle_part,-1,ending))
				elif self.title=='passive':
					if hasattr(self,'perfect') or hasattr(self,'pluperfect') or hasattr(self,'futureperfect'):
						if fourth_principle_part is not None:
							for element in list_of_perfect_tense:
								ending=self.endings[self.title][conjugation][element.title]
								element.fill(conjugate(fourth_principle_part,0,ending))
								element.fill_plural(conjugate(fourth_principle_part[:-2]+'i',0,ending[3:]))

		class VerbHolder(tk.Frame):

			def __init__(self,master,title,isactive=True):
				tk.Frame.__init__(self,master)
				self.isactive=isactive
				self.title=title
				tk.Label(self,text=title,font=('Times New Roman',16,'bold')).grid(row=0,column=1,columnspan=2)
				tk.Label(self,text='singular').grid(row=1,column=1)
				tk.Label(self,text='plural').grid(row=1,column=2)
				tk.Label(self,text='1st person').grid(row=2,column=0)
				tk.Label(self,text='2nd person').grid(row=3,column=0)
				tk.Label(self,text='3rd person').grid(row=4,column=0)
				self.s1=tk.Entry(self,width=15)
				self.s1.grid(row=2,column=1)
				self.s2=tk.Entry(self,width=15)
				self.s2.grid(row=3,column=1)
				self.s3=tk.Entry(self,width=15)
				self.s3.grid(row=4,column=1)
				self.p1=tk.Entry(self,width=15)
				self.p1.grid(row=2,column=2)
				self.p2=tk.Entry(self,width=15)
				self.p2.grid(row=3,column=2)
				self.p3=tk.Entry(self,width=15)
				self.p3.grid(row=4,column=2)
				self.config(padx=10,pady=10)

			def fill(self,content):
				"""expecting content to be a iterable with 6 elements"""
				if self.isactive:
					target=(self.s1,self.s2,self.s3,self.p1,self.p2,self.p3)
					apply_to_all(fill_in_the_blank,target,content)

			def fill_plural(self,content):
				if self.isactive:
					target=(self.p1,self.p2,self.p3)
					apply_to_all(fill_in_the_blank,target,content)

			def fill_singular(self,content):
				if self.isactive:
					target=(self.s1,self.s2,self.s3,)
					apply_to_all(fill_in_the_blank,target,content)

		class Voice():
			def __init__(self,master,mood,voice,endings):
				self.selection=Selection(master,voice)
				self.endings=endings
				self.voice=voice
				self.mood=mood

			def build(self,master):
				self.tense=AllTenses(master,self.mood,self.voice,self.endings,self.selection,self.selection.main_selection.get())

		class Mood(tk.Frame):
			def __init__(self,master,mood,endings):
				tk.Frame.__init__(self,master)
				self.mood=mood
				self.selected=tk.BooleanVar()
				self.title=tk.Label(self,text=self.mood,font=('Times New Roman',16,'bold'))
				self.title.grid(row=0,columnspan=2)
				self.active=Voice(self,mood,'active',endings)
				self.active.selection.grid(row=1,column=0)
				self.passive=Voice(self,mood,'passive',endings)
				self.passive.selection.grid(row=1, column=1)

		class Selection(tk.Frame):
			def __init__(self,master,title):
				tk.Frame.__init__(self,master)
				self.main_selection=tk.IntVar()
				self.present=tk.IntVar()
				self.imperfect=tk.IntVar()
				self.future=tk.IntVar()
				self.perfect=tk.IntVar()
				self.pluperfect=tk.IntVar()
				self.futureperfect=tk.IntVar()
				tk.Checkbutton(self,text=title,variable=self.main_selection,command=lambda:self.select_all()).grid(row=0,column=0,columnspan=2)
				self.present_check=tk.Checkbutton(self,text='present',variable=self.present,state=tk.DISABLED)
				self.present_check.grid(row=1,column=0,sticky='w')
				self.imperfect_check=tk.Checkbutton(self,text='imperfect',variable=self.imperfect,state=tk.DISABLED)
				self.imperfect_check.grid(row=2,column=0,sticky='w')
				self.future_check=tk.Checkbutton(self,text='future',variable=self.future,state=tk.DISABLED)
				self.future_check.grid(row=3,column=0,sticky='w')
				self.perfect_check=tk.Checkbutton(self,text='perfect',variable=self.perfect,state=tk.DISABLED)
				self.perfect_check.grid(row=1,column=1,sticky='w')
				self.pluperfect_check=tk.Checkbutton(self,text='pluperfect',variable=self.pluperfect,state=tk.DISABLED)
				self.pluperfect_check.grid(row=2,column=1,sticky='w')
				self.futureperfect_check=tk.Checkbutton(self,text='future perfect',variable=self.futureperfect,state=tk.DISABLED)
				self.futureperfect_check.grid(row=3,column=1,sticky='w')

			def select_all(self):
				select=self.main_selection.get()
				self.present.set(select)
				self.imperfect.set(select)
				self.future.set(select)
				self.perfect.set(select)
				self.pluperfect.set(select)
				self.futureperfect.set(select)
				if not select:
					self.present_check.config(state=tk.DISABLED)
					self.future_check.config(state=tk.DISABLED)
					self.imperfect_check.config(state=tk.DISABLED)
					self.pluperfect_check.config(state=tk.DISABLED)
					self.perfect_check.config(state=tk.DISABLED)
					self.futureperfect_check.config(state=tk.DISABLED)
				else:
					self.present_check.config(state=tk.NORMAL)
					self.future_check.config(state=tk.NORMAL)
					self.imperfect_check.config(state=tk.NORMAL)
					self.pluperfect_check.config(state=tk.NORMAL)
					self.perfect_check.config(state=tk.NORMAL)
					self.futureperfect_check.config(state=tk.NORMAL)


		textbox_frame=tk.Frame(self)
		tk.Label(textbox_frame,text="Please enter the dictionary form of the word here").pack()
		tk.Label(textbox_frame,text='e.g. cogito, cogitare, cogitavi, cogitatus').pack()
		frame=tk.Frame(textbox_frame)
		usr_input=tk.Entry(frame,width=30)
		usr_input.bind('<Return>',lambda x: generate())
		usr_input.pack(side=tk.LEFT)
		frame.pack()

		textbox_frame.pack()

		ls=tk.LabelFrame(self, text="Please select what you want to conjugate:",font=('Sans-serif', 14),labelanchor='n')

		indicative=Mood(ls,'indicative',endings_indicative)
		subjunctive=Mood(ls,'subjunctive',endings_subjunctive)

		subjunctive.active.selection.future_check.grid_forget()
		subjunctive.active.selection.futureperfect_check.grid_forget()
		subjunctive.passive.selection.future_check.grid_forget()
		subjunctive.passive.selection.futureperfect_check.grid_forget()

		indicative.active.selection.main_selection.set(True)
		indicative.active.selection.select_all()

		indicative.pack()
		subjunctive.pack()

		ls.pack()

		def generate():
			display=True
			result_panel=tk.Toplevel()
			result_panel.title("")
			#result_panel.overrideredirect(1)
			result_panel.lift()
			result_panel.grab_set()
			data=usr_input.get()
			if data.replace(' ','') == '':
				#tk.Label(result_panel,text='Error: Please enter the word',font=('Times New Roman',15,'bold')).pack()
				#centerwindow(result_panel,22,146)
				display=False
				data=['place holder']

			self.answer_area=tk.Frame(result_panel)

			indicative_frame=tk.Frame(self.answer_area)
			subjunctive_frame=tk.Frame(self.answer_area)

			indicative.active.build(indicative_frame)
			indicative.passive.build(indicative_frame)

			tk.Label(indicative_frame,text='indicative',font=('Times New Roman',30)).pack()
			indicative.active.tense.pack()
			indicative.passive.tense.pack()

			subjunctive.active.build(subjunctive_frame)
			subjunctive.passive.build(subjunctive_frame)

			tk.Label(subjunctive_frame, text='subjunctive', font=('Times New Roman', 30)).pack()
			subjunctive.active.tense.pack()
			subjunctive.passive.tense.pack()
			#self.answer_area.pack()

			###starting conjugate

			try:
				data=data.replace(' ','')
				data = data.split(',')
			except AttributeError:
				pass
			i=0
			while i<len(data):
				if data[i]=='':
					data[i]=None
				i+=1
			try:
				first_part=data[0]
				second_part=data[1]
				assert first_part is not None
				assert second_part is not None
			except (IndexError,AssertionError):
				display=False
				tk.Label(result_panel,text='        Error: Please provide the first and second principle parts',font=('Times New Roman',15,'bold')).pack(anchor='w')

			if indicative.active.selection.perfect.get() or indicative.active.selection.pluperfect.get() or indicative.active.selection.futureperfect.get() or subjunctive.active.selection.perfect.get() or subjunctive.active.selection.pluperfect.get():
				try:
					third_part=data[2]
				except IndexError:
					tk.Label(result_panel,text="        Error: Please provide the third principle part of the word",font=('Times New Roman',15,'bold')).pack(anchor='w')
					centerwindow(result_panel,44,327)
					display=False
					third_part=None
			else:
				third_part=None

			if indicative.passive.selection.perfect.get() or indicative.passive.selection.pluperfect.get() or indicative.passive.selection.futureperfect.get() or subjunctive.passive.selection.perfect.get() or subjunctive.passive.selection.pluperfect.get():
				try:
					fourth_part=data[3]
				except IndexError:
					tk.Label(result_panel,text="        Error: Please provide the fourth principle part of the word",font=('Times New Roman',15,'bold')).pack(anchor='w')
					centerwindow(result_panel, 44, 327)
					display=False
					fourth_part=None
			else:
				fourth_part=None

			try:
				indicative.active.tense.fill_answer(first_part,second_part,third_part,fourth_part)
				indicative.passive.tense.fill_answer(first_part,second_part,third_part,fourth_part)
				subjunctive.active.tense.fill_answer(first_part, second_part, third_part, fourth_part)
				subjunctive.passive.tense.fill_answer(first_part, second_part, third_part, fourth_part)
			except KeyError:
				display=False
				tk.Label(result_panel,text="        Error: Could not recognize the word.",font=('Times New Roman',15,'bold')).pack(anchor='w')
			except UnboundLocalError:
				pass
			num_to_seq={'1':'first','2':'second','3':'third','3io':'third-io','4':'fourth'}

			###display###
			if not indicative.active.selection.main_selection.get() and not indicative.passive.selection.main_selection.get() and not subjunctive.active.selection.main_selection.get() and not subjunctive.passive.selection.main_selection.get():
				tk.Label(result_panel,text="        Error: You did not select anything to be displayed (Checkboxes below)",font=('Times New Roman',15,'bold')).pack(anchor='w')
				display=False
			elif display:
				tk.Label(result_panel,text="The Conjugation of The Verb: "+usr_input.get()+\
				'  ('+num_to_seq[decide_conjugation(first_part,second_part)]+' conjugation)',font=('Times New Roman',30,'italic')).pack()

			buttonframe = tk.Frame(result_panel)

			if display:
				centerwindow(result_panel, 774, 1179)
				result_panel.geometry('1179x774')

				master.withdraw()
				indicative.selected=indicative.active.selection.main_selection.get() or indicative.passive.selection.main_selection.get()
				subjunctive.selected=subjunctive.active.selection.main_selection.get() or subjunctive.passive.selection.main_selection.get()

				if indicative.selected:
					indicative_frame.pack()
				if subjunctive.selected:
					subjunctive_frame.pack()

				self.answer_area.pack()
			else:
				error_frame=tk.Frame(result_panel)
				tk.Label(error_frame,text='').pack()
				tk.Label(error_frame,text="The above error(s) may also occur because you didn't enter the word in a").pack(anchor='w')
				tk.Label(error_frame,text=" machine-recognizable form. Your input should be like this: ").pack(anchor='w')
				entry = tk.Entry(error_frame)
				entry.insert(0, 'cogito, cogitare, cogitavi, cogitatus')
				entry.pack()
				entry.config(state='readonly')
				tk.Label(error_frame,
				         text='Note that the space after each comma is optional, but the comma itself is not.').pack(anchor='w')
				tk.Label(error_frame,
				         text='You will only be required to enter the third principle part if you selected').pack(anchor='w',)
				tk.Label(error_frame,
				         text='any perfect tenses in active voice, and fourth principle part if you selected').pack(anchor='w')
				tk.Label(error_frame,
				         text='any perfect tenses in passive voice. If you choose to omit the third principle').pack(anchor='w')
				tk.Label(error_frame,
				         text='part, you should still keep the comma. For example: cogito, cogitare, ,cogitatus"').pack(anchor='w')
				help_button = tk.Button(result_panel,text='Help?',
				                        command=lambda: (f for f in (error_frame.pack(), help_button.pack_forget())))
				help_button.pack(side=tk.LEFT)
				centerwindow(result_panel,254,508)





			back_button=tk.Button(buttonframe,text='Back',command=result_panel.destroy)
			back_button.pack()
			buttonframe.pack()
			result_panel.update()




			if display:

				try:
					subjunctive.active.tense.future.grid_forget()
					subjunctive.active.tense.futureperfect.grid_forget()
				except AttributeError:
					pass

				try:
					subjunctive.passive.tense.future.grid_forget()
					subjunctive.passive.tense.futureperfect.grid_forget()
				except AttributeError:
					pass

				if indicative.selected and subjunctive.selected:
					next_button = tk.Button(buttonframe, text='Next Page >',command=lambda: next_page())
					last_button = tk.Button(buttonframe, text='< Last Page',command=lambda: last_page())
					def last_page():
						indicative_frame.pack()
						subjunctive_frame.pack_forget()
						last_button.pack_forget()
						back_button.pack_configure(side=tk.LEFT)
						next_button.pack(side=tk.RIGHT)
						result_panel.update()

					def next_page():
						subjunctive_frame.pack()
						indicative_frame.pack_forget()
						next_button.pack_forget()
						back_button.pack_configure(side=tk.RIGHT)
						last_button.pack(side=tk.LEFT)
						result_panel.update()

					last_page()

				master.wait_window(result_panel)
				master.deiconify()

		def sum():
			display=True
			result_panel=tk.Toplevel()
			#result_panel.overrideredirect(1)
			result_panel.lift()
			result_panel.grab_set()
			if not indicative.active.selection.main_selection.get() and not indicative.passive.selection.main_selection.get():
				tk.Label(result_panel,text="You did not select anything to be displayed ").pack()
				display=False
			else:
				tk.Label(result_panel,text="The Conjugation of The Verb: sum, esse, fui, futurus",font=('Times New Roman',30,'italic')).pack()

			indicative.active.build(result_panel)


			if indicative.active.tense.isactive:
				indicative.active.tense.present.fill(('sum','es','est','sumus','estis','sunt'))
				indicative.active.tense.imperfect.fill(('eram','eras','erat', 'eramus','eratis','erant'))
				indicative.active.tense.future.fill(('ero','eris','erit','erimus','eritis','erunt'))
				indicative.active.tense.perfect.fill(('fui','fuisti','fuit','fuimus','fuistis','fuerunt'))
				indicative.active.tense.pluperfect.fill(('fueram','fueras','fuerat','fueramus','fueratis','fuerant'))
				indicative.active.tense.futureperfect.fill(('fuero','fueris','fuerit','fuerimus','fueritis','fuerint'))
			if display:
				master.withdraw()
				indicative.active.tense.pack()
				if indicative.passive.selection.main_selection.get():
					tk.Label(result_panel,text='The verb posse has no passive voice',font=('Times New Roman',16)).pack()
			tk.Button(result_panel,text='Back',command=result_panel.destroy).pack()
			if display:
				master.wait_window(result_panel)
				master.deiconify()

		def possum():
			display=True
			result_panel=tk.Toplevel()
			#result_panel.overrideredirect(1)
			result_panel.lift()
			result_panel.grab_set()
			if not indicative.active.selection.main_selection.get() and not indicative.passive.selection.main_selection.get():
				tk.Label(result_panel,text="Error: Please select something to be displayed").pack(anchor='w')
				display=False
			else:
				tk.Label(result_panel,text="The Conjugation of The Verb: posum, posse, potui, --",font=('Times New Roman',30,'italic')).pack()
			indicative.active.build(result_panel)
			if indicative.active.tense.isactive:
				indicative.active.tense.present.fill(('possum','potes','potest','possumus','potestis','possunt'))
				indicative.active.tense.imperfect.fill(('poteram','poteras','poterat', 'poteramus','poteratis','poterant'))
				indicative.active.tense.future.fill(('potero','poteris','poterit','poterimus','poteritis','poterunt'))
				indicative.active.tense.perfect.fill(('potui','potuisti','potuit','potuimus','potuistis','potuerunt'))
				indicative.active.tense.pluperfect.fill(('potueram','potueras','potuerat','potueramus','potueratis','potuerant'))
				indicative.active.tense.futureperfect.fill(('potuero','potueris','potuerit','potuerimus','potueritis','potuerint'))
			if display:
				window_widget.withdraw()
				indicative.active.tense.pack()
				if indicative.passive.selection.main_selection.get():
					tk.Label(result_panel,text='The verb posse has no passive voice',font=('Times New Roman',16)).pack()


			tk.Button(result_panel,text='Back',command=result_panel.destroy).pack()
			if display:
				window_widget.wait_window(result_panel)
				window_widget.deiconify()


		#usr_input.insert(0,'amo, amare, amavi, amatus') #debug

		tk.Button(frame,text='generate',command=generate).pack(side=tk.RIGHT)

		# specialcase=tk.Frame(self)
		# tk.Label(specialcase,text='special cases: ').pack(side=tk.LEFT)
		# tk.Button(specialcase,text="esse",command=sum).pack(side=tk.LEFT)
		# tk.Button(specialcase,text="posse",command=possum).pack(side=tk.LEFT)
		# specialcase.pack()  #special cases will be updated soon(hopefully,) with new API

	
if __name__ == '__main__':
	root = tk.Tk()
	verb=Verb(root,root)
	verb.pack()
	root.attributes('-topmost',True)
	root.bind('<FocusIn>',lambda x: [f for f in (root.attributes('-topmost',False),root.unbind('<FocusIn'))])
	root.mainloop()
