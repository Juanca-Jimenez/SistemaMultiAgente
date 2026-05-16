# Sistema Multiagente para Optimización de Flujo Hospitalario

## Descripción del Proyecto
Este es un verdadero **Sistema Multiagente (SMA)** desarrollado en Python que busca la optimización inteligente del flujo hospitalario. No es un modelo predictivo descriptivo, ni un chatbot, sino un sistema distribuido donde entidades autónomas (agentes) cooperan y negocian mediante paso de mensajes para priorizar y distribuir a los pacientes.

## Arquitectura Modular

* **Agent Core (`src/agents`)**: Contiene agentes especializados (Patient, Triage, Coordinator, Department, Monitoring).
* **Communication (`src/communication`)**: Implementación del patrón *Message Bus* utilizando performativas FIPA-ACL (REQUEST, PROPOSE, CFP).
* **Rules (`src/rules`)**: Motores lógicos desacoplados para determinar prioridad (Triage) y niveles de congestión.
* **Simulation (`src/simulation`)**: Ciclo de vida impulsado por un *Scheduler* que avanza de manera discreta permitiendo eventos dinámicos.
* **Data (`src/data`)**: Ingesta y limpieza del dataset mediante Pandas.
* **Dashboard (`dashboard`)**: Interfaz analítica visual utilizando Streamlit.

## Ejecución

1. **Instalación de Dependencias**:
   ```bash
   pip install -r requirements.txt
   ```
2. **Ejecutar la Simulación Multiagente**:
   ```bash
   python main.py
   ```
   *Esto generará la actividad de los agentes en la terminal y escribirá los eventos detallados en `logs/sma_hospital.log`.*

3. **Ejecutar el Dashboard (Streamlit)**:
   ```bash
   streamlit run dashboard/app.py
   ```