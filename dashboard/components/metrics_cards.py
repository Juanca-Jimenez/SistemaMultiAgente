import streamlit as st

def render_metric_card(title: str, value: str, delta: str = None, help_text: str = None):
    """Renderiza una tarjeta de métrica estilizada."""
    st.metric(
        label=title,
        value=value,
        delta=delta,
        help=help_text
    )

def render_dashboard_header():
    """Renderiza la cabecera general del dashboard."""
    st.markdown(
        """
        <style>
        .main-title {
            font-size: 2.5rem;
            font-weight: 700;
            color: #1E3A8A;
            margin-bottom: 0px;
        }
        .sub-title {
            font-size: 1.1rem;
            color: #6B7280;
            margin-bottom: 2rem;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.markdown('<p class="main-title">🏥 Sistema Multiagente Hospitalario</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">Monitorización distribuida y optimización de flujos de pacientes</p>', unsafe_allow_html=True)
    st.divider()
