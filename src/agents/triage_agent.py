from src.agents.base_agent import BaseAgent
from src.communication.message import Message, MessagePerformative
from src.rules.priority_rules import evaluate_patient_priority

class TriageAgent(BaseAgent):
    """Agente experto que evalúa la urgencia de los pacientes."""
    def __init__(self, agent_id: str, message_bus):
        super().__init__(agent_id, message_bus)
        
    def act(self, current_tick: int):
        msgs = self.receive_messages()
        for msg in msgs:
            if msg.performative == MessagePerformative.REQUEST:
                self._process_triage(msg)

    def _process_triage(self, msg: Message):
        patient_id = msg.content.get("patient_id")
        data = msg.content.get("data")
        
        # 1. Aplicar reglas de prioridad
        priority = evaluate_patient_priority(data)
        self.logger.info(f"Paciente {patient_id} clasificado con prioridad {priority.name}")
        
        # 2. Informar al paciente que el triage terminó
        reply_patient = Message(
            sender=self.agent_id,
            receiver=patient_id,
            performative=MessagePerformative.INFORM,
            content={"action": "triage_done", "priority": priority.value}
        )
        self.send_message(reply_patient)
        
        # 3. Enviar solicitud al Coordinador para asignar cama
        req_coordinator = Message(
            sender=self.agent_id,
            receiver="CoordinatorAgent",
            performative=MessagePerformative.REQUEST,
            content={
                "action": "assign_department",
                "patient_id": patient_id,
                "priority": priority.value,
                "data": data
            }
        )
        self.send_message(req_coordinator)
