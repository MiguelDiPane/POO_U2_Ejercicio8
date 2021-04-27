class Conjunto:
    #Atributos
    __elem = [] #inicializo como el conjunto vacio

    #Metodos
    def __init__(self, elementos = []):
        lista = []
        if type(elementos) == list:
            for i in range(len(elementos)):
                if type(elementos[i]) != int:
                    if type(elementos[i]) == str and elementos[i].isdigit():
                        elementos[i] = int(elementos[i])
                        lista.append(elementos[i])
                    else:
                        print('El elemento {} no es entero, se omite su carga.'.format(i+1))
                else:
                    lista.append(elementos[i])
        else:
            print('Error: El conjunto debe cargarse como una lista de enteros.')
        
        #Elimino elementos repetidos antes de cargar la lista
        #Los conjuntos no pueden tener elementos repetidos
        result = self.__eliminarRepetidos(lista)
        self.__elem = result
    
    def muestra(self):
        print(self.__elem)

    def getComp(self):
        return self.__elem
    
    def __eliminarRepetidos(self,lista):
        result = []
        for elemento in lista:
            if elemento not in result:
                result.append(elemento)
        return result      

    #Sobrecarga de operadores
    #Suma -> union
    '''la unión de dos onjuntos es una operación que resulta en otro conjunto,
    cuyos elementos son los mismos de los conjuntos iniciales.'''
    def __add__(self,otro):
        if type(otro) == Conjunto:
            conj1 = self.getComp()
            conj2 = otro.getComp()
            conj1.extend(conj2) 
            #Elimino elementos repetidos
            result = self.__eliminarRepetidos(conj1)
            return Conjunto(result)
        else:
            print('Error: Se necesitan dos conjuntos para realizar la UNION.')
            return []
    
    #Diferencia
    '''Sean A y B  dos conjuntos cualesquiera. 
    El conjunto diferencia de A y B , que se representa por A-B, 
    es el conjunto formado por todos los elementos que están en A, pero no están en B.'''
    def __sub__(self,otro):
        if type(otro) == Conjunto:
            conj1 = self.getComp()
            conj2 = otro.getComp()
            conj3 = [elem for elem in conj1 if elem not in conj2] 
            return Conjunto(conj3)
        else:
            print('Error: Se necesitan dos conjuntos para realizar la DIFERENCIA.')
            return []
    
    #Igualdad
    '''dos conjuntos se consideran iguales si tienen la misma cantidad
    de elementos y sus valores son iguales (sin importar el orden de los elementos)'''
    def __eq__(self,otro):
        igualdad = False
        if type(otro) == Conjunto:
            conj1 = self.getComp()
            conj2 = otro.getComp()
            if len(conj1) == len(conj2): #verifico que tengan igual cantidad de elementos
                #Ordeno listas para comprar
                conj1.sort()
                conj2.sort()
                if conj1 == conj2:
                    igualdad = True
        else:
            print('Error: Se necesitan dos conjuntos para realizar la Igualdad.')
        return igualdad

    