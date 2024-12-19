import tkinter as tk

windowWidth = 600
windowHeight = 400
bgColor = "#1E1E1E"
txtColor = "#DDDDDD"

# Creazione della finestra principale
window = tk.Tk()
window.title("Random Password Generator")
window.geometry(f"{windowWidth}x{windowHeight}")
window.configure(background=bgColor)

# Titolo
title = tk.Label(
    window,
    text = "Random Password Generator",
    font = ("Arial", 20, "bold"),
    foreground = txtColor,
    background = bgColor
)
title.pack(pady=20)

# Creazione di un frame per le checkbox
checkbox_frame = tk.Frame(
    window, 
    background = bgColor
)
checkbox_frame.pack(pady=10)

# Checkbox all'interno del frame
lowercaseCheck = tk.Checkbutton(
    checkbox_frame, 
    text = "Minuscole", 
    bg = bgColor, 
    fg = txtColor, 
    selectcolor = bgColor
    
)
uppercaseCheck = tk.Checkbutton(
    checkbox_frame, 
    text = "Maiuscole", 
    bg = bgColor, 
    fg = txtColor, 
    selectcolor = bgColor
)
digitsCheck = tk.Checkbutton(
    checkbox_frame, 
    text = "Cifre", 
    bg = bgColor, 
    fg = txtColor, 
    selectcolor = bgColor
)
specialCharsCheck = tk.Checkbutton(
    checkbox_frame, 
    text = "Caratteri speciali", 
    bg = bgColor, 
    fg = txtColor, 
    selectcolor = bgColor
)

# Disposizione delle checkbox con grid nel frame
lowercaseCheck.grid(row = 0, column = 0, padx = 10, pady = 0)
uppercaseCheck.grid(row = 0, column = 1, padx = 10, pady = 0)
digitsCheck.grid(row = 0, column = 2, padx = 10, pady = 0)
specialCharsCheck.grid(row = 0, column = 3, padx = 10, pady = 0)

# Label per mostrare il valore selezionato
label_valore = tk.Label(
    window,
    text="Valore selezionato: 0",  # Valore iniziale
    font=("Arial", 14),
    bg="#1E1E1E",
    fg="white"
)
label_valore.pack(pady=10)

# Creazione dello slider
pwLength = tk.Scale(
    window, 
    from_ = 1,          # Valore minimo
    to = 128,           # Valore massimo
    orient="horizontal",  # Orientamento: "horizontal" o "vertical"
    length=300,       # Lunghezza dello slider
    troughcolor=txtColor,   # Colore della "trough" (barra dello slider)    
    background=txtColor,    # Colore sfondo slider
    foreground=txtColor,
    highlightthickness=0,
    sliderrelief="ridge",
    showvalue=False
)
pwLength.pack(pady=10)

# Ciclo principale
window.mainloop()



''' TODO
    - SLIDER [WIP]
    - CHECKBOXES WITH SEPARATED LABELS [IDEA]
    - PW LABEL
    - GEN BTN
    - COPY BTN
    - COMP + STRENGTH LABEL
'''