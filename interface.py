import os
import math

import tkinter as tk
from tkinter import *

filesScreen = 3
global counter
counter = 0

def listFiles():
  first = 0
  second = 1
  third = 2

  print(os.listdir("/Users/cesar/Code/CDJ"))

  for page in range(math.ceil(len(os.listdir("/Users/cesar/Code/CDJ"))/filesScreen)):
    print(os.listdir("/Users/cesar/Code/CDJ")[first])
    print(os.listdir("/Users/cesar/Code/CDJ")[second])
    print(os.listdir("/Users/cesar/Code/CDJ")[third])

    first += filesScreen
    second += filesScreen
    third += filesScreen

    print("\n")

def Widgets():
  #row 1: input label
  link_label = Label(
    root, 
    text = "Selecione a música", 
    font = ("Arial", 25, "bold"), 
    bg = "#010509", 
    fg = "#fff")
  link_label.grid(
    row = 1, 
    column = 1, 
    pady = 5, 
    padx = 5) 
  
  upButton = Button(
    root, 
    text = "<", 
    cursor = "hand2", 
    highlightthickness = 0, 
    borderwidth = 0, 
    command = Deacrease,
    width = 5, 
    height = 11,
    font = ("Arial", 25, "bold"), 
    bg = "#010509", 
    fg = "#fff") 
  upButton.place(
    x = 930,
    y = 0) 
  
  downButton = Button(
    root, 
    text = ">", 
    cursor = "hand2", 
    highlightthickness = 0, 
    borderwidth = 0, 
    command = Increase,
    width = 5, 
    height = 11,
    font = ("Arial", 25, "bold"), 
    bg = "#010509", 
    fg = "#fff") 
  downButton.place(
    x = 930,
    y = 300) 
   

def Increase():
  global counter
  if counter < math.ceil(len(os.listdir("/Users/cesar/Code/CDJ"))/filesScreen):
    counter += 1
  print(counter)

def Deacrease():
  global counter
  if counter > 0:
    counter -= 1
  print(counter)

  
root = tk.Tk()

root.geometry("1024x600") 
root.resizable(False, False) 
root.title("CDJ") 
root.config(background="#010509") 
    
   
video_Link = StringVar() 
download_Path = StringVar() 
resolution = StringVar()
setResolution = StringVar()
   
   
Widgets() 
   
root.mainloop() 