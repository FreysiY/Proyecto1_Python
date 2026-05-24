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


elif seccion == "Ejercicio 2":
          st.title("Registro con NumPy")
          st.markdown("Registro de productos en arrays y DataFrame")
          
          if "datos" not in st.session_state:
                    st.session_state.datos = []
                    
          nombredelproducto = st.text_input("Nombre del Producto")
          categoria = st.selectbox("Categoría", ["A", "B", "C"])
          precio = st.number_input("Precio", min_value=0.0)
          cantidad = st.number_input("Cantidad", min_value=1)
                    
          if st.button("Agregar registro"):
                    if nombredelproducto != "":
                              total = precio * cantidad
                              st.session_state.datos.append([nombredelproducto, categoria, precio, cantidad, total])

                              st.success("Registro agregado correctamente")
                    else:
                              st.error("Ingrese nombre del producto")
                    
          if st.session_state.datos:
                    arreglo = np.array(st.session_state.datos, dtype=object)
                    df = pd.DataFrame(arreglo, columns=["Nombre del Producto", "Categoría", "Precio", "Cantidad", "Total"])
                    st.dataframe(df)


elif seccion == "Ejercicio 3":
          from libreria_funciones_proyecto1 import calcular_productividad_laboral
          st.title("Ejercicio 3: Productividad Laboral")

          st.markdown("""
          Cálculo de productividad en operaciones:
          -Productividad por hora
          -Productividad por trabajador
          """)
          
          if "historial_prod" not in st.session_state:
                    st.session_state.historial_prod = []
                    
          opcion = st.selectbox(
                    "Seleccione función",["Productividad Laboral"])
          
          unidades = st.number_input("Unidades producidas", min_value=0.0)
          horas = st.number_input("Horas trabajadas", min_value=0.0)
          trabajadores = st.number_input("Número de trabajadores", min_value=1)
          
          if st.button("Calcular productividad"):
                    try:
                              resultado = calcular_productividad_laboral(unidades, horas, trabajadores)
                              
                              st.write("Resultado:")
                              st.write(resultado)
                              
                              st.session_state.historial_prod.append({
                                        "Unidades": unidades,
                                        "Horas": horas,
                                        "Trabajadores": trabajadores,
                                        "Prod/Hora": resultado["productividad_por_hora"],
                                        "Prod/Trabajador": resultado["productividad_por_trabajador"]
                                        })

                              st.success("Cálculo realizado correctamente")
                    
                    except Exception as e:
                              st.error(f"Error: {e}")
          
          if st.session_state.historial_prod:
                    df = pd.DataFrame(st.session_state.historial_prod)
                    
                    st.subheader("Histórico de resultados")
                    st.dataframe(df)















elif seccion == "Ejercicio 4":

    st.title("CRUD simple")
    st.markdown("Registro de productos")

    if "productos" not in st.session_state:
        st.session_state.productos = []

    nombre = st.text_input("Nombre")
    precio = st.number_input("Precio")

    if st.button("Agregar producto"):
        st.session_state.productos.append([nombre, precio])

    if st.session_state.productos:
        df = pd.DataFrame(st.session_state.productos, columns=["Nombre", "Precio"])
        st.dataframe(df)

        eliminar = st.selectbox("Seleccionar producto a eliminar", df["Nombre"])

        if st.button("Eliminar"):
            st.session_state.productos = [
                p for p in st.session_state.productos if p[0]!= eliminar
            ]
                    
