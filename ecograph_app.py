
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------------------------
# FUNCIÓN: Mercado de Dinero
# -----------------------------------------------
def mercado_dinero(Y, P, Ms_real, ax):
    k = 0.5
    h = 100
    Ms = Ms_real / P
    i_max = (k * Y) / h
    i = np.linspace(0, i_max * 1.2, 100)
    Md = k * Y - h * i
    i_eq = (k * Y - Ms) / h

    ax.plot(Md, i, label='Demanda de Dinero (Md)', color='blue')
    ax.axvline(Ms, color='red', linestyle='--', label='Oferta Monetaria Real (Ms/P)')
    ax.plot([Ms], [i_eq], 'ko', label=f"Equilibrio: i = {i_eq:.2f}")

    ax.set_xlabel('M/P (Dinero Real)')
    ax.set_ylabel('Tasa de interés (i)')
    ax.set_title('Mercado de Dinero')
    ax.set_xlim(0, max(Ms, Md.max()) * 1.1)
    ax.legend()
    ax.grid(True)

    return i_eq

# -----------------------------------------------
# FUNCIÓN: Demanda de Inversión
# -----------------------------------------------
def demanda_inversion(I0, b, i, ax):
    i_vals = np.linspace(0, i * 1.2, 100)
    I_vals = I0 - b * i_vals
    ax.plot(I_vals, i_vals, label="Curva de Inversión", color='orange')
    ax.plot([I0 - b * i], [i], 'ko', label=f"i = {i:.2f}")

    ax.set_xlabel("Inversión (I)")
    ax.set_ylabel("Tasa de interés (i)")
    ax.set_title("Demanda de Inversión")
    ax.legend()
    ax.grid(True)

# -----------------------------------------------
# FUNCIÓN: Mercado de Bienes
# -----------------------------------------------
def mercado_bienes(Y_max, C0, c, I0, G, T, i, b, ax):
    Y = np.linspace(0, Y_max, 100)
    C = C0 + c * (Y - T)
    I = I0 - b * i
    DA = C + I + G
    ax.plot(Y, DA, label="DA = C + I + G", color='purple')
    ax.plot(Y, Y, linestyle='--', label="45°: Y = DA", color='gray')
    ax.set_xlabel("Ingreso (Y)")
    ax.set_ylabel("Demanda Agregada (DA)")
    ax.set_title("Mercado de Bienes")
    ax.legend()
    ax.grid(True)

# -----------------------------------------------
# Streamlit App
# -----------------------------------------------
st.title("EcoGraph - Simulador Macroeconómico Interactivo")

Y = st.slider("Ingreso (Y)", 500, 2000, 1000, step=100)
P = st.slider("Precios (P)", 0.5, 2.0, 1.0, step=0.1)
Ms_real = st.slider("Ms real", 100, 1000, 500, step=50)
C0 = st.slider("Consumo autónomo (C₀)", 50, 200, 100, step=10)
c = st.slider("Propensión marginal a consumir (c)", 0.1, 1.0, 0.8, step=0.05)
I0 = st.slider("Inversión autónoma (I₀)", 50, 300, 150, step=10)
G = st.slider("Gasto público (G)", 100, 500, 200, step=50)
T = st.slider("Impuestos (T)", 50, 300, 100, step=25)
b = st.slider("Sensibilidad de inversión (b)", 50, 500, 300, step=25)

fig, axs = plt.subplots(1, 3, figsize=(20, 5))
i = mercado_dinero(Y, P, Ms_real, axs[0])
demanda_inversion(I0, b, i, axs[1])
mercado_bienes(2000, C0, c, I0, G, T, i, b, axs[2])
st.pyplot(fig)
