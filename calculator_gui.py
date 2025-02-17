
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
        
   def create_widgets(self):
        """create the input field and buttons for the calculator"""
        #create the entry field 
        entry_frame = tk.Frame(self.root)
        #allow the frame to fill width and height
        entry_frame.pack(expand=True, fill="both")
        #create a input box and set the font size set the border width
        entry = tk.Entry(entry_frame, font=("Arial", 20), textvariable=self.input_text, justify="right", bd=10, relief=tk.GROOVE)
        entry.pack(expand=True, fill="both")
        #create the button box
        button_frame = tk.Frame(self.root)
        button_frame.pack(expand=True, fill="both")
        #create digital buttons
        buttons = [
            ("7", "8", "9", "/"),
            ("4", "5", "6", "*"),
            ("1", "2", "3", "-"),
            ("0", ".", "=", "+"),
        ]
        #create calculate buttons
        sci_buttons = [
            ("sin", "cos", "tan", "√"),
            ("asin", "acos", "atan", "x²"),
            ("C", "(", ")", "Del"),
        ]