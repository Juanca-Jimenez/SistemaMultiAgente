import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

def draw_congestion_bar_chart(df: pd.DataFrame):
    """Dibuja un gráfico de barras mostrando la congestión por departamento."""
    fig = px.bar(
        df, 
        x='Departamento', 
        y='Nivel Congestión (%)',
        color='Nivel Congestión (%)',
        color_continuous_scale='RdYlGn_r',
        title="Ocupación Actual por Departamento",
        labels={'Nivel Congestión (%)': 'Ocupación (%)'}
    )
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=20, r=20, t=40, b=20)
    )
    return fig

def draw_wait_time_trend(times_series: list):
    """Dibuja una línea de tendencia simulada para los tiempos de espera."""
    df = pd.DataFrame({"Tiempo": range(len(times_series)), "Espera (min)": times_series})
    fig = px.line(df, x='Tiempo', y='Espera (min)', title="Evolución del Tiempo de Espera")
    fig.update_traces(line_color='#2563EB', line_width=3)
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)'
    )
    return fig
