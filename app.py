import streamlit as st
import pandas as pd
import numpy as np
import libreria_funciones as lf

st.title("Mi primer proyecto en Python Fundamentals")

st.sidebar.title("Secciones")

st.write("Elaborado por: Freysi Ybeth Zurita Yman
          Módulo: 1
          Año: 2026
          Descripción del proyecto: Se presenta un aplicación interactiva en Streamlit que integra los contenidos revisados durante el módulo 1
          Tecnologías utilizadas: GitHub, Streamlit, librerías entre otros")

st.sidebar.image("logoPythonDMC")

seccion = st.sidebar.selectbox("Seleccione una sección", ["Ejercicio 1","Ejercicio 2","Ejercicio 3","Ejercicio 4"])

if seccion == "Ejercicio 1":
  st.write("Bienvenido al ejercicio 1")
  st.image("logoPythonDMC" )

elif seccion == "Ejercicio 2":
  st.write("Bienvenido al ejercicio 2")

  precio = st.number_input("Ingrese el precio del producto", min_value = 0 , max_value = 5000 , value = 1200)
  descuento = st.number_input("Ingrese el descuento del producto del 0 al 100% ", min_value = 0 , max_value = 100 )

  precio_final_producto = precio - (precio*(descuento/100))

  st.write("El precio final del producto es: ", precio_final_producto  )

elif seccion == "Ejercicio 3":
  st.write("Bienvenido al ejercicio 3")
  fin_rango = st.slider("Seleccione un valor",min_value = 0, max_value = 20, value = 7)

  arreglo = np.arange(0, fin_rango)
  st.write(arreglo)

else:
  st.write("Bienvenido al ejercicio 4")
  principal = st.number_input("Ingrese el monto del préstamo", value=1000)
  tasa_anual = st.number_input("Ingrese la tasa anual en decimal", value=0.1, min_value=0.0, max_value=1.0)
  anios = st.number_input("Ingrese el número de años del préstamo", value=1)
  pagos_anio = st.number_input("Ingrese la cantidad de pagos por año", value=12)
    
  cuota = round(lf.cuota_prestamo(principal, tasa_anual, anios, pagos_anio),2)
  st.write(f"El valor de la cuota es {cuota}")
