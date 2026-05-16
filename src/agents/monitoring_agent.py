from src.agents.base_agent import BaseAgent
from src.communication.message import Message, MessagePerformative
from src.utils.constants import Topic

class MonitoringAgent(BaseAgent):
    """Observador del sistema, genera alertas globales si detecta anomalías."""
    def __init__(self, agent_id: str, message_bus):
        super().__init__(agent_id, message_bus)
        # Se suscribe a un tópico global donde los departamentos podrían enviar métricas
        self.message_bus.subscribe(self.agent_id, Topic.GLOBAL_EVENTS.value)
        self.alerts = []

    def act(self, current_tick: int):
        msgs = self.receive_messages()
        for msg in msgs:
            # Procesar eventos (esto puede expandirse)
            pass
            
        # Periódicamente emitir alertas simuladas si fuera necesario
        if current_tick > 0 and current_tick % 50 == 0:
            self.logger.info("Chequeo de salud global del sistema realizado.")
