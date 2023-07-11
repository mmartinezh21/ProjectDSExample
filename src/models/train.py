# train_model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import preprocessing
import helpers.DataLoader as Dtl  

#Solución sugeridad por demás compañeros al problema sobre "ModuleNotFoudError: No module named 'helpers'"
#import os
#import sys
#sys.path.insert(0, os.path.join(os.path.dirname(sys.path[0]),"helpers"))
#from DataLoader import * 
 




# Leer los datos
#df = pd.read_csv("./data/processed/RH_procesado.csv") Código antes de cambiar a POO

reader = Dtl.Dataloader("./data/processed/RH_procesado.csv") #Implementando POO
df = reader.load_data()


# Convertir columnas no numéricas a numéricas
for column in df.columns:
    if df[column].dtype == type(object):
        le = preprocessing.LabelEncoder()
        df[column] = le.fit_transform(df[column])

# Mapear la columna 'Desercion'
mapeo_desercion = {1: 1, 0: 0, 2: 0}
df["Desercion"] = df["Desercion"].replace(mapeo_desercion)

# Suponiendo que 'Desercion' es la columna que quieres predecir
X = df.drop("Desercion", axis=1)
y = df["Desercion"]

# Dividir los datos en conjunto de eWntrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Entrenar un modelo de Random Forest
clf = RandomForestClassifier()
clf.fit(X_train, y_train)

# Guardar el modelo entrenado
import joblib

joblib.dump(clf, "./random_forest.joblib")
