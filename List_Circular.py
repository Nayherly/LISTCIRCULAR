#gregar ultimo
#Eliminar ultimo.
#Lista Vacía
#Agregar Inicio
#Eliminar Inicio
#Mostrar Lista

class Nodo:
    def __init__(self,dato):
        self.dato = dato
        self.next = None

class ListaCircular:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def vacia(self):
        return self.head == None #none representa a vacio

    def agregar_inicio(self,dato):
        if self.vacia():
            self.head = self.tail = Nodo(dato)
                                 
        else:
            aux = Nodo(dato)
            aux.next = self.head
            self.head = aux
            self.tail.next = self.head
            
    
    def agregar_ultimo (self,dato): #funciona
        if self.vacia():
            self.head = self.tail = Nodo(dato)
            self.tail.next = self.head #Ahora apunta a la cabeza, porque es circular 
           
        else:
            aux = self.tail
            self.tail = aux.next = Nodo(dato)
            self.tail.next = self.head
            

    def recorrido(self):
        aux = self.head
        while aux:
            print(aux.dato)
            aux = aux.next
            if aux == self.head:
                break

    def eliminar_ultimo(self):
        if self.vacia():
            print("lista vacia")
        elif self.head == self.tail:
            self.head = self.tail = None
        else:
            aux = self.head
            while aux.next != self.tail:
                aux = aux.next
            aux.next = self.head
            self.tail = aux
        

    def eliminar_inicio(self):
        if self.vacia():
            print("lista vacia")
        elif self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head


try:
    if __name__ == "__main__":
        opcion = 0
        lista = ListaCircular()
        
        while opcion !=7:
            print("Lista Circular: \n 1.Agregar Ultimo\n 2.Eliminar ultimo\n 3.Lista vacia?\n 4.Agregar Inicio\n 5. Eliminar inicio\n 6.Mostrar toda la lista\n 7.Salir")
            opcion = int(input("Ingrese opcion: "))

            if opcion == 1:
                dato = input("Ingrese un dato: ")
                lista.agregar_ultimo(dato)
            elif opcion == 2:
                lista.eliminar_ultimo()
            elif opcion == 3:
                print("Si" if lista.vacia()else "No")
            elif opcion == 4:
                dato = input("Ingrese un dato: ")
                lista.agregar_inicio(dato)
            elif opcion == 5:
                lista.eliminar_inicio()
            elif opcion == 6:
                lista.recorrido()
            elif opcion == 7:
                print("FIN")
            else:
                print("Ingrese un dato correcto")

except Exception as e:
    print(e)