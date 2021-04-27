from claseMenu import Menu
from claseConjunto import Conjunto

def test():
    print('Carga de conjunto con elementos de tipo cadena (no digito), boleano y flotante')
    lista = [1,'2f',1,True,5,3.5]
    print(lista)
    conjP1 = Conjunto(lista)
    print('Conjunto: ',end = '')
    conjP1.muestra()
    print('Carga de dato que no es de tipo lista')
    entero = 15
    print(entero)
    conjP2 = Conjunto(entero)
    print('Conjunto: ',end = '')
    conjP2.muestra()

if __name__ == '__main__':
    miMenu = Menu()
    miMenu.define_menu(['[1]- Union','[2]- Diferencia','[3]- Igualdad','[4]- Funcion test','[5]- Salir'])
    miMenu.showMenu()
    op = miMenu.selectOption()

    while op != 5:
        if op != 4:
            #Ingreso de datos
            conjuntos=[]
            for i in range(2):
                print('Conjunto {}'.format(i+1))
                cant = int(input('Cantidad de elementos: '))
                conj = []
                for i in range(cant):
                    elem = input('elemento {}: '.format(i+1))
                    conj.append(elem)
                conjunto = Conjunto(conj)
                conjuntos.append(conjunto)

            print('Conjunto 1: ',end = '')
            conjuntos[0].muestra()
            print('Conjunto 2: ',end = '')
            conjuntos[1].muestra()

        #Operaciones con los conjuntos
        if op == 1:
            print('Union C1 U C2: ',end = '')
            conj3 = conjuntos[0] + conjuntos[1]
            conj3.muestra() 
            input('Presione ENTER para continuar...')
        elif op == 2:
            print('Diferencia C1 - C2: ',end = '')
            conj3 = conjuntos[0] - conjuntos[1]
            conj3.muestra()
            input('Presione ENTER para continuar...')
        elif op == 3:
            print('Iguladad C1 = C2: ',end = '')
            if conjuntos[0] == conjuntos[1]:
                print('Los conjuntos son iguales')
            else:
                print('Los conjuntos NO son iguales')
            input('Presione ENTER para continuar...')
        elif op == 4:
            test()
            input('Presione ENTER para continuar...')

        miMenu.showMenu()
        op = miMenu.selectOption()