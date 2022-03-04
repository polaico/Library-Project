import re

class Validaciones:
    
    def __init__(self) -> None:
        pass

    def val_alfanum(self, cadena, autor, editorial):
        """
        Alphanumeric validatons for the Title, Author and Publisher fields
        """
        valid = "^[\w\s]+$"
        return re.match(valid, (cadena)) and re.match(valid, autor) and re.match(valid, editorial)
    
    def val_num(self, cadena):
        """
        Numeric validations for Year field.
        """
        valid2 = "^[0-9]{4}$"
        return re.match(valid2, (cadena))