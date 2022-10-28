import cerezas
import albaricoques
import random
import pandas as pd
#tenemos que heredar los datos de cerezas y frutas que hemos generado para juntarlos
#tenemos que heredar las clases cerezas y albaricoques
#vamos a utilizar el método super() para heredar los métodos de las clases cerezas y albaricoques
class frutas (albaricoques.Datos_Albaricoques, cerezas.Datos_Cerezas):
    #Constructor
    def __init__(self, Cerezas_lista, Albaricoques_lista) :
        super().__init__(Cerezas_lista, Albaricoques_lista)

    def union_lista(self) :
        self.lista_cerezas = super().generar_cerezas()
        self.lista_albaricoques = super().generar_albaricoques()

        #Unión de la lista
        frutas = self.lista_cerezas + self.lista_albaricoques

        print(frutas)

        #Mezcla de las observaciones
        random.shuffle(frutas)

        #Guardado de las observaciones en un archivo
        dataFrame = pd.DataFrame(frutas)
        dataFrame.to_csv("datas/frutas.csv", index=False,header=False)


#Creamos el main

def main():
    #Llamamos al main de cerezas y albaricoques para obtener los datos
    lista_cerezas = cerezas.main()
    print(lista_cerezas)
    lista_albaricoques = albaricoques.main()
    print (lista_albaricoques)
    '''
    lista_cerezas = [[17,19,1,5],[20,21,5,6],[22,23,6,7],[24,25,7,8.5],[26,27,8.5,10],[28,29,10,11.5]]
    datos_cerezas = Datos_Cerezas(500, lista_cerezas)

    lista_albaricoques = [[40,44,41],[45,49,54],[50,54,74],[55,59,100]]
    datos_albaricoques = Datos_Albaricoques(500, lista_albaricoques)
    print(datos_albaricoques)'''


if __name__ == "__main__":
    main()



