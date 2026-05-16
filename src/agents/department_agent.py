from src.agents.base_agent import BaseAgent
from src.communication.message import Message, MessagePerformative
from src.utils.config import DEFAULT_DEPARTMENT_CAPACITY
from src.rules.congestion_rules import calculate_congestion_level

class DepartmentAgent(BaseAgent):
    """Agente que gestiona los recursos de un departamento (ej. Cardiología)."""
    def __init__(self, agent_id: str, message_bus, capacity: int = DEFAULT_DEPARTMENT_CAPACITY):
        super().__init__(agent_id, message_bus)
        self.capacity = capacity
        self.current_patients = []
        
    def act(self, current_tick: int):
        msgs = self.receive_messages()
        for msg in msgs:
            if msg.performative == MessagePerformative.CFP:
                self._handle_cfp(msg)
            elif msg.performative == MessagePerformative.ACCEPT_PROPOSAL:
                self._admit_patient(msg)
                
        # Simulación de alta (liberación de recursos) - simple aleatorio o por tiempo
        if self.current_patients and current_tick % 12 == 0: # Cada hora aprox (12 * 5 min)
            discharged = self.current_patients.pop(0)
            self.logger.info(f"Paciente {discharged} dado de alta de {self.agent_id}")
            self.send_message(Message(
                sender=self.agent_id, receiver=discharged,
                performative=MessagePerformative.INFORM, content={"action": "discharged"}
            ))

    def _handle_cfp(self, msg: Message):
        patient_id = msg.content.get("patient_id")
        target_dept = msg.content.get("target_department")
        
        # Si soy el departamento solicitado o soy alternativo
        if target_dept == self.agent_id or target_dept == "General":
            congestion = calculate_congestion_level(len(self.current_patients), self.capacity)
            if congestion < 1.0: # Hay espacio
                reply = Message(
                    sender=self.agent_id,
                    receiver=msg.sender,
                    performative=MessagePerformative.PROPOSE,
                    content={"load": congestion, "available": True},
                    in_reply_to=msg.reply_with
                )
                self.send_message(reply)
            else:
                reply = Message(
                    sender=self.agent_id,
                    receiver=msg.sender,
                    performative=MessagePerformative.REJECT_PROPOSAL,
                    content={"load": congestion, "available": False},
                    in_reply_to=msg.reply_with
                )
                self.send_message(reply)

    def _admit_patient(self, msg: Message):
        patient_id = msg.content.get("patient_id")
        self.current_patients.append(patient_id)
        self.logger.info(f"Paciente {patient_id} admitido en {self.agent_id}. Ocupación: {len(self.current_patients)}/{self.capacity}")
        
        # Notificar al paciente
        notify = Message(
            sender=self.agent_id,
            receiver=patient_id,
            performative=MessagePerformative.INFORM,
            content={"action": "admitted", "department": self.agent_id}
        )
        self.send_message(notify)
