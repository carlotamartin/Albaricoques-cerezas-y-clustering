from cerezas import Cerezas
from albaricoques import Albaricoques
#tenemos que heredar los datos de cerezas y frutas que hemos generado para juntarlos
#tenemos que heredar las clases cerezas y albaricoques
class frutas (Cerezas, Albaricoques):
    def __init__(self, datos_cerezas, datos_albaricoques) :
        self.datos_cerezas = Cerezas.main
        self.datos_albaricoques = Albaricoques.main

    def __str__(self) :
        return 'lista {}'.format(self.datos_albaricoques)


def main():
    

