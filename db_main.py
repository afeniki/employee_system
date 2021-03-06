import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
from PIL import ImageTk, Image
import pymysql
import os
import shutil
import db_config

form = tk.Tk()
form.title("Database Form")
form.geometry("500x280")

tab_parent = ttk.Notebook(form)  #helps to set up(design and manage) tabs
tab1 = ttk.Frame(tab_parent)
tab2 = ttk.Frame(tab_parent)

tab_parent.add(tab1, text="All Records")
tab_parent.add(tab2, text="Add New Record")


firstLabelTabOne = tk.Label(tab1, text="First Name:")
familyLabelTabOne = tk.Label(tab1, text="Family Name:")
jobLabelTabOne = tk.Label(tab1, text="Job Title:")

firstEntryTabOne = tk.Entry(tab1)
familyEntryTabOne = tk.Entry(tab1)
jobEntryTabOne = tk.Entry(tab1)

imgLabelTabOne = tk.Label(tab1)

buttonForward = tk.Button(tab1, text="Forward")
buttonBack = tk.Button(tab1, text="Back")

#ADD WIDGETS TO GRID ON TAB
firstLabelTabOne.grid(row=0, column=0, padx=15, pady=15)
firstEntryTabOne.grid(row=0, column=1, padx=15, pady=15)

familyLabelTabOne.grid(row=1, column=0, padx=15, pady=15)
familyEntryTabOne.grid(row=1, column=1, padx=15, pady=15)

jobLabelTabOne.grid(row=2, column=0, padx=15, pady=15)
jobEntryTabOne.grid(row=2, column=1, padx=15, pady=15)

imgLabelTabOne.grid(row=0, column=2, rowspan=3, padx=15, pady=15)

#ADDING WIDGETS FOR TAB
tab_parent.pack(expand=1, fill="both")

form.mainloop()
