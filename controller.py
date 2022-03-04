from tkinter import Tk
from vista import *

class Controller:
    """
    Controller Class
    """

    def __init__(self, root) -> None:
        
        self.root_controler = root
        self.vision_activada()

    def vision_activada(self):
        """
        Activates the view
        """
        Vision(self.root_controler)

if __name__ == "__main__":
    root_tk = Tk()
    application = Controller(root_tk)
    root_tk.mainloop()