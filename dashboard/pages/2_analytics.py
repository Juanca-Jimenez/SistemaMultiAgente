import streamlit as st
import json
import os
import random
from dashboard.components.charts import draw_wait_time_trend
from src.utils.config import BASE_DIR

st.set_page_config(page_title="Analytics - SMA", layout="wide")

st.title("📊 Análisis Histórico y KPIs")
st.markdown("Resultados consolidados de las últimas simulaciones")

report_path = os.path.join(BASE_DIR, 'logs', 'summary_report.json')

col1, col2, col3 = st.columns(3)

try:
    if os.path.exists(report_path):
        with open(report_path, 'r') as f:
            data = json.load(f)
            
        col1.metric("Pacientes Procesados", data.get("total_processed", 0))
        col2.metric("Pacientes Rechazados", data.get("total_rejected", 0))
        col3.metric("Tiempo Espera Promedio", f"{data.get('average_wait_time', 0):.1f} min")
    else:
        st.warning("No se encontró el reporte JSON de la simulación. Corriendo con datos simulados.")
        col1.metric("Pacientes Procesados", 342)
        col2.metric("Pacientes Rechazados", 5)
        col3.metric("Tiempo Espera Promedio", "34.5 min")
except Exception as e:
    st.error(f"Error leyendo el reporte: {e}")

st.divider()

st.subheader("Evolución del Tiempo de Espera (Simulado)")
# Generamos una serie temporal de mentira con tendencia a la baja
trend = [50]
for _ in range(50):
    trend.append(max(10, trend[-1] + random.randint(-5, 4)))

st.plotly_chart(draw_wait_time_trend(trend), use_container_width=True)

st.divider()

st.subheader("Log de Simulación (Raw)")
log_path = os.path.join(BASE_DIR, 'logs', 'sma_hospital.log')
if os.path.exists(log_path):
    with open(log_path, 'r') as f:
        # Mostramos solo las últimas 20 líneas
        lines = f.readlines()
        st.code("".join(lines[-20:]), language='text')
else:
    st.info("Archivo de log no encontrado. Corre 'python main.py' para generarlo.")
