import frutas
import random

class Cerezas ():
    def __init__(self, lista) :
        self.lista = lista


    def __str__(self) :
        return 'lista {}'.format(self.lista)


    def generar_cerezas(self, numero_observaciones):
        cerezas = []
        random.seed()
        for iteration in range(numero_observaciones):
            #elección al azar de una característica
            cereza = random.choice(self.lista)
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
    lista = cerezas.generar_cerezas(500)

if __name__ == "__main__":
    main()

