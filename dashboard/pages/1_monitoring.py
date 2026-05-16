import streamlit as st
import pandas as pd
import random
import time
from dashboard.components.charts import draw_congestion_bar_chart

st.set_page_config(page_title="Monitoring - SMA", layout="wide")

st.title("🔴 Live Monitoring")
st.markdown("Monitorización del Estado de Agentes del Hospital")

# Simulamos la lectura en vivo de los agentes variando levemente los datos con cada recarga o con un loop
if 'live_data' not in st.session_state:
    st.session_state.live_data = {
        "Cardiology": 80,
        "Neurology": 50,
        "General": 80,
        "Orthopedics": 30
    }

# Simular cambio en vivo
for k in st.session_state.live_data.keys():
    change = random.choice([-5, 0, 5])
    new_val = max(0, min(100, st.session_state.live_data[k] + change))
    st.session_state.live_data[k] = new_val

col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("Estado de los Departamentos")
    for dept, val in st.session_state.live_data.items():
        st.metric(label=dept, value=f"{val}%", delta=f"{random.choice(['-','+'])}{random.randint(1,5)}%")

with col2:
    st.subheader("Mapa de Congestión")
    df = pd.DataFrame({
        "Departamento": list(st.session_state.live_data.keys()),
        "Nivel Congestión (%)": list(st.session_state.live_data.values())
    })
    st.plotly_chart(draw_congestion_bar_chart(df), use_container_width=True)

st.divider()
st.subheader("Últimas Notificaciones del MessageBus")
st.info("🕒 10:42 AM - [CoordinatorAgent] - Paciente asignado a Cardiology")
st.warning("🕒 10:40 AM - [MonitoringAgent] - Congestión detectada en General")
st.success("🕒 10:35 AM - [DepartmentAgent] - 3 pacientes dados de alta en Orthopedics")

# Si se quiere que se recargue solo, descomentar (puede ser molesto al desarrollar)
# time.sleep(5)
# st.rerun()
