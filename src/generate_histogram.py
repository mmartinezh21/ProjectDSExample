# src/generate_figures.py
import pandas as pd
import matplotlib.pyplot as plt
import helpers.DataLoader as Dtl  

#Solución sugeridad por demás compañeros al problema sobre "ModuleNotFoudError: No module named 'helpers'"
#import os
#import sys
#sys.path.insert(0, os.path.join(os.path.dirname(sys.path[0]),"helpers"))
#from DataLoader import *  


def plot_histogram(df, column, output_path):
    plt.figure(figsize=(10, 6))
    plt.hist(df[column])
    plt.title(f"Distribución de {column}")
    plt.xlabel(column)
    plt.ylabel("Frecuencia")

    plt.savefig(output_path)
    plt.close()


def main():
    
    #df = pd.read_csv("./data/processed/RH_procesado.csv") Código antes de cambiar a POO
    reader = Dtl.Dataloader("./data/processed/RH_procesado.csv") #Implementando POO
    df = reader.load_data()

    # Asegúrate de que los datos estén correctamente procesados antes de intentar trazarlos
    plot_histogram(df, "Desercion", "./reports/figures/histograma_desercion.png")


if __name__ == "__main__":
    main()
