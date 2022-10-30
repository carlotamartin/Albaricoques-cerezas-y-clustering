import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from joblib import dump
from sklearn import mixture #para el algortimo de mezclas gausianas

class Cluster ():
    def __init__(self, df, num_clusters):
        self.df = df
        self.num_clusters = num_clusters

    def grafica (self):
        self.df.plot.scatter(x="DIAMETRO",y="PESO")
        plt.show()

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
        plt.savefig('codigo_carlota/plots/modelos.png')
        #dump(modelo,'codigo_carlota/modelos/kmean.joblib')

    def adaptacion_cluster(self, cereza, albaricoque):
        modelo = KMeans(n_clusters = self.num_clusters)
        modelo.fit(self.df)
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
    #Primero cargamos los datos y los cargamos
    df = pd.read_csv("codigo_carlota/datas/ frutas.csv", names=['DIAMETRO','PESO'], header=None)
    #Creamos el cluster
    cluster = Cluster(df,2)
    #Gráfica
    cluster.grafica()
    #Hecemos el algoritmo Kmeans
    cluster.aprendizaje()
    cluster.adaptacion_cluster([26.98,8.75],[55.7,102.16])

    #Modelo de mezclas gaussianas (GMM)
    cluster.mezclas_gaussianas()


if __name__ == "__main__":
    main()


