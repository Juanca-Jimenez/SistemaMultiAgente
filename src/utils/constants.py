from enum import Enum

class PatientState(Enum):
    NEW = "NEW"
    WAITING_TRIAGE = "WAITING_TRIAGE"
    WAITING_ADMISSION = "WAITING_ADMISSION"
    IN_TREATMENT = "IN_TREATMENT"
    DISCHARGED = "DISCHARGED"

class Priority(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4

class MessagePerformative(Enum):
    INFORM = "INFORM"
    REQUEST = "REQUEST"
    PROPOSE = "PROPOSE"
    ACCEPT_PROPOSAL = "ACCEPT_PROPOSAL"
    REJECT_PROPOSAL = "REJECT_PROPOSAL"
    CFP = "CFP" # Call for Proposal
    FAILURE = "FAILURE"

class Topic(Enum):
    GLOBAL_EVENTS = "GLOBAL_EVENTS"
    HOSPITAL_ALERTS = "HOSPITAL_ALERTS"
