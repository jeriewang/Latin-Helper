try:
	import tkinter as tk
	import tkinter.scrolledtext as tkst
except ImportError:
	import  Tkinter as tk
import sys
from Noun import Noun
from Verb import Verb

softwarename = 'Latin Helper '  # remember to put a space after the name
version = '0.0.2'

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
selection.protocol("WM_DELETE_WINDOW", lambda: quitsoftware(selection))
selection.attributes('-topmost', True)
selection.bind('<FocusIn>', lambda x: (f for f in (selection.attributes('-topmost', False), selection.unbind('<FocusIn>'))))
verb=Verb(selection,selection)
noun=Noun(selection,selection)


tk.Label(selection,text="Nouns",font=("Times New Roman",24)).grid(row=0,column=0)
tk.Label(selection,text="Verbs",font=("Times New Roman",24)).grid(row=0,column=1)
verb.grid(row=1,column=1,padx=50)
noun.grid(row=1,column=0)

centerwindow(selection,251,792)

if not is_quit:
	root.wait_window(selection)
