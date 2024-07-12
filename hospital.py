from tkinter import*
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import _mysql_connector

class Hospital:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1200x600")
        
        lbltitle = Label(self.root,bd=20,relief=RIDGE,text="HOSPITAL MANAGEMENT SYSTEM",fg="red",font=("times new roman",15,"bold"))
        lbltitle.pack(side=TOP,fill=X)

        #===================================================Dataframe=================================================
        Dataframe = Frame(self.root,bd=20,relief=RIDGE)
        Dataframe.place(x=0,y=130,width=1300,height=400)