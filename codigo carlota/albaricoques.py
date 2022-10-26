import frutas
import random

class albaricoques ():
    def __init__(self, lista) :
        self.lista = lista


    def __str__(self) :
        return 'lista {}'.format(self.lista)

    def generar_albaricoques(self, numero_observaciones):
        albaricoques = []
        random.seed()
        for iteration in range(numero_observaciones):
            #elección al azar de una característica
            albaricoque = random.choice(self.lista)
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
    albaricoque = albaricoques(lista)
    lista = albaricoque.generar_albaricoques(500)

if __name__ == "__main__":
    main()


