#import required modules
#create graphical user interfaces
import tkinter as tk
#allow displaying popup alerts
from tkinter import messagebox
from calculator_function import calculate
class CalculatorGUI:
    """"create a new defined class"""
    def __init__(self, root):
        #create root as main application window
        self.root = root
        #set the window title
        self.root.title("Scientific Calculator")
        #set the window size
        self.root.geometry("400x600")
        self.root.resizable(False, False)  
        
        #store the mathmatical expression entered by the user
        self.expression = ""
        
        #create a stringvar variable slinked to the user's input
        self.input_text = tk.StringVar()
        self.entry = tk.Entry(root, textvariable=self.input_text, font=("Arial", 20), justify="right", bd=10, relief=tk.GROOVE)
        self.entry.pack(padx=10, pady=10, fill="x")
        
        
        self.create_buttons()
    
    def create_buttons(self):
        '''Creating the calculator buttons'''
        #create digital buttons
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "π", "+"],
            ["sin", "cos", "tan", "sqrt"],
            ["arcsin", "arccos", "arctan", "^"],
            ["ln", "exp", "fact", "x^2"],
            ["C", "Del", "(", ")"],
            ["="]
        ]
        
        #Iterate through the button list, create a Frame for each row, and add buttons to it
        for row in buttons:
            #create a row container for each button
            frame = tk.Frame(self.root)
            frame.pack(expand=True, fill="both")
            for btn in row:
                #Bind click events for each button, call the onbuttonclick method
                button = tk.Button(frame, text=btn, font=("Arial", 15),
                                   command=lambda b=btn: self.on_button_click(b))
                button.pack(side="left", expand=True, fill="both", padx=2, pady=2)
    
    def on_button_click(self, btn):
        """Button click event handling function:
        - "=" Calculation result
        - "C" Clear input
        - "Del" deletes the last one
        - Other buttons are appended to the expression
        """
        if btn == "=":
            try:
                result = calculate(self.expression)
                self.input_text.set(str(result))
                self.expression = str(result)
            except Exception as e:
                messagebox.showerror("Error", "Invalid Expression")
                self.expression = ""
                self.input_text.set("")
        elif btn == "C":
            self.expression = ""
            self.input_text.set("")
        elif btn == "Del":
            self.expression = self.expression[:-1]
            self.input_text.set(self.expression)
        else:
            #Append button text to the current expression
            self.expression += btn
            self.input_text.set(self.expression)


if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorGUI(root)
    root.mainloop()