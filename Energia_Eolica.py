
# 🔹 Importar librerías
import numpy as np
import streamlit as st
import pandas as pd

# 🔹 Título
st.write(''' # ODS 7: Energía Asequible y No Contaminante ''')

st.markdown("""
Esta aplicación utiliza **Machine Learning** para predecir la energía generada por una turbina eólica
en función de la velocidad del viento.
""")

st.image("Energia eolica.avif", caption="Generación de energía eólica.")

# 🔹 Sidebar (entrada del usuario)
st.sidebar.header("Parámetros del Viento")

velocidad = st.sidebar.slider("Velocidad del viento (m/s)", 0.0, 30.0, 10.0)

# 🔹 Cargar datos
df = pd.read_csv('Eolica_ODS7.csv')

# 🔹 Selección de variables
X = df[['Velocidad_Viento_ms']]
y = df['Eficiencia_Energetica_kWh']

# 🔹 Modelo
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=0)
LR = LinearRegression()
LR.fit(X_train,y_train)
# 🔹 Función de predicción (LO QUE TE PIDEN)
# Hacemos la predicción con el modelo y la temperatura seleccionada por el usuario
b1 = LR.coef_
b0 = LR.intercept_
prediccion = b0 + b1[0]*velocidad

# 🔹 Resultados
st.subheader('Energía generada')
st.write(f'La turbina produciría aproximadamente: {prediccion:.2f} kWh')

# 🔹 Interpretación simple
if prediccion < 150:
    st.warning("Producción baja")
elif prediccion < 300:
    st.info("Producción moderada")
else:
    st.success("Alta producción de energía")
