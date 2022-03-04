from __future__ import unicode_literals
from turtle import title
from peewee import *
from validaciones import Validaciones
from tkinter import messagebox
from datetime import datetime

db = SqliteDatabase('library.db')                           
    
class BaseModel(Model):  
                                        
    class Meta:					       
        database = db						
																	
    
class Biblioteca(BaseModel):
    
    title = CharField(unique=True)
    author = CharField()
    publisher = CharField()
    year = CharField()
     	
db.connect()
db.create_tables([Biblioteca])

consulta_valida = Validaciones()


def decorador_alta(function):
    """
    Decorator for alta function from Crud. Generates a log .txt
    """
    def envoltura(*arg, **kargs):
        titulo = arg[1].get()
        autor = arg[2].get()
        editorial = arg[3].get()
        año = arg[4].get()
        now = datetime.now()
        date = now.strftime("%d/%m/%Y, %H:%M:%S")
        valid_1 = consulta_valida.val_alfanum(titulo, autor, editorial)
        valid_2 = consulta_valida.val_num(año)
        if valid_1 and valid_2:
        
            file = open("log_entries", "a")
            file.write(date + "\n")
            file.write("Title: " + titulo + "\n")
            file.write("Author: " + autor + "\n")
            file.write("Publisher: " + editorial + "\n")
            file.write("Year: " + año + "\n")
            file.write("---" * 20 + "\n")
            file.close()

        return function (*arg, **kargs)
        
    return envoltura

def decorador_modif(function):
    """
    Decorator for modificar function from Crud. Generates a log .txt
    """
    def envoltura(*arg, **kargs):
        titulo = arg[1].get()
        autor = arg[2].get()
        editorial = arg[3].get()
        año = arg[4].get()
        now = datetime.now()
        date = now.strftime("%d/%m/%Y, %H:%M:%S")
        valid_1 = consulta_valida.val_alfanum(titulo, autor, editorial)
        valid_2 = consulta_valida.val_num(año)

        if valid_1 and valid_2:
            file = open("log_updates", "a")
            file.write(date + "\n")
            file.write("Title: " + titulo + "\n")
            file.write("Author: " + autor + "\n")
            file.write("Publisher: " + editorial + "\n")
            file.write("Year: " + año + "\n")
            file.write("---" * 20 + "\n")
            file.close()

        return function (*arg, **kargs)

    return envoltura

def decorador_baja(function):
    """
    Decorator for borrar function from Crud. Generates a log .txt
    """
    def envoltura(*arg, **kargs):
        titulo = arg[1].get()
        autor = arg[2].get()
        editorial = arg[3].get()
        año = arg[4].get()
        now = datetime.now()
        date = now.strftime("%d/%m/%Y, %H:%M:%S")
        valid_1 = consulta_valida.val_alfanum(titulo, autor, editorial)
        valid_2 = consulta_valida.val_num(año)

        if valid_1 and valid_2:
            file = open("log_deletes", "a")
            file.write(date + "\n")
            file.write("Title: " + titulo + "\n")
            file.write("Author: " + autor + "\n")
            file.write("Publisher: " + editorial + "\n")
            file.write("Year: " + año + "\n")
            file.write("---" * 20 + "\n")
            file.close()

        return function (*arg, **kargs)

    return envoltura

class Crud:
    """
    This class has all the code related with the database
    """
    
    def __init__(self) -> None:
        
        self.consulta_valida = Validaciones()

         

    def mostrar(self, tree):
        """
        Shows the data from the database on the treeview
        """
        registros = tree.get_children()
        for elemento in registros:
            tree.delete(elemento)

        for fila in Biblioteca.select():
            tree.insert('', 0, text=fila.id, values=(fila.title, fila.author, fila.publisher, fila.year))

    @decorador_alta
    def agregar(self, titulo, autor, editorial, año, tree):
        """
        Adds new entries to the database, following validation rules from validaciones.py
        """
        valid_1 = self.consulta_valida.val_alfanum(titulo.get(), autor.get(), editorial.get())
        valid_2 = self.consulta_valida.val_num(año.get())
        try:
            if valid_1 and valid_2:
                biblioteca = Biblioteca()
                biblioteca.title = titulo.get()
                biblioteca.author = autor.get()
                biblioteca.publisher = editorial.get()
                biblioteca.year = año.get()
                biblioteca.save()
            
                self.mostrar(tree)
                messagebox.showinfo(message="The new entry has been successfully added"
                                     , title="New Entry")
                
                
                
            else:
                if not self.consulta_valida.val_alfanum(titulo.get(), autor.get(), editorial.get()):
                    messagebox.showerror(message="Wrong characters. Only use alphanumeric characters for the Title, Author and Publisher fields"
                                     , title="Validation Error")
                else:
                    messagebox.showerror(message="Wrong characters. Enter 4 numbers for the Year field"
                                     , title="Validation Error")
        
        except IntegrityError:
            #print("Probando")
            messagebox.showerror(message="This book has already been entered in the database"
                                     , title="Duplicate Error")
        
       
        
                  
    @decorador_baja    
    def borrar(self, titulo, autor, editorial, año, tree):
        """
        Deletes entries from the database
        """
        item_seleccionado = tree.focus()
        valor_id = tree.item(item_seleccionado)

        respuesta = messagebox.askokcancel(message="¿Are you sure you want to delete the selected entry?", title="Delete Entry")
        if respuesta == True:
            borrar = Biblioteca.get(Biblioteca.id == valor_id["text"])
            borrar.delete_instance()
            messagebox.showinfo(message="The entry has been deleted"
                                     , title="Entry Deleted")
            self.mostrar(tree)
       
    @decorador_modif
    def modificar(self, titulo, autor, editorial, ano, tree):
        """
        Updates entries
        """
        
        item_seleccionado = tree.focus()
        valor_id = tree.item(item_seleccionado)
       
        if self.consulta_valida.val_alfanum(titulo.get(), autor.get(), editorial.get()) and self.consulta_valida.val_num(ano.get()):
            actualizar = Biblioteca.update(title=titulo.get(), author=autor.get(), publisher=editorial.get(), year=ano.get()).where(Biblioteca.id == valor_id["text"])
            actualizar.execute()
            self.mostrar(tree)
            messagebox.showinfo(message="Entry succesfully updated"
                                     , title="Entry Updated")
        else:
            
            if not self.consulta_valida.val_alfanum(titulo.get(), autor.get(), editorial.get()):
                    messagebox.showerror(message="Wrong characters. Only use alphanumeric characters for the Title, Author and Publisher fields"
                                     , title="Validation Error")
            else:
                messagebox.showerror(message="Wrong characters. Enter 4 numbers for the Year field"
                                     , title="Validation Error")