import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from joblib import dump
from sklearn import mixture #para el algortimo de mezclas gausianas



class Carga_datos():
    def __init__(self, df):
        self.df = df

    def load (self):
        self.df = pd.read_csv("datas/frutas.csv", names=['DIAMETRO','PESO'], header=None)

    def grafica (self):
        self.dr.plot.scatter(x="DIAMETRO",y="PESO")
        plt.show()

class cluster (Carga_datos):
    def __init__(self, df, num_clusters):
        super().__init__(df)
        self.num_clusters = num_clusters

    def aprendizaje (self):

        #Predicciones
        modelo = KMeans(n_clusters = self.num_clusters)
        modelo.fit(self.df)

        #Predicciones
        predicciones_kmeans = modelo.predict(self.df)

        #Visualización de la clusterización
        plt.scatter(self.df.DIAMETRO, self.df.PESO, c=predicciones_kmeans, s=50, cmap='viridis')
        plt.xlabel("DIAMETRO")
        plt.ylabel("PESO")

        #Visualización de los centroides
        centers = modelo.cluster_centers_
        plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5)
        plt.show()
        plt.savefig('plots/modelos.png')
        dump(modelo,'modelos/kmean.joblib')

    def adaptacion_cluster(self, cereza, albaricoque):
        modelo = KMeans(n_clusters = self.num_clusters)
        numCluster = modelo.predict(cereza)
        print("Número de clúster de las cerezas: "+ str(numCluster))


        numCluster = modelo.predict(albaricoque)
        print("Número de clúster de los albaricoques: " + str(numCluster))


    def mezclas_gaussianas(self):
        gmm = mixture.GaussianMixture(n_components=self.num_clusters)
        #Aprendizaje
        gmm.fit(self.df)

        #Clasificación
        clusteres = gmm.predict(self.df)

        #Visualización de los clústeres
        plt.scatter(self.df.DIAMETRO, self.df.PESO, c=clusteres, s=40, cmap='viridis');
        plt.xlabel("DIAMETRO")
        plt.ylabel("PESO")
        plt.show()


def main():
    

