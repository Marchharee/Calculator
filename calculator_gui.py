
#import required modules
#create graphical user interfaces
import tkinter as tk
#allow displaying popup alerts
from tkinter import messagebox
#import math(a built-in library for mathematical functions)
import math


class Calculator:
   """"create a new defined class"""
    
   def __init__(self, root):
        """initialize the calculator"""
        #create root as main application window
        self.root = root
        #set the window title
        self.root.title("Classic Calculator")
        #set the window size
        self.root.geometry("400x600")
        #store the mathmatical expression entered by the user
        self.expression = ""
        #create a stringvar variable slinked to the user's input
        self.input_text = tk.StringVar()
        #create the input field and buttons
        self.create_widgets()