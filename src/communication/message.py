import time
import uuid
from typing import Any, Dict
from src.utils.constants import MessagePerformative

class Message:
    """Clase base que representa un mensaje en la ontología FIPA-ACL."""
    def __init__(
        self, 
        sender: str, 
        receiver: str, 
        performative: MessagePerformative, 
        content: Any,
        ontology: str = "hospital_flow",
        reply_with: str = None,
        in_reply_to: str = None
    ):
        self.message_id = str(uuid.uuid4())
        self.sender = sender
        self.receiver = receiver
        self.performative = performative
        self.content = content
        self.ontology = ontology
        self.timestamp = time.time()
        self.reply_with = reply_with
        self.in_reply_to = in_reply_to

    def __str__(self):
        return f"[{self.performative.value}] {self.sender} -> {self.receiver}: {self.content}"
