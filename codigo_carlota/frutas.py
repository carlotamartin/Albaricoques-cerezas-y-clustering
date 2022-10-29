import cerezas
import albaricoques
import random
import pandas as pd
#tenemos que heredar los datos de cerezas y frutas que hemos generado para juntarlos
#tenemos que heredar las clases cerezas y albaricoques
#vamos a utilizar el método super() para heredar los métodos de las clases cerezas y albaricoques
class Frutas (albaricoques.Datos_Albaricoques, cerezas.Datos_Cerezas):
    #Constructor
    def __init__(self, Albaricoques_lista,Cerezas_lista) :
        self.Albaricoques_lista = Albaricoques_lista
        self.Cerezas_lista = Cerezas_lista

    def union_lista(self) :
        #self.lista_cerezas = super().generar_cerezas()
        #self.lista_albaricoques = super().generar_albaricoques()

        #Unión de la lista
        frutas = self.Cerezas_lista + self.Albaricoques_lista

        print(frutas)

        #Mezcla de las observaciones
        random.shuffle(frutas)

        #Guardado de las observaciones en un archivo
        dataFrame = pd.DataFrame(frutas)
        print(dataFrame.head(10))
        dataFrame.to_csv("codigo_carlota\datas\ frutas.csv", index=False,header=False)


#Creamos el main

def main():
    #Llamamos al main de cerezas y albaricoques para obtener los datos
    lista_cerezas = cerezas.main()
    print('LISTA DE LAS CEREZAS')
    lista_albaricoques = albaricoques.main()


    #Creamos el csv
    frutas = Frutas( lista_albaricoques,lista_cerezas)
    frutas.union_lista()


if __name__ == "__main__":
    main()



