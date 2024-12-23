import tkinter as tk
from PasswordGenerator import PasswordGenerator
import textwrap

pwGenerator = PasswordGenerator()
pwLength = 1
userList = []
charsAvailable = []
password = ""

# Funzione per aggiornare il valore della label
def setPwLength(value):
    global pwLength
    pwLength = value
    valueLabel.config(text=f"Lunghezza: {pwLength}")

# Funzione per aggiornare le scelte di caratteri dell'utente
def setUserList():
    global userList
    userList = []
    # Controlla lo stato delle checkbox e aggiorna la lista
    if lowercaseVar.get():  # Checkbox "Minuscole" selezionata
        if 1 not in userList:
            userList.append(1)
    else:  # Checkbox "Minuscole" deselezionata
        if 1 in userList:
            userList.remove(1)
    
    if uppercaseVar.get():  # Checkbox "Maiuscole" selezionata
        if 2 not in userList:
            userList.append(2)
    else:  # Checkbox "Maiuscole" deselezionata
        if 2 in userList:
            userList.remove(2)
    
    if digitsVar.get():  # Checkbox "Cifre" selezionata
        if 3 not in userList:
            userList.append(3)
    else:  # Checkbox "Cifre" deselezionata
        if 3 in userList:
            userList.remove(3)
    
    if specialCharsVar.get():  # Checkbox "Caratteri speciali" selezionata
        if 4 not in userList:
            userList.append(4)
    else:  # Checkbox "Caratteri speciali" deselezionata
        if 4 in userList:
            userList.remove(4)   

def generatePw():
    if not userList:
        pwLabel.config(text="Errore: nessun tipo di carattere selezionato")

    charsAvailable = pwGenerator.buildCharsAvailable(userList)
    
    password = pwGenerator.buildPassword(int(pwLength), charsAvailable)
    wrappedPw = "\n".join(textwrap.wrap(password, width=40))
    pwLabel.config(text=wrappedPw)

    entropy = pwGenerator.pwStrength(password)
    description = pwGenerator.calcViolation(entropy)
    wrappedDesc = "\n".join(textwrap.wrap(description, width=70))
    descLabel.config(text=f"Entropia: {entropy:.3f}\n{wrappedDesc}")

# Dimensioni e colori base della finestra
windowWidth = 600
windowHeight = 500
bgColor = "#1E1E1E"  # Colore di sfondo principale
txtColor = "#DDDDDD" # Colore del testo

# Creazione della finestra principale
window = tk.Tk()
window.title("Random Password Generator")  # Titolo della finestra
window.geometry(f"{windowWidth}x{windowHeight}")  # Imposta le dimensioni della finestra
window.configure(background=bgColor)  # Imposta il colore di sfondo

# Creazione del titolo
title = tk.Label(
    window,
    text="Random Password Generator",
    font=("Arial", 20, "bold"),  # Font personalizzato
    foreground=txtColor,  # Colore del testo
    background=bgColor    # Colore di sfondo
)
title.pack(pady=20)  # Spaziatura verticale del titolo

# Creazione di un frame per le checkbox
checkbox_frame = tk.Frame(
    window,
    background=bgColor  # Sfondo del frame
)
checkbox_frame.pack(pady=10)  # Spaziatura verticale del frame

lowercaseVar = tk.IntVar()
uppercaseVar = tk.IntVar()
digitsVar = tk.IntVar()
specialCharsVar = tk.IntVar()

# Checkbox all'interno del frame
lowercaseCheck = tk.Checkbutton(
    checkbox_frame,
    text="Minuscole",  # Testo della checkbox
    bg=bgColor,        # Colore di sfondo
    fg=txtColor,       # Colore del testo
    selectcolor=bgColor, # Colore della casella selezionata
    variable=lowercaseVar,
    command=setUserList
)
uppercaseCheck = tk.Checkbutton(
    checkbox_frame,
    text="Maiuscole",
    bg=bgColor,
    fg=txtColor,
    selectcolor=bgColor,
    variable=uppercaseVar,
    command=setUserList
)
digitsCheck = tk.Checkbutton(
    checkbox_frame,
    text="Cifre",
    bg=bgColor,
    fg=txtColor,
    selectcolor=bgColor,
    variable=digitsVar,
    command=setUserList
)
specialCharsCheck = tk.Checkbutton(
    checkbox_frame,
    text="Caratteri speciali",
    bg=bgColor,
    fg=txtColor,
    selectcolor=bgColor,
    variable=specialCharsVar,
    command=setUserList
)

# Posizionamento delle checkbox nel frame (layout grid)
lowercaseCheck.grid(row=0, column=0, padx=10, pady=0)  # Colonna 0
uppercaseCheck.grid(row=0, column=1, padx=10, pady=0)  # Colonna 1
digitsCheck.grid(row=0, column=2, padx=10, pady=0)     # Colonna 2
specialCharsCheck.grid(row=0, column=3, padx=10, pady=0)  # Colonna 3

# Label per mostrare il valore selezionato dallo slider
valueLabel = tk.Label(
    window,
    text=f"Lunghezza: {pwLength}", # Valore iniziale
    font=("Arial", 11),           # Font della label
    bg=bgColor,                   # Colore di sfondo
    fg="white"                    # Colore del testo
)
valueLabel.pack(pady=0)  # Spaziatura verticale della label

# Creazione dello slider (Scale)
pwLengthSlider = tk.Scale(
    window,
    from_=1,                # Valore minimo
    to=128,                 # Valore massimo
    orient="horizontal",    # Orientamento orizzontale
    length=300,             # Lunghezza dello slider
    troughcolor="white",   # Colore della barra sotto il cursore
    background=bgColor,     # Sfondo del controllo
    activebackground="black", # Sfondo del controllo quando selezionato
    highlightthickness=0,   # Rimuove il bordo
    sliderrelief="flat",    # Stile del cursore (piatto)
    showvalue=False,        # Nasconde il valore accanto allo slider
    sliderlength=20,        # Lunghezza del cursore
    width=10,                # Altezza della barra dello slider
    command=setPwLength
)
pwLengthSlider.pack(pady=10)  # Spaziatura verticale dello slider

# Label per mostrare la password generata
pwLabel = tk.Label(
    window,
    text=f"{password}...", # Valore iniziale
    font=("Arial", 14),           # Font della label
    bg=bgColor,                   # Colore di sfondo
    # bg='#2A2A2A',                   # Colore di sfondo
    foreground=txtColor                    # Colore del testo
)
pwLabel.pack(pady=15)  # Spaziatura verticale della label

# Creazione button per generare la password
generatePwBtn = tk.Button(
    window, 
    text="Genera Password",        # Testo del pulsante
    font=("Arial", 11),      # Font del testo
    background=txtColor,               # Colore di sfondo del pulsante
    foreground=bgColor,              # Colore del testo
    activebackground="white",
    command=generatePw
)
generatePwBtn.pack(pady=10)  # Posiziona il pulsante con spaziatura verticale

# Label per mostrare la password generata
descLabel = tk.Label(
    window,
    text="", # Valore iniziale
    font=("Arial", 11),           # Font della label
    bg=bgColor,                   # Colore di sfondo
    # bg='#2A2A2A',                   # Colore di sfondo
    foreground=txtColor                    # Colore del testo
)
descLabel.pack(pady=10)  # Spaziatura verticale della label

# Ciclo principale per mantenere la finestra attiva
window.mainloop()



''' TODO
    - PWLENGTH > 50 → INSERT \n
    - ↑ SAME FOR DESCRIPTION ↑
    - FIX COMMENTS
    - LIGHTER BG FOR LABELS [IDEA]
    - CHECKBOXES WITH SEPARATED LABELS [IDEA]
    - COPY BTN [IDEA]
'''