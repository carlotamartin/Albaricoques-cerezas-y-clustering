import random

class Cerezas ():
    def __init__(self, lista_cerezas) :
        self.lista_cerezas = lista_cerezas

    def __str__(self) :
        return 'LISTA CEREZAS: \n {} '.format(self.lista_cerezas)

    def get (self):
        return self.lista_cerezas

    def set (self, elemento):
        self.lista_cerezas.append(elemento)

class Datos_Cerezas (Cerezas):
    def __init__ (self, numero_observaciones, lista_cerezas):
        self.numero_observaciones = numero_observaciones
        super().__init__(lista_cerezas) #heredamos la lista de las cerezas

    def __str__(self) :
        return 'LISTA CEREZAS: \n {} \n Número de observaciones: {}'.format(self.lista_cerezas, self.numero_observaciones)

    def generar_cerezas(self):
        cerezas = []
        random.seed()
        for iteration in range(self.numero_observaciones):
            #elección al azar de una característica
            cereza = random.choice(self.lista_cerezas)
            #Generación de un diámetro
            diametro = round(random.uniform(cereza[0], cereza[1]),2)
            #Generación de un peso
            peso = round(random.uniform(cereza[2], cereza[3]),2)
            print ("Cereza "+str(iteration)+" "+str(cereza)+" : "+str(diametro)+" - "+str(peso))
            cerezas.append([diametro,peso])

        return cerezas



def main():
    lista = [[17,19,1,5],[20,21,5,6],[22,23,6,7],[24,25,7,8.5],[26,27,8.5,10],[28,29,10,11.5]]
    cerezas = Cerezas(lista)
    print(cerezas)
    #Añadimos un dato más de las cerezas
    cerezas.set([28,29,10,11.5])
    print(cerezas)

    #Creamos los datos de las cerezas
    datos_cerezas = Datos_Cerezas(500,lista)
    lista = datos_cerezas.generar_cerezas()
    return lista

if __name__ == "__main__":
    main()

