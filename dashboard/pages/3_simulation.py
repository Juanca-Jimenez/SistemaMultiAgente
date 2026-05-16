import streamlit as st

st.set_page_config(page_title="Simulation Control - SMA", layout="wide")

st.title("⚙️ Control de Simulación")

st.markdown("""
Desde este panel (en el futuro) podrás inyectar eventos manualmente al sistema o modificar las reglas en caliente para observar cómo reaccionan los agentes.
""")

with st.form("sim_config"):
    st.subheader("Parámetros del Hospital")
    c1, c2 = st.columns(2)
    with c1:
        st.number_input("Capacidad de Cardiología", min_value=1, max_value=50, value=10)
        st.number_input("Capacidad de Neurología", min_value=1, max_value=50, value=10)
    with c2:
        st.number_input("Capacidad General", min_value=1, max_value=100, value=15)
        st.number_input("Tasa de Llegada de Pacientes (x Tick)", min_value=1, max_value=20, value=3)
        
    submitted = st.form_submit_button("Actualizar Reglas en los Agentes")
    if submitted:
        st.success("Configuración enviada al CoordinatorAgent exitosamente (Mocked).")
