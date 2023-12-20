import tkinter as tk
import random

class SorteadorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sorteador")

        # Adiciona um rótulo como título
        self.titulo = tk.Label(root, text="Sorteador de Objetos")
        self.titulo.pack(pady=10)

        self.lista_objetos = []
        self.objetos_entry = tk.Entry(root)
        self.objetos_entry.pack(pady=10)

        self.botao_adicionar = tk.Button(root, text="Adicionar Objeto", command=self.adicionar_objeto)
        self.botao_adicionar.pack()

        self.botao_sortear = tk.Button(root, text="Sortear", command=self.sortear)
        self.botao_sortear.pack()

        self.resultado = tk.Label(root, text="")
        self.resultado.pack(pady=10)

    def adicionar_objeto(self):
        objeto = self.objetos_entry.get()
        if objeto:
            self.lista_objetos.append(objeto)
            self.objetos_entry.delete(0, tk.END)

    def sortear(self):
        if self.lista_objetos:
            objeto_sorteado = random.choice(self.lista_objetos)
            self.resultado.config(text=f"Objeto sorteado: {objeto_sorteado}")
        else:
            self.resultado.config(text="Adicione objetos antes de sortear.")

if __name__ == "__main__":
    root = tk.Tk()
    app = SorteadorApp(root)
    root.mainloop()
