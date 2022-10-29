import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st

class Curva_Gaussiana():
    def __init__(self, componentes):
        self.df = pd.read_csv("datas/frutas.csv", names=['DIAMETRO','PESO'], header=None)
        self.componentes = componentes
    '''
    def load (self):
        self.df = pd.read_csv("datas/frutas.csv", names=['DIAMETRO','PESO'], header=None)'''

    def curva_3D(self):
        # Extraer x e y
        x = self.df.DIAMETRO
        y = self.df.PESO
        # Define los límites
        deltaX = (max(x) - min(x))/10
        deltaY = (max(y) - min(y))/10
        xmin = min(x) - deltaX
        xmax = max(x) + deltaX
        ymin = min(y) - deltaY
        ymax = max(y) + deltaY
        print(xmin, xmax, ymin, ymax)
        # Crear meshgrid
        xx, yy = np.mgrid[xmin:xmax:100j, ymin:ymax:100j]

        posiciones = np.vstack([xx.ravel(), yy.ravel()])
        values = np.vstack([x, y])
        kernel = st.gaussian_kde(values)
        f = np.reshape(kernel(posiciones).T, xx.shape)

        fig = plt.figure(figsize=(8,8))
        ax = fig.gca()
        ax.set_xlim(xmin, xmax)
        ax.set_ylim(ymin, ymax)
        cfset = ax.contourf(xx, yy, f, cmap='coolwarm')
        ax.imshow(np.rot90(f), cmap='coolwarm', extent=[xmin, xmax, ymin, ymax])
        cset = ax.contour(xx, yy, f, colors='k')
        ax.clabel(cset, inline=1, fontsize=10)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        plt.show()

        from mpl_toolkits.mplot3d import axes3d, Axes3D
        fig = plt.figure(figsize=(13, 7))
        ax = plt.axes(projection='3d')
        surf = ax.plot_surface(xx, yy, f, rstride=1, cstride=1, cmap='coolwarm', edgecolor='none')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        fig.colorbar(surf, shrink=0.5, aspect=5) # añadir barra de color indicando el PDF
        ax.view_init(60, 35)
        plt.show()

def main():
    curva_gaussiana = Curva_Gaussiana(2)
    curva_gaussiana.curva_3D()
