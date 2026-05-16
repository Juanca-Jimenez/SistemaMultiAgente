import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.data.dataset_loader import DatasetLoader
from src.communication.message_bus import MessageBus
from src.agents.triage_agent import TriageAgent
from src.agents.coordinator_agent import CoordinatorAgent
from src.agents.department_agent import DepartmentAgent
from src.agents.monitoring_agent import MonitoringAgent
from src.simulation.scheduler import Scheduler
from src.simulation.patient_generator import EventGenerator
from src.utils.config import RAW_DATA_PATH, MAX_TICKS

def main():
    print("Iniciando SMA Hospitalario...")
    
    # 1. Cargar Datos
    loader = DatasetLoader(RAW_DATA_PATH)
    df = loader.load_and_clean()
    
    # 2. Inicializar Core del SMA
    message_bus = MessageBus()
    scheduler = Scheduler(max_ticks=MAX_TICKS)
    
    # 3. Crear Agentes del Sistema
    triage = TriageAgent("TriageAgent", message_bus)
    monitoring = MonitoringAgent("MonitoringAgent", message_bus)
    
    departments = ["Cardiology", "Neurology", "General", "Orthopedics"]
    dept_agents = []
    for dept in departments:
        # Capacidad aleatoria o por config para el ejemplo
        agent = DepartmentAgent(dept, message_bus, capacity=10)
        dept_agents.append(agent)
        
    coordinator = CoordinatorAgent("CoordinatorAgent", message_bus, departments)
    
    # Registrar agentes base en el scheduler
    scheduler.register_agent(triage)
    scheduler.register_agent(coordinator)
    for da in dept_agents:
        scheduler.register_agent(da)
    scheduler.register_agent(monitoring)
    
    # 4. Iniciar Generador de Eventos (Pacientes)
    event_gen = EventGenerator(df, message_bus)
    
    # 5. Ejecutar Simulación
    print("Corriendo simulación (Event Loop)...")
    while not event_gen.is_finished() and scheduler.current_tick < MAX_TICKS:
        # Generar nuevos pacientes
        new_patients = event_gen.get_new_patients(scheduler.current_tick, max_per_tick=3)
        for p in new_patients:
            scheduler.register_agent(p)
            
        # Ejecutar ciclo de los agentes
        scheduler.step()
        
    print("Simulación finalizada. Logs generados en /logs")

if __name__ == "__main__":
    main()
