import tkinter as tk
import random
import sys
import pyperclip
#-------------------------------------------
password = ""
tuples = []
#TUPLES
lowercase = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
             "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")

capital_letters = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
                   "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")

special = ("!", "@", "#", "$", "%", "^", "&", "*", "_", "-", "+", "=", "|",
           "\\", "~", "`", ";", ":", "'", '"', "<", ">", ",", ".", "?", "/")

Special_ISO8859 = (
    "¡", "¢", "£", "¤", "¥", "¦", "§", "¨", "©", "ª", "«", "¬", "-", "®", "¯", "°",
    "±", "²", "³", "´", "µ", "¶", "·", "¸", "¹", "º", "»", "¼", "½", "¾", "¿", "À",
    "Á", "Â", "Ã", "Ä", "Å", "Æ", "Ç", "È", "É", "Ê", "Ë", "Ì", "Í", "Î", "Ï", "Ð",
    "Ñ", "Ò", "Ó", "Ô", "Õ", "Ö", "×", "Ø", "Ù", "Ú", "Û", "Ü", "Ý", "Þ", "ß", "à",
    "á", "â", "ã", "ä", "å", "æ", "ç", "è", "é", "ê", "ë", "ì", "í", "î", "ï", "ð",
    "ñ", "ò", "ó", "ô", "õ", "ö", "÷", "ø", "ù", "ú", "û", "ü", "ý", "þ", "ÿ")

numbers = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
parenthesis = ('(', ')', '[', ']', '{', '}')
minus = "-"
underscore = "_"
space = " "
#-------------------------------------------
#WINDOW CONFIGURATION/STYLE
root = tk.Tk()
root.title("PasswordGenerator") #Title
root.geometry("370x270") #Size
root.configure(bg="#1e1e1e")  # Dark background
root.attributes("-alpha", 0.9) #Transparency
#-------------------------------------------
# Password Generator
def password_generator(password, tuples):
    for i in range(int(length_txt.get())):
        password += random.choice(tuples)
    return password

def change_length_block(password):
    length_block.config(state="normal") #Unlock TexBox
    length_block.config(width= int(length_txt.get()) + (3)) #length of Texbox
    length_block.delete(0, tk.END) #Clear TexBox
    length_block.insert(0, password) #Insert Password
    length_block.config(state="readonly", fg="black") #Block TexBox

#random Tuple generator
def random_tuple(tuples):
    tuples.clear()
    if lowercase_var.get():
        tuples.extend(lowercase)
    if capital_letters_var.get():
        tuples.extend(capital_letters)
    if numbers_var.get():
        tuples.extend(numbers)
    if special_var.get():
        tuples.extend(special)
    if ISO8859_var.get():
        tuples.extend(Special_ISO8859)
    if parenthesis_var.get():
        tuples.extend(parenthesis)
    if minus_var.get():
        tuples.extend(minus)
    if underscore_var.get():
        tuples.extend(underscore)
    if space_var.get():
        tuples.extend(space)
        
def clipboard():
    pyperclip.copy(length_block.get())
    
def check_config(password, tuples):
    random_tuple(tuples)
    password = password_generator(password, tuples)
    change_length_block(password)
#-------------------------------------------
# CHECK BOX STYLE
check_style = {
    "bg": "#1e1e1e",
    "fg": "#bbbbbb",
    "selectcolor": "#444444",
    "activebackground": "#1e1e1e",
    "activeforeground": "#ffffff",
    "relief": tk.FLAT
}
# CHECK BOX STATUS(ON/OFF)
lowercase_var = tk.IntVar(value=1)
capital_letters_var = tk.IntVar(value=1)
numbers_var = tk.IntVar(value=1)
special_var = tk.IntVar(value=1)
ISO8859_var = tk.IntVar(value=1)
parenthesis_var = tk.IntVar(value=1)
minus_var = tk.BooleanVar()
underscore_var = tk.BooleanVar()
space_var = tk.IntVar(value=1)
# CHECK BOX
lowercase_check = tk.Checkbutton(root, text="abcdef...vwxy", variable=lowercase_var, **check_style)
capital_letters_check = tk.Checkbutton(root, text="ABCDEF...VWXY", variable=capital_letters_var, **check_style)
numbers_check = tk.Checkbutton(root, text="0123456789", variable=numbers_var, **check_style)
special_check = tk.Checkbutton(root, text="!@#$%^,.:?/", variable=special_var, **check_style)
ISO8859_check = tk.Checkbutton(root, text="¡¢£¤¥¦....üýþÿ", variable=ISO8859_var, **check_style)
parenthesis_check = tk.Checkbutton(root, text="()[]{}", variable=parenthesis_var, **check_style)
minus_check = tk.Checkbutton(root, text="-", variable=minus_var, **check_style)
underscore_check = tk.Checkbutton(root, text="_", variable=underscore_var, **check_style)
space_check = tk.Checkbutton(root, text=" (space)", variable=space_var, **check_style)
#-------------------------------------------
# BUTTON STYLE
bnt_style = {
    "bg": "#444444",
    "fg": "#ffffff",
    "relief": tk.FLAT
}
# BUTTON
bnt_start = tk.Button(root, text="Create", command=lambda: check_config(password, tuples), **bnt_style)
bnt_test = tk.Button(root, text="COPY", command=clipboard, **bnt_style)
#-------------------------------------------
# LABEL STYLE
label_style = {
    "bg": "#1e1e1e",  # Dark background
    "fg": "#bbbbbb",  # Light gray text
    "font": ("Arial", 12),  # Font
    "relief": tk.FLAT  # Flat border
}
#LABEL
text_label = tk.Label(root, text="Select u config", **label_style)
length_label = tk.Label(root, text="Length of the password", **label_style)
#-------------------------------------------
#TEX BOX STYLE
entry_style = {
    "bg": "#1e1e1e",
    "fg": "#bbbbbb",
    "width": 3,
    "relief": tk.FLAT,
    "highlightbackground": "#444444",
    "highlightthickness": 1 
}
# Texbox for length
length_txt = tk.Entry(root, **entry_style)
length_txt.insert(0, 30)
# Texbox for copy
length_block = tk.Entry(root, **entry_style)
length_block.config(state="readonly") #Block, Only read
#-------------------------------------------
# List of Widgets with values of padx, pady and column (widget, padx, pady, column)
# Tuple of Widgets for first column
column1_widgets = [
    (text_label, 10, 0, 0),(lowercase_check, 10, 0, 0), (capital_letters_check, 10, 0, 0), (numbers_check, 10, 0, 0),
    (special_check, 10, 0, 0), (ISO8859_check, 10, 0, 0), (parenthesis_check, 10, 0, 0),
    (minus_check, 10, 0, 0), (underscore_check, 10, 0, 0), (space_check, 10, 0, 0)
]

# Tuple of Widgets for second column
column2_widgets = [
    (length_label, 10, 2, 1), (length_txt, 10, 2, 1), (length_block, 10, 2 ,1),
    (bnt_start, 10, 2, 1), (bnt_test, 10, 2, 1)
]

# Variable for the auto increment of row
row_index = 0

# Configuration of the GRID for widgets of first column
for widget, padx_value, pady_value, column_value in column1_widgets:
    widget.grid(row=row_index, column=column_value, sticky='w', padx=padx_value, pady=pady_value)
    row_index += 1  # Autoincrement of index row

# Restart of index of row for second column
row_index = 0

# Configuration of the GRID for widgets of second column
for widget, padx_value, pady_value, column_value in column2_widgets:
    widget.grid(row=row_index, column=column_value, sticky='w', padx=padx_value, pady=pady_value)
    row_index += 1  # Autoincrement of index row

root.mainloop()



