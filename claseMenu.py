import os
class Menu:
    __opciones = []

    def __init__(self,opciones=[]):
        self.__opciones = opciones
  
    def define_menu(self,opciones):
        self.__opciones = opciones
  
    def selectOption(self):
        try:
            op = int(input('--> '))
            if op > len(self.__opciones) or op < 0:
                input('Opcion invalida, reintente')
                op = None
            
        except ValueError:
            input('Error: Opcion invalida, debe ingresar un numero entero.')
            op = None
        return op
    
    def showMenu(self):
        os.system('cls')
        print('#-----MENU-----#')
        for opcion in self.__opciones:
            print(opcion)





               
