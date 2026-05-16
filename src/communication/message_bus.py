from collections import defaultdict
from queue import Queue
from src.communication.message import Message
from src.utils.logger import get_logger

logger = get_logger("MessageBus")

class MessageBus:
    """Implementa un bus de mensajes para la comunicación asíncrona entre agentes."""
    def __init__(self):
        # Colas de mensajes punto a punto (inbox por agente)
        self.inboxes = defaultdict(Queue)
        # Topics para pub/sub (ej. alertas globales)
        self.topics = defaultdict(list)

    def register_agent(self, agent_id: str):
        """Registra un agente en el bus."""
        if agent_id not in self.inboxes:
            self.inboxes[agent_id] = Queue()
            logger.debug(f"Agente registrado: {agent_id}")

    def subscribe(self, agent_id: str, topic: str):
        """Suscribe un agente a un tópico."""
        if agent_id not in self.topics[topic]:
            self.topics[topic].append(agent_id)
            logger.debug(f"Agente {agent_id} suscrito al tópico {topic}")

    def send(self, message: Message):
        """Envía un mensaje punto a punto o por broadcast a un tópico."""
        if message.receiver.startswith("TOPIC_"):
            topic_name = message.receiver.replace("TOPIC_", "")
            self._publish(topic_name, message)
        else:
            if message.receiver in self.inboxes:
                self.inboxes[message.receiver].put(message)
                logger.debug(f"Mensaje enviado: {message}")
            else:
                logger.warning(f"Destinatario no encontrado: {message.receiver}")

    def _publish(self, topic: str, message: Message):
        if topic in self.topics:
            for agent_id in self.topics[topic]:
                self.inboxes[agent_id].put(message)
            logger.debug(f"Mensaje publicado en {topic}: {message}")

    def receive(self, agent_id: str) -> Message:
        """Extrae el siguiente mensaje del inbox del agente (no bloqueante)."""
        if agent_id in self.inboxes and not self.inboxes[agent_id].empty():
            return self.inboxes[agent_id].get()
        return None
