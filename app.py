import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="BioGea AquaManager", layout="wide")

st.title("Sistema integral de gestión técnica para camaroneras y piscifactorías")

modulo = st.sidebar.selectbox("Selecciona un módulo", [
    "Módulo 1: Cultivo Productivo",
    "Módulo 2: Calidad de Agua",
    "Módulo 3: Alimentación",
    "Módulo 4: Costos y Rentabilidad",
    "Módulo 5: Manejo Sanitario",
    "Módulo 6: Personal y Actividades",
    "Módulo 7: Cosecha y Resultados",
    "Módulo 8: Dashboard Visual"
])

if modulo == "Módulo 1: Cultivo Productivo":
    st.subheader("Módulo 1: Cultivo Productivo")
    st.write("Registro semanal de peso, talla, biomasa, mortalidad y SGR.")
    data = {
        "Semana": list(range(5)),
        "Peso (g)": [1.2, 2.4, 3.5, 4.1, 5.0],
        "Talla (cm)": [2.3, 3.6, 4.2, 5.1, 6.0],
        "Mortalidad (%)": [0, 2, 1, 3, 2],
    }
    df = pd.DataFrame(data)
    st.dataframe(df)
    fig, ax = plt.subplots()
    ax.plot(df["Semana"], df["Peso (g)"], marker='o', label="Peso")
    ax.plot(df["Semana"], df["Talla (cm)"], marker='s', label="Talla")
    ax.set_xlabel("Semana")
    ax.set_ylabel("Medidas")
    ax.legend()
    st.pyplot(fig)

elif modulo == "Módulo 2: Calidad de Agua":
    st.subheader("Módulo 2: Calidad de Agua")
    st.write("Ingreso semanal de parámetros físico-químicos con validación por rangos.")

elif modulo == "Módulo 3: Alimentación":
    st.subheader("Módulo 3: Alimentación")
    st.write("Registro diario de alimento ofrecido, FCR y balance de bodega.")

elif modulo == "Módulo 4: Costos y Rentabilidad":
    st.subheader("Módulo 4: Costos y Rentabilidad")
    st.write("Ingreso de eventos de costos y análisis de rentabilidad.")

elif modulo == "Módulo 5: Manejo Sanitario":
    st.subheader("Módulo 5: Manejo Sanitario")
    st.write("Registro de tratamientos, productos veterinarios, dosis y vías.")

elif modulo == "Módulo 6: Personal y Actividades":
    st.subheader("Módulo 6: Personal y Actividades")
    st.write("Turnos, actividades diarias y pagos al personal.")

elif modulo == "Módulo 7: Cosecha y Resultados":
    st.subheader("Módulo 7: Cosecha y Resultados")
    st.write("Peso final, rendimiento por hectárea y precio de venta.")

elif modulo == "Módulo 8: Dashboard Visual":
    st.subheader("Módulo 8: Dashboard Visual")
    st.write("Resumen visual de KPIs productivos, sanitarios y económicos.")