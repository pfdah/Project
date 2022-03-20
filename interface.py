import tkinter as tk
from tkinter import *
import capture
import os
import shutil
from data_preprocess import preprocess
from train_main import trainin
from sheets import insert_attendance,mark_attendance,close_attendance
import face_recognition

def putCreateWindow():
    window = Tk()
    window.geometry("600x500")
    #window.configure(background='')
    window.title("Attendance System - Creating Record")
    #window.geometry("800x500")
    tk.Label(window, text = "Attendance Software").pack()
    
    LabelInfo = tk.Label(window,text="CREATE RECORD").place(x=40,y=80);
    
    LabelstName = tk.Label(window,text="Name").place(x=40,y=120)
    stName = tk.Entry(window)
    stName.place(x=80, y=120, width=250, height=25)

    
    def captureImage():
        capture.captureVids(stName.get())
        gotoHome()
    
    def gotoHome():
        window.destroy()
        putMainWindow()
    
    
    button1 = tk.Button(text='Create Student Record', command=captureImage).place(x=230,y=180)
    
    LabelInfo2 = tk.Label(window,text="Please note that video will open when the button is pressed").place(x=40,y=220);
    LabelInfo3 = tk.Label(window,text="Please press 'A' when the student is ready").place(x=40,y=240);
    
    button2 = tk.Button(text='Home',command = gotoHome).place(x=30,y=260)

    window.mainloop()
def deleteTrained():
    print("Deleted Data")
    os.remove('./class/classifier.pkl')
    os.remove('./attendance/Attendance.xlsx')
    shutil.rmtree('./aligned_img')
    print("Made necessary folder")
    os.makedirs('./aligned_img')

def training():
    preprocess()
    trainin()
    insert_attendance(os.listdir('./train_img'))
def recognize():
    name = face_recognition.perform()
    mark_attendance(name)
def close():
    close_attendance()
def putMainWindow():
    window1 = Tk()
    window1.geometry("600x500")
    #window.configure(background='')
    window1.title("Attendance System")
    #window.geometry("800x500")
    tk.Label(window1, text = "Attendance Software").pack()
    
    LabelInfo = tk.Label(window1,text="Action to be performed").place(x=30,y=40)

    def gotoCreate():
        window1.destroy()
        putCreateWindow()
    
    button1 = tk.Button(text='Create a record', command=gotoCreate).place(x=30,y=70)
    
    button2 = tk.Button(text='Train Collected Models', command=training).place(x=30,y=110)

    button3 = tk.Button(text='Delete Trained Data',command=deleteTrained).place(x=30,y=150)

    button4 = tk.Button(text="Perform Attendance",command=recognize).place(x=30,y=190)

    button5 = tk.Button(text="Close Attendance",command=close).place(x=30,y=230)


    window1.mainloop()



if __name__ == "__main__":
    putMainWindow()
