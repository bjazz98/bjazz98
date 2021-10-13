from tkinter import *
from tkinter.scrolledtext import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter.font import Font
def new_command():
    """checks if there's any text in the texfield, if there is, prompts user if they want to continue, if they select yes, the texfield is cleared"""
    global text
    x = text.get('1.0', 'end-1c')
    if len(x)>0:
        answer = messagebox.askquestion('New', 'Would you like to continue?')
        if answer == 'yes':
            text.delete('1.0','end')

def open_command():
    """ opens a file dialog box and allows users to select a file to open the text in the textfield"""
    global text
    x = text.get('1.0', 'end-1c')
    #clears any previous text before opening new file
    if len(x)>0:
        text.delete('1.0','end')

    file = filedialog.askopenfile(mode = 'r', title='Please Select File:', filetypes = [('txt files', '*.txt')])
    if file is not None:
        contents = file.read()
        text.insert(INSERT,contents)

def save_command():
    """opens a file dialog box and allows users to select a path and name for the text in the textfield to be saved (saved as .txt files)"""
    global text
    file = filedialog.asksaveasfilename(title= 'Save As',filetypes = [('txt files', '*.txt')])
    f = open(file, 'w')
    f.write(text.get('1.0', 'end'))
    f.close()
    messagebox.showinfo('Save', 'File Saved')

def copy_command():
   """temporarily stores the text that is currently highlighted on the textfield"""
    global text
    global saved
    x = text.selection_get()
    saved = x

def cut_command():
    """temporarily stores the text that is currently highlighted on the textfield, as well as deletes the selected text from the textfield"""
    global text
    global saved
    x = text.get(SEL_FIRST, SEL_LAST)
    saved = x
    index1 = text.index(SEL_FIRST)
    index2 = text.index(SEL_LAST)
    text.delete(index1,index2)

def paste_command():
    """ inserts any text that is temporarily stored where the cursor in the textfield is"""
    global text
    global saved
    index = text.index(INSERT)
    text.insert(index, saved)

def font():
    """changes font size"""
    global entry
    global text
    global font1
    x = entry.get()
    font1.configure(size=x)
    
    
    
    
    



    
'''Below is code that creates the layout of the text processor'''
saved = ''    
root = Tk()
root.title('Microsoft Word')
root.geometry('500x500')

menuBar = Menu(root)

fileMenu = Menu(menuBar)
fileMenu.add_command(label = 'New', command = new_command)
fileMenu.add_command(label = 'Open', command = open_command)
fileMenu.add_command(label = 'Save', command = save_command)

editMenu = Menu(menuBar)
editMenu.add_command(label = 'Copy', command = copy_command)
editMenu.add_command(label = 'Cut', command = cut_command)
editMenu.add_command(label = 'Paste', command = paste_command)

menuBar.add_cascade(label = 'File', menu = fileMenu)
menuBar.add_cascade(label = 'Edit', menu = editMenu)

root.config(menu = menuBar)

frame = Frame(root)
label = Label(frame,text = 'Font Size:')
label.pack(side=LEFT)
entry = Entry(frame)
entry.pack(side=LEFT)

displayButton = Button(frame, text = 'Enter', command = font)
displayButton.pack(side=LEFT)

frame.pack(side=TOP)

text = ScrolledText(root,height = 30, width = 100, wrap = WORD)
text.pack()

font1 = Font(family="Times New Roman", size = 12)
text.configure(font=font1)

root.mainloop()


