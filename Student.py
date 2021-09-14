import tkinter as tk
from tkinter import Entry
from tkinter import Label
from tkinter import Button
from tkinter import messagebox as mb


def welcomeDialog():
    mb.showinfo("Record Data","Data")


def validateRNo(rno):
    return rno.isdigit() and 1<=int(rno)<=50

def validateName(na):
    for x in na.lower():
        if x not in " abcdefghijklmnopqrstuvwxyz":
            return False
    return True

def validateStudentInfo(info):
    flag=[True,True,True,True,True,True,True,True,True]
    flag[0]=validateRNo(info[0])
    flag[1]=validateName(info[1])

    return flag
    
def addRecordGUI():
    
    myWindow=tk.Tk()
    myWindow.title("Add Log")
    myWindow.geometry("600x500")
    
    myLabelMsg0=Label(myWindow,text="",padx=50,pady=10)
    myLabelMsg0.grid(row=0,column=0)

    myLabelMsg1=Label(myWindow,text="Roll No.",padx=50,pady=10)
    myLabelMsg1.grid(row=1,column=0)
    
    myEntryNo1=Entry(myWindow,width=35)
    myEntryNo1.grid(row=1,column=1) 
    
    myLabelMsg2=Label(myWindow,text="Name",padx=50,pady=10)
    myLabelMsg2.grid(row=2,column=0)

    myEntryNo2=Entry(myWindow,width=35)
    myEntryNo2.grid(row=2,column=1) 
    
    myLabelMsg3=Label(myWindow,text="Address",padx=50,pady=10)
    myLabelMsg3.grid(row=3,column=0)

    myEntryNo3=Entry(myWindow,width=35)
    myEntryNo3.grid(row=3,column=1) 
    
    myLabelMsg4=Label(myWindow,text="Standard",padx=50,pady=10)
    myLabelMsg4.grid(row=4,column=0)

    myEntryNo4=Entry(myWindow,width=35)
    myEntryNo4.grid(row=4,column=1) 
    
    myLabelMsg5=Label(myWindow,text="Division",padx=50,pady=10)
    myLabelMsg5.grid(row=5,column=0)

    myEntryNo5=Entry(myWindow,width=35)
    myEntryNo5.grid(row=5,column=1) 
    
    myLabelMsg6=Label(myWindow,text="Gender",padx=50,pady=10)
    myLabelMsg6.grid(row=6,column=0)
    
    myEntryNo6=Entry(myWindow,width=35)
    myEntryNo6.grid(row=6,column=1) 
    
    myLabelMsg7=Label(myWindow,text="Computer",padx=50,pady=10)
    myLabelMsg7.grid(row=7,column=0)
    
    myEntryNo7=Entry(myWindow,width=35)
    myEntryNo7.grid(row=7,column=1) 
    
    myLabelMsg8=Label(myWindow,text="Maths",padx=50,pady=10)
    myLabelMsg8.grid(row=8,column=0)
    
    myEntryNo8=Entry(myWindow,width=35)
    myEntryNo8.grid(row=8,column=1) 
    
    myLabelMsg9=Label(myWindow,text="Science",padx=50,pady=10)
    myLabelMsg9.grid(row=9,column=0)

    myEntryNo9=Entry(myWindow,width=35)
    myEntryNo9.grid(row=9,column=1) 
    
    def AddStudentData():
        info=[myEntryNo1.get(),myEntryNo2.get(),myEntryNo3.get(),myEntryNo4.get(),myEntryNo5.get(),myEntryNo6.get(),myEntryNo7.get(),myEntryNo8.get(),myEntryNo9.get()]
        errorMessage=("Invalid Roll Number. Numbers between 1 and 50","Invalid Name. Alphabet and space only allowed ","","","","","","","")
        flag=validateStudentInfo(info)
        check=True
        for i in range(0,len(flag)):
            if flag[i]==False:
                check=False
                print(errorMessage[i])
        
        if check:
            print("Insert data into database")
        
    def reset():
        myEntryNo1.delete(0,len(myEntryNo1.get()))
        myEntryNo2.delete(0,len(myEntryNo2.get()))
        myEntryNo3.delete(0,len(myEntryNo3.get()))
        myEntryNo4.delete(0,len(myEntryNo4.get()))
        myEntryNo5.delete(0,len(myEntryNo5.get()))
        myEntryNo6.delete(0,len(myEntryNo6.get()))
        myEntryNo7.delete(0,len(myEntryNo7.get()))
        myEntryNo8.delete(0,len(myEntryNo8.get()))
        myEntryNo9.delete(0,len(myEntryNo9.get()))
    
    myButtonSubmit=Button(myWindow,text="Submit",padx=20,pady=10,command=AddStudentData)
    myButtonSubmit.grid(row=10,column=1)
    
    myButtonReset=Button(myWindow,text="Reset",padx=20,pady=10,command=reset)
    myButtonReset.grid(row=10,column=2)

myWindow=tk.Tk()
myWindow.title("Student Logs")
myWindow.geometry("600x400")

myLabelMsg0=Label(myWindow,text="",padx=75,pady=15)
myLabelMsg0.grid(row=0,column=0)

myLabelTitle=Label(myWindow,text="Student Logs",padx=75,pady=15,bg='black',fg='White',bd=10,relief='sunken',font='Roboto')
myLabelTitle.grid(row=1,column=1)

myLabelMsg0=Label(myWindow,text="",padx=75,pady=15)
myLabelMsg0.grid(row=2,column=0)

myLabelSpace=Label(myWindow,text="")
myLabelSpace.grid(row=3,column=0)

myButtonAdd=Button(myWindow,text="Add",padx=20,pady=10,command = addRecordGUI)#Add command
myButtonAdd.grid(row=7,column=0)

myButtonEdit=Button(myWindow,text="Edit",padx=20,pady=10)#Add command
myButtonEdit.grid(row=7,column=1)

myButtonView=Button(myWindow,text="View",padx=20,pady=10,command=welcomeDialog)
myButtonView.grid(row=7,column=2)

myLabelSpace.grid(row=8,column=0)

myButtonDelete=Button(myWindow,text="Delete",padx=20,pady=10)#Add command
myButtonDelete.grid(row=9,column=0)

myButtonClear = Button(myWindow, text= "Exit", padx=20,pady=10,command=myWindow.destroy)
myButtonClear.grid(row = 9, column=2)

myWindow.mainloop()