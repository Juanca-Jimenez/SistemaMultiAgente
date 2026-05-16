from src.agents.base_agent import BaseAgent
from src.utils.constants import PatientState
from src.communication.message import Message, MessagePerformative

class PatientAgent(BaseAgent):
    """Agente que representa a un paciente en el sistema."""
    def __init__(self, agent_id: str, message_bus, patient_data: dict):
        super().__init__(agent_id, message_bus)
        self.data = patient_data
        self.state = PatientState.NEW
        self.wait_time = patient_data.get('patient_waittime', 0)
        self.assigned_department = None

    def act(self, current_tick: int):
        msgs = self.receive_messages()
        for msg in msgs:
            if msg.performative == MessagePerformative.INFORM:
                if msg.content.get("action") == "triage_done":
                    self.state = PatientState.WAITING_ADMISSION
                elif msg.content.get("action") == "admitted":
                    self.state = PatientState.IN_TREATMENT
                    self.assigned_department = msg.content.get("department")
                elif msg.content.get("action") == "discharged":
                    self.state = PatientState.DISCHARGED

        # Si es nuevo, solicita triage
        if self.state == PatientState.NEW:
            self._request_triage()
            self.state = PatientState.WAITING_TRIAGE
            
        # Si está esperando, incrementa su tiempo de espera
        if self.state in [PatientState.WAITING_TRIAGE, PatientState.WAITING_ADMISSION]:
            self.wait_time += 5 # Incremento por tick

    def _request_triage(self):
        msg = Message(
            sender=self.agent_id,
            receiver="TriageAgent",
            performative=MessagePerformative.REQUEST,
            content={"patient_id": self.agent_id, "data": self.data}
        )
        self.send_message(msg)
