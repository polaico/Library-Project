from tkinter import *
from tkinter import ttk
from modelo import Crud
from tkinter import messagebox
from validaciones import Validaciones


class Vision:
    """
    This Class has all the code related with graphics
    """
    def __init__(self, master) -> None:
        
        self.consulta_modelo = Crud()
        """
        Object calling class Crud from model
        """
        
        self.consulta_valida = Validaciones()
        
        self.root = master
        self.root.title("Library Project")
        self.titulo = Label(master, text="Enter book data:", height=1, width=60)
        self.titulo.grid(row=0, column=1, columnspan=6, padx=5, pady=5, sticky=W+E)
    
        self.a_val = StringVar()
        self.titulo2 = Label(master, text="Title")
        self.titulo2.grid(row=2, column=3, padx=5, pady=5, sticky=E)
        self.e2 = Entry(master, textvariable=self.a_val)
        self.e2.grid(row=2, column=4, padx=5, pady=5, sticky=E)

        self.b_val = StringVar()
        self.ruta = Label(master, text="Author")
        self.ruta.grid(row=4, column=3, padx=5, pady=5, sticky=E)
        self.e3 = Entry(master, textvariable=self.b_val)
        self.e3.grid(row=4, column=4, padx=5, pady=5, sticky=E)

        self.c_val = StringVar()
        self.descripcion = Label(master, text="Publisher")
        self.descripcion.grid(row=6, column=3, padx=5, pady=5, sticky=E)
        self.e4 = Entry(master, textvariable=self.c_val)
        self.e4.grid(row=6, column=4, padx=5, pady=5, sticky=E)

        self.d_val = StringVar()
        self.descripcion2 = Label(master, text="Year")
        self.descripcion2.grid(row=8, column=3, padx=5, pady=5, sticky=E)
        self.e5 = Entry(master, textvariable=self.d_val)
        self.e5.grid(row=8, column=4, padx=5, pady=5, sticky=E)
        """
        Elements and their disposition on the GUI
        """

        self.b = Button(master, text="Add", foreground="black", background="lightgreen", 
        command=lambda: self.alta())
        self.b.grid(row=12, column=4, padx=10, pady=15, sticky=W)
        self.c = Button(master, text="Read", foreground="black", background="lightblue", 
        command=lambda: self.consulta_modelo.mostrar(self.tree))
        self.c.grid(row=12, column=5, padx=10, pady=15, sticky=W)
        self.d = Button(master, text="Update", foreground="black", background="gold", 
        command=lambda: self.cambiar())
        self.d.grid(row=2, column=5, padx=5, pady=5, sticky=W+E)
        self.e = Button(master, text="Delete", foreground="black", background="tomato", 
        command=lambda: self.baja())
        self.e.grid(row=4, column=5, padx=5, pady=5, sticky=W+E)
        self.f = Button(master, text="Clean", foreground="black", background="white", 
        command=lambda: self.limpiar())
        self.f.grid(row=6, column=5, padx=5, pady=5, sticky=W+E)
        """
        Buttons
        """


        self.tree = ttk.Treeview(master)
        self.tree["columns"] = ("col1", "col2", "col3", "col4")
        self.tree.column("#0", width=40, minwidth=40, anchor=W)
        self.tree.column("col1", width=130, minwidth=130)
        self.tree.column("col2", width=80, minwidth=80)
        self.tree.column("col3", width=85, minwidth=85)
        self.tree.column("col4", width=60, minwidth=60)
        self.tree.heading("#1",text="Title")
        self.tree.heading("#2", text="Author")
        self.tree.heading("#3", text="Publisher")
        self.tree.heading("#4", text="Year")
        self.tree.grid(row=14, column=2, columnspan=4)
        self.tree.bind("<ButtonRelease-1>", self.seleccionar_fila)
        """
        Treeview
        """



    def alta(self):
        """
        Calls agregar function from modelo.py
        """
        self.consulta_modelo.agregar(self.a_val, self.b_val, self.c_val, self.d_val, self.tree)
        
        if self.consulta_valida.val_alfanum(self.a_val.get(), self.b_val.get(), self.c_val.get()) and self.consulta_valida.val_num(self.d_val.get()):
            self.a_val.set('')
            self.b_val.set('')
            self.c_val.set('')
            self.d_val.set('')
    
    
    

    def baja(self):
        """
        Calls borrar function from modelo.py
        """
        self.consulta_modelo.borrar(self.a_val, self.b_val, self.c_val, self.d_val, self.tree)
        
        self.a_val.set('')
        self.b_val.set('')
        self.c_val.set('')
        self.d_val.set('')
    

    def cambiar(self):
        """
        Calls modificar function from modelo.py
        """
        self.consulta_modelo.modificar(self.a_val, self.b_val, self.c_val, self.d_val, self.tree)
        
        self.a_val.set('')
        self.b_val.set('')
        self.c_val.set('')
        self.d_val.set('')
       

    def seleccionar_fila(self, a):
       """
       Allows to select entries from the treeview and shows its data on the fields
       """
       item_a = self.tree.focus()
       data = self.tree.item(item_a)
       titulo, autor, editorial, año = data["values"]
       self.id = data["text"]
       self.e2.delete('0', END)
       self.e2.insert(0, titulo)
       self.e3.delete('0', END)
       self.e3.insert(0, autor)
       self.e4.delete('0', END)
       self.e4.insert(0, editorial)
       self.e5.delete('0', END)
       self.e5.insert(0, año)
       

    def limpiar(self):
        """
        Cleans the fields
        """
        self.a_val.set('')
        self.b_val.set('')
        self.c_val.set('')
        self.d_val.set('')
        