from src.agents.base_agent import BaseAgent
from src.communication.message import Message, MessagePerformative
from src.communication.protocols import ProtocolBuilder

class CoordinatorAgent(BaseAgent):
    """Agente central que enruta y balancea a los pacientes en los departamentos."""
    def __init__(self, agent_id: str, message_bus, departments: list):
        super().__init__(agent_id, message_bus)
        self.departments = departments
        self.pending_patients = []
        self.active_cfps = {} # {reply_with: {"patient_id": id, "proposals": []}}

    def act(self, current_tick: int):
        msgs = self.receive_messages()
        for msg in msgs:
            if msg.performative == MessagePerformative.REQUEST and msg.content.get("action") == "assign_department":
                self._handle_assignment_request(msg)
            elif msg.performative == MessagePerformative.PROPOSE:
                self._handle_proposal(msg)
            elif msg.performative == MessagePerformative.REJECT_PROPOSAL:
                pass # Ignorar rechazos por ahora
                
        self._evaluate_cfps()

    def _handle_assignment_request(self, msg: Message):
        patient_id = msg.content.get("patient_id")
        data = msg.content.get("data")
        target_dept = data.get("department_referral", "General")
        
        self.logger.info(f"Iniciando subasta para paciente {patient_id} destinado a {target_dept}")
        
        # Enviar CFP a todos los departamentos
        cfp_msgs = ProtocolBuilder.create_cfp(
            sender=self.agent_id,
            receivers=self.departments,
            task_description={"patient_id": patient_id, "target_department": target_dept}
        )
        
        reply_with_id = cfp_msgs[0].reply_with
        self.active_cfps[reply_with_id] = {
            "patient_id": patient_id,
            "target_dept": target_dept,
            "proposals": [],
            "ticks_waiting": 0
        }
        
        for m in cfp_msgs:
            self.send_message(m)

    def _handle_proposal(self, msg: Message):
        reply_to = msg.in_reply_to
        if reply_to in self.active_cfps:
            self.active_cfps[reply_to]["proposals"].append({
                "dept": msg.sender,
                "load": msg.content.get("load")
            })

    def _evaluate_cfps(self):
        to_remove = []
        for cfp_id, cfp_data in self.active_cfps.items():
            cfp_data["ticks_waiting"] += 1
            # Esperamos 1 tick para recolectar respuestas
            if cfp_data["ticks_waiting"] > 1:
                proposals = cfp_data["proposals"]
                patient_id = cfp_data["patient_id"]
                
                if proposals:
                    # Elegir el que tenga menor carga
                    best_dept = min(proposals, key=lambda x: x["load"])["dept"]
                    
                    self.logger.info(f"Asignando paciente {patient_id} a {best_dept}")
                    accept_msg = ProtocolBuilder.accept_proposal(
                        sender=self.agent_id,
                        receiver=best_dept,
                        content={"patient_id": patient_id},
                        in_reply_to=cfp_id
                    )
                    self.send_message(accept_msg)
                else:
                    self.logger.warning(f"Ningún departamento aceptó al paciente {patient_id}")
                    # Posible lógica de reintento futura
                    
                to_remove.append(cfp_id)
                
        for r in to_remove:
            del self.active_cfps[r]
