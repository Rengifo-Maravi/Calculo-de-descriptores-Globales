import streamlit as st

def calcular_descriptores(homo, lumo):
    # Calcular descriptores globales
    gap = homo - lumo
    energia_ionizacion = -homo  # E_I = -HOMO
    afinidad_electronica = -lumo  # A = -LUMO
    dureza_global = gap / 2  # η = (HOMO - LUMO) / 2
    blandura_global = 1 / dureza_global  # S = 1 / η
    electrofilicidad_global = (energia_ionizacion + afinidad_electronica) ** 2 / (2 * dureza_global)  # ω = (μ^2) / 2η

    return {
        "Brecha de Energía (HOMO - LUMO)": gap,
        "Energía de Ionización": energia_ionizacion,
        "Afinidad Electrónica": afinidad_electronica,
        "Dureza Global (η)": dureza_global,
        "Blandura Global (S)": blandura_global,
        "Electrofilicidad Global (ω)": electrofilicidad_global,
    }

def main():
    st.title("Cálculo de Descriptores Globales a partir de HOMO y LUMO")

    st.header("Ingresa los valores de HOMO y LUMO")

    # Entrada de HOMO y LUMO
    homo = st.number_input("HOMO (Ejemplo: -5.0)", step=0.1, format="%.2f")
    lumo = st.number_input("LUMO (Ejemplo: -1.0)", step=0.1, format="%.2f")

    # Selección de unidades de entrada
    unidades_entrada = st.radio("Selecciona las unidades de HOMO y LUMO:", ["eV", "Hartrees"], index=0)

    # Conversión de unidades si es necesario
    if unidades_entrada == "Hartrees":
        homo *= 27.2114
        lumo *= 27.2114

    # Selección de unidades de salida
    unidades_salida = st.radio("Selecciona las unidades para los resultados:", ["eV", "Hartrees"], index=0)

    if st.button("Calcular Descriptores"):
        if homo <= lumo:
            st.error("El valor de HOMO debe ser mayor que el de LUMO.")
        else:
            descriptores = calcular_descriptores(homo, lumo)

            # Conversión de resultados si es necesario
            if unidades_salida == "Hartrees":
                conversion_factor = 1 / 27.2114
                descriptores = {k: v * conversion_factor for k, v in descriptores.items()}

            st.subheader("Resultados")
            for descriptor, valor in descriptores.items():
                st.write(f"{descriptor}: {valor:.4f} {unidades_salida}")

if __name__ == "__main__":
    main()
