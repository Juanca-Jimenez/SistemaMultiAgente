import streamlit as st
from dashboard.components.metrics_cards import render_dashboard_header

st.set_page_config(page_title="Inicio - SMA", layout="wide", page_icon="🏥")

render_dashboard_header()

st.markdown("""
### Bienvenido al Dashboard del Sistema Multiagente

Este panel de control web está diseñado para interactuar con la simulación distribuida del hospital.
El sistema operativo subyacente se basa en **Agentes Inteligentes** que negocian camas y clasifican urgencias en tiempo real.

👈 **Usa el menú de la izquierda para navegar:**
- **Monitoring:** Visualiza el gemelo digital en tiempo real y la saturación actual.
- **Analytics:** Revisa las estadísticas históricas y reportes luego de correr una simulación en la consola.
- **Simulation:** Panel explicativo sobre cómo iniciar una corrida.
""")

st.info("Para generar nuevos datos, recuerda correr `python main.py` en tu terminal o VS Code.")
