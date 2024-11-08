from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

window = Tk()
window.title("Notepad ripoff")
window.geometry("700x600")
window.rowconfigure(0,minsize=800,weight=1)
window.columnconfigure(1,minsize=800,weight=1)

#open file function
def openfile():
    filepath=askopenfilename(defaultextension=".txt*",filetypes=[("Text files","*.txt"),("All files","*.*")])
    if not filepath:
        return
    txt_edit.delete(1.0,END)

    with open(filepath,"r")as input_file:
        text = input_file.read()
        txt_edit.insert(END,text)
        input_file.close()
        
def save_asfile():
    filepath= asksaveasfilename(filetypes=[("Text files","*.txt"),("All files","*.*")])
    if not filepath:
        return

    with open(filepath,"w")as output_file:
        text=txt_edit.get(1.0,END)
        output_file.write(text)
        output_file.close()
        
txt_edit=Text(window)
Frame_btn=Frame(window,relief=RAISED,bd=2)
btn_open=Button(Frame_btn,text="open", command=openfile)
btn_save=Button(Frame_btn,text="save as" , command = save_asfile)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)

Frame_btn.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

window.mainloop()
