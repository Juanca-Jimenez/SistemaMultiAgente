import pandas as pd
from src.agents.patient_agent import PatientAgent
from src.utils.logger import get_logger

class EventGenerator:
    """Genera instancias de PatientAgent a lo largo del tiempo basado en el dataset."""
    def __init__(self, dataset: pd.DataFrame, message_bus):
        self.dataset = dataset
        self.message_bus = message_bus
        self.current_index = 0
        self.logger = get_logger("EventGenerator")

    def get_new_patients(self, current_tick: int, max_per_tick: int = 5) -> list:
        new_agents = []
        # En una simulación real ligada al tiempo, checaríamos df['datetime'] vs tick.
        # Por simplicidad en este MVP, sacamos un lote por tick:
        start = self.current_index
        end = min(self.current_index + max_per_tick, len(self.dataset))
        
        for i in range(start, end):
            row = self.dataset.iloc[i].to_dict()
            agent_id = f"Patient_{row.get('patient_id', i)}"
            p_agent = PatientAgent(agent_id=agent_id, message_bus=self.message_bus, patient_data=row)
            new_agents.append(p_agent)
            
        self.current_index = end
        return new_agents
        
    def is_finished(self):
        return self.current_index >= len(self.dataset)
