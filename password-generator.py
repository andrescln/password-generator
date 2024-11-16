import random

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

password = ""
tuplas = []

print("Choose the words: 'Y' / 'N'")
select_lowercase = str(input("abcdef...vwxy: : ")).upper()
select_capital_letters = str(input("ABCDEF...VWXY: : ")).upper()
select_numbers = str(input("0123456789: ")).upper()
select_special = str(input("!@#$%^,.:?/: ")).upper()
select_ISO8859 = str(input("¡¢£¤¥¦....üýþÿ: ")).upper()
select_parenthesis = str(input("()[]{}: ")).upper()
select_minus = str(input("-: ")).upper()
select_underscore = str(input("_: ")).upper()
select_space = str(input(" : ")).upper()

if select_lowercase == 'Y':
    tuplas.append(lowercase)
    
if select_capital_letters == 'Y':
    tuplas.append(capital_letters)
    
if select_numbers == 'Y':
    tuplas.append(numbers)
    
if select_special == 'Y':
    tuplas.append(special)
    
if select_ISO8859 == 'Y':
    tuplas.append(Special_ISO8859)
    
if select_parenthesis == 'Y':
    tuplas.append(parenthesis)
    
if select_minus == 'Y':
    tuplas.append(minus)
    
if select_underscore == 'Y':
    tuplas.append(underscore)
    
if select_space == 'Y':
    tuplas.append(space)
    


length = int(input("Length of the password: "))

for i in range(length):
    password += random.choice(random.choice(tuplas))
print(password)

