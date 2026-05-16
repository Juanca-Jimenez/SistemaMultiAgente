from src.utils.constants import Priority

def evaluate_patient_priority(patient_data: dict) -> Priority:
    """
    Evalúa la prioridad de un paciente basado en reglas clínicas simples.
    """
    age = patient_data.get('patient_age', 30)
    wait_time = patient_data.get('patient_waittime', 0)
    is_admission = patient_data.get('patient_admission_flag', False)
    
    score = 0
    
    if age > 65:
        score += 2
    elif age < 12:
        score += 1
        
    if is_admission:
        score += 3
        
    if wait_time > 60:
        score += 1
    if wait_time > 120:
        score += 2
        
    if score >= 5:
        return Priority.CRITICAL
    elif score >= 3:
        return Priority.HIGH
    elif score >= 1:
        return Priority.MEDIUM
    else:
        return Priority.LOW
