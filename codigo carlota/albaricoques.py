import random

class Albaricoques ():
    def __init__(self, lista_albaricoques) :
        self.lista_albaricoques = lista_albaricoques

    def __str__(self) :
        return 'LISTA ALBARICOQUES {}'.format(self.lista_albaricoques)

    def get (self):
        return self.lista_albaricoques

    def set (self, elemento):
        self.lista_albaricoques.append(elemento)

class Datos_Albaricoques (Albaricoques):
    def __init__ (self, numero_observaciones, lista_albaricoques):
        super().__init__(lista_albaricoques) #heredamos la lista de los albaricoques
        self.numero_observaciones = numero_observaciones

    def __str__(self) :
        return 'LISTA ALBARICOQUES: \n {} \n Número de observaciones: {}'.format(self.lista_albaricoques, self.numero_observaciones)


    def generar_albaricoques(self):
        albaricoques = []
        random.seed()
        for iteration in range(self.numero_observaciones):
            #elección al azar de una característica
            albaricoque = random.choice(self.lista_albaricoques)
            #Generación de un diámetro
            diametro = round(random.uniform(albaricoque[0], albaricoque[1]),2)
            #Generación de un peso
            limiteMinPeso = albaricoque[2] / 1.10
            limiteMaxPeso = albaricoque[2] * 1.10
            peso = round(random.uniform(limiteMinPeso, limiteMaxPeso),2)
            print ("Albaricoque "+str(iteration)+" "+str(albaricoque)+" : "+str(diametro)+" - "+str(peso))
            albaricoques.append([diametro,peso])
        return albaricoques
def main():
    lista = [[40,44,41],[45,49,54],[50,54,74],[55,59,100]]
    albaricoques = Albaricoques(lista)
    print(albaricoques)
    #Añadimos un dato más de las cerezas
    albaricoques.set([55,59,100])
    print(albaricoques)

    #Creamos los datos de las cerezas
    datos_albaricoques = Datos_Albaricoques(500, lista)


    return datos_albaricoques.generar_albaricoques()


if __name__ == "__main__":
    main()


