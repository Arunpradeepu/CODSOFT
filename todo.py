from asyncio import tasks
import tkinter as tk
from tkinter import ANCHOR, END, Button, Entry, Frame, StringVar

from numpy import pad
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x650")
root.resizable(False, False)

task_list=[]

def addTask():
    task=task_entry.get()
    task_entry.delete(0,END)

    if task:
        with open("task.txt",'a') as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert(END,task)

def deleteTask():
    global task_list
    task=str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("task.txt",'w') as taskfile:
            for task in task_list:
                taskfile.write(task+"\n")
        listbox.delete(ANCHOR)        

def add_task_list():
    try:
        global task_list
        with open("task.txt",'r') as taskfile:
            tasks=taskfile.readlines()
        for task in tasks:
            if task!='\n':
                task_list.append(task)
                listbox.insert(tk.END ,task)
    except:
        file=open("task.txt","w")
        file.close()
  

    

icon = tk.PhotoImage(file="taskicon.png")
root.iconphoto(False,icon)

top = tk.PhotoImage(file="new.png")
tk.Label(root, image=top).pack()

doc= tk.PhotoImage(file="dock.png")
tk.Label(root, image=doc ,bg="#FF5733").place(x=30,y=50)

note= tk.PhotoImage(file="note.png")
tk.Label(root, image=note ,bg="#FF5733").place(x=340,y=50)

heading=tk.Label(text="TO-DO-LIST",font="arial 25 bold",fg="black",bg="#FF5733")
heading.place(x=100,y=40)

frame= tk.Frame(root,width="400",height="75",bg="black")
frame.place(x=0,y=150)

task= StringVar()
task_entry=Entry(frame,width=18,font="arial 20")
task_entry.place(x=10,y=20)
task_entry.focus()

button=Button(frame,text="ADD",font="arial 15 ", width=6,height=1,command=addTask)
button.place(x=300,y=20)

frame1=tk.Frame(root,bd=3,width=700,height=280,bg="#FF5733")
frame1.pack(pady=(130,0))

listbox=tk.Listbox(frame1,font=('arial', 12),width=40 ,height=16,bg="#FF5733",fg="black",cursor="Hand2",)
listbox.pack(side="left",fill="both",padx=2)
scroll=tk.Scrollbar(frame1)
scroll.pack(side="right",fill="both")

listbox.config(yscrollcommand=scroll.set)
scroll.config(command=listbox.yview)

add_task_list()
delete=tk.PhotoImage(file="delete.png")
Button(root,image=delete,bd=0,command=deleteTask).pack(side="bottom",pady=13)
root.mainloop()

