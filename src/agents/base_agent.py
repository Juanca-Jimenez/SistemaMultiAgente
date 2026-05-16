from abc import ABC, abstractmethod
from src.communication.message_bus import MessageBus
from src.utils.logger import get_logger

class BaseAgent(ABC):
    """Clase base para todos los agentes del SMA."""
    def __init__(self, agent_id: str, message_bus: MessageBus):
        self.agent_id = agent_id
        self.message_bus = message_bus
        self.logger = get_logger(self.agent_id)
        
        # Auto-registro en el bus
        self.message_bus.register_agent(self.agent_id)

    def send_message(self, message):
        self.message_bus.send(message)

    def receive_messages(self):
        """Lee todos los mensajes en el inbox."""
        messages = []
        while True:
            msg = self.message_bus.receive(self.agent_id)
            if not msg:
                break
            messages.append(msg)
        return messages

    @abstractmethod
    def act(self, current_tick: int):
        """Método principal que se ejecuta en cada ciclo de la simulación."""
        pass
