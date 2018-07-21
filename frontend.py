import tkinter as Tk
import backend

def viewcommand():
    list1.delete(0,Tk.END)
    for row in backend.view():
        list1.insert(Tk.END,row)

        
def searchcommand():
     list1.delete(0,Tk.END)
     for row in backend.search(t.get()):
         list1.insert(Tk.END,row)

         
def addnote():
    backend.insert(t.get())
    list1.delete(0,Tk.END)
    list1.insert(Tk.END,t.get())

    
def getselectedrow(event):
    global selectedtuple
    index=list1.curselection()[0]
    selectedtuple=list1.get(index)

    
def deletecommand():    
    backend.delete(selectedtuple[0])


window=Tk.Tk()
window.title('Note Taking app')
window.geometry("500x370")
l1=Tk.Label(window,text="Enter your input",padx=5, pady=5,font=("Arial Bold", 15),bg="blue",fg="black")
l1.grid(row=0,column=1)
t = Tk.Entry(window, width=40)
t.grid(row=0,column=0)
list1=Tk.Listbox(window,height=20,width=40)
list1.grid(row=3,column=0)
sb1=Tk.Scrollbar(window)
sb1.place(x=300,y=80)
list1.configure(yscrollcommand=sb1.set)
list1.bind('<<ListboxSelect>>',getselectedrow)
sb1.configure(command=list1.yview)
btn1 = Tk.Button(window, text="ADD NEW NOTE",padx=5, pady=5,font=("Arial Bold", 10),bg="blue",fg="black",command=addnote)
btn1.place(x=350,y=50)
btn2 = Tk.Button(window, text="VIEW ALL",padx=5, pady=5,font=("Arial Bold", 10),bg="blue",fg="black",command=viewcommand)
btn2.place(x=350,y=90)
btn3 = Tk.Button(window, text="SEARCH NOTE",padx=5, pady=5,font=("Arial Bold", 10),bg="blue",fg="black",command=searchcommand)
btn3.place(x=350,y=130)
btn5 = Tk.Button(window, text="DELETE NOTE",padx=5, pady=5,font=("Arial Bold", 10),bg="blue",fg="black",command=deletecommand)
btn5.place(x=350,y=170)
btn6 = Tk.Button(window, text="EXIT NOTE",padx=5, pady=5,font=("Arial Bold", 10),bg="blue",fg="black",command=window.destroy)
btn6.place(x=350,y=210)
window.mainloop()
