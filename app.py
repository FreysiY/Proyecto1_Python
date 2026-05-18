import streamlit as st
import pandas as pd
import numpy as np


st.title("Mi primer proyecto en Streamlit")

st.sidebar.title("Secciones")

seccion = st.sidebar.selectbox("Sección", ["Home","Ejercicio 1","Ejercicio 2","Ejercicio 3","Ejercicio 4"])


if seccion == "Home":
          st.title("Proyecto Python Fundamentals")
          st.subheader("Aplicación en Streamlit")
          
          st.write("Nombre: Freysi Ybeth Zurita Yman")
          st.write("Módulo: 1-Python Fundamentals")
          st.write("Año: 2026")
          
          st.markdown(" Esta aplicación integra variables y estructuras de datos, listas, NumPy, funciones, programación funcional y orientada a objetos")
          
          st.image("logoPythonDMC")
          

elif seccion == "Ejercicio 1":
          st.title("Flujo de Caja con Listas")
          st.markdown("Registro de ingresos y gastos usando listas")
