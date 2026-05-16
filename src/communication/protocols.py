from src.communication.message import Message
from src.utils.constants import MessagePerformative

class ProtocolBuilder:
    """Ayudante para construir respuestas según protocolos establecidos."""
    
    @staticmethod
    def create_cfp(sender: str, receivers: list, task_description: str) -> list:
        """Call For Proposal: Inicia una subasta entre departamentos."""
        messages = []
        reply_with = f"cfp_{time.time()}"
        for receiver in receivers:
            msg = Message(
                sender=sender,
                receiver=receiver,
                performative=MessagePerformative.CFP,
                content=task_description,
                reply_with=reply_with
            )
            messages.append(msg)
        return messages

    @staticmethod
    def accept_proposal(sender: str, receiver: str, content: dict, in_reply_to: str) -> Message:
        return Message(
            sender=sender,
            receiver=receiver,
            performative=MessagePerformative.ACCEPT_PROPOSAL,
            content=content,
            in_reply_to=in_reply_to
        )
        
    @staticmethod
    def reject_proposal(sender: str, receiver: str, in_reply_to: str) -> Message:
        return Message(
            sender=sender,
            receiver=receiver,
            performative=MessagePerformative.REJECT_PROPOSAL,
            content="Rejected",
            in_reply_to=in_reply_to
        )
import time
