# src/generate_figures.py
import pandas as pd
import matplotlib.pyplot as plt
import helpers.DataLoader as Dtl


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
