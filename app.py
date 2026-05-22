import streamlit as st
import pandas as pd
import numpy as np


st.title("MI PRIMER PROYECTO EN STREAMLIT")

seccion = st.sidebar.selectbox("Sección", ["Home","Ejercicio 1","Ejercicio 2","Ejercicio 3","Ejercicio 4"])


if seccion == "Home":
          st.title("Proyecto Python Fundamentals")
          st.subheader("Aplicación en Streamlit")
          
          st.write("Nombre: Freysi Ybeth Zurita Yman")
          st.write("Módulo: 1")
          st.write("Año: 2026")
          
          st.markdown("Descripción: Esta aplicación integra variables y estructuras de datos, listas, NumPy, funciones, programación funcional y orientada a objetos.")
          
          st.image("logoPythonDMC.png")
          

elif seccion == "Ejercicio 1":
          st.title("Flujo de Caja con Listas")
          st.markdown("Registro de ingresos y gastos usando listas → diccionario → DataFrame")
          
          if "concepto" not in st.session_state:
                    st.session_state.concepto = []
                    
          if "tipodemovimiento" not in st.session_state:
                    st.session_state.tipodemovimiento = []
          
          if "valor" not in st.session_state:
                    st.session_state.valor = []

          concepto = st.text_input("Concepto")
          tipodemovimiento = st.selectbox("Tipo de movimiento", ["Ingreso", "Gasto"])
          valor = st.number_input("Valor", min_value=0.0)
          
          if st.button("Agregar movimiento"):
                    
                    st.session_state.concepto.append(concepto)
                    st.session_state.tipodemovimiento.append(tipodemovimiento)
                    st.session_state.valor.append(valor)
          
                    st.success("Movimiento agregado")
         
          if st.session_state.concepto:
                    datos = {
                                "Concepto": st.session_state.concepto,
                                "Tipo de movimiento": st.session_state.tipodemovimiento,
                                "Valor": st.session_state.valor
                    }
                    
                    df = pd.DataFrame(datos)

                    st.subheader("Movimientos registrados")
                    st.dataframe(df)

                    ingresos = df[df["Tipo de movimiento"] == "Ingreso"]["Valor"].sum()
                    gastos = df[df["Tipo de movimiento"] == "Gasto"]["Valor"].sum()
                    saldo = ingresos - gastos

                    st.subheader("Resultados")

                    st.metric("Total ingresos", ingresos)
                    st.metric("Total gastos", gastos)
                    st.metric("Saldo final", saldo)

                    if saldo > 0:
                              st.success("Flujo de caja a favor")
                    elif saldo < 0:
                              st.error("Flujo de caja en contra")
                    else:
                              st.info("Flujo equilibrado")
                    
