try:
	import tkinter as tk
	import tkinter.ttk as ttk
except ImportError:
	import Tkinter as tk
	import ttk

import sys
from Noun import Noun
from Verb import Verb
from Adjective import Adjective
from Pronoun import Pronoun

softwarename = 'Latin Helper '  # remember to put a space after the name
version = '0.2.1'

root = tk.Tk()

root.withdraw()
root.title('')

is_quit = False


def quitsoftware(window):
	global is_quit
	is_quit = True
	window.destroy()
	sys.exit(0)

def centerwindow(window,h,w):
	sh = window.winfo_screenheight()
	sw = window.winfo_screenwidth()
	window.geometry('+' + str((sw - w) // 2) + '+' + str((sh - h) // 2))

def getwinfo(widget):
	widget.update()
	print('height= %s, width= %s'% (widget.winfo_height(), widget.winfo_width()))


root.createcommand('::tk::mac::Quit', lambda: quitsoftware(first))


root.bind_all('<Command-W>', lambda event: quitsoftware(root))


first = tk.Toplevel()
title_frame = tk.Frame(first, height=10, width=200)
first.title(softwarename)
# tk.Label(first,text=sys.version_info).pack()
tk.Label(first, text=softwarename, font=("zapfino", 24)).pack()

title_frame.pack()
buttons_frame = tk.Frame(first)

tk.Button(buttons_frame, text="Next", command=lambda: first.destroy()).pack(side=tk.RIGHT)
tk.Button(buttons_frame, text="Quit", command=lambda: quitsoftware(first)).pack(side=tk.LEFT)
tk.Label(first, text="By Ruocheng Wang", font=("Times New Roman", 14), fg="gray").pack()
tk.Label(first, text="Version " + version, font=("Times New Roman", 14), fg="gray").pack()
buttons_frame.pack(fill=tk.X)
first.protocol("WM_DELETE_WINDOW", lambda: quitsoftware(first))
first.attributes('-topmost', True)
first.bind('<FocusIn>', lambda x: (f for f in (first.attributes('-topmost', False), first.unbind('<FocusIn>'))))

centerwindow(first,169,208)


root.wait_window(first)
root.createcommand('::tk::mac::Quit', lambda: quitsoftware(selection))
selection=tk.Toplevel()
centerwindow(selection,627,778)
selection.protocol("WM_DELETE_WINDOW", lambda: quitsoftware(selection))
selection.attributes('-topmost', True)
selection.bind('<FocusIn>', lambda x: (f for f in (selection.attributes('-topmost', False), selection.unbind('<FocusIn>'))))
verb=Verb(selection,selection)
noun=Noun(selection,selection)
pronoun=Pronoun(selection,selection)
adjective=Adjective(selection,selection)

tk.Label(selection,text="Nouns",font=("Times New Roman",24)).grid(row=0,column=0)
tk.Label(selection,text="Verbs",font=("Times New Roman",24)).grid(row=0,column=2)
verb.grid(row=1,column=2)
noun.grid(row=1,column=0)
tk.Label(selection,text="Pronouns",font=("Times New Roman",24)).grid(row=3,column=0)
tk.Label(selection,text="Adjectives",font=("Times New Roman",24)).grid(row=3,column=2)
pronoun.grid(row=4,column=0)
adjective.grid(row=4,column=2)
ttk.Separator(selection,orient='horizontal').grid(row=2,columnspan=3,sticky='ew',pady=10)
ttk.Separator(selection).grid(column=1,row=0,rowspan=5,sticky='sn',padx=25)
tk.Button(selection,text='Quit',command=lambda: quitsoftware(selection)).grid(row=5,column=1)

if not is_quit:
	root.wait_window(selection)
