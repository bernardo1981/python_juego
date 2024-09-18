import tkinter as tk
import random

class AdivinaElNumero:
    def __init__(self, master):
        self.master = master
        self.master.title("Adivina el Número")
        
        self.intento = 0
        self.numero_secreto = random.randint(1, 100)

        self.label = tk.Label(master, text="Adivina un número entre 1 y 100:")
        self.label.pack()

        self.entrada = tk.Entry(master)
        self.entrada.pack()

        self.boton = tk.Button(master, text="Enviar", command=self.adivinar)
        self.boton.pack()

        self.resultado = tk.Label(master, text="")
        self.resultado.pack()

    def adivinar(self):
        try:
            guess = int(self.entrada.get())
            self.intento += 1
            
            if guess < self.numero_secreto:
                self.resultado.config(text="Demasiado bajo, intenta otra vez.")
            elif guess > self.numero_secreto:
                self.resultado.config(text="Demasiado alto, intenta otra vez.")
            else:
                self.resultado.config(text=f"¡Correcto! Adivinaste en {self.intento} intentos.")
        except ValueError:
            self.resultado.config(text="Por favor, ingresa un número válido.")
        
        self.entrada.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    juego = AdivinaElNumero(root)
    root.mainloop()
