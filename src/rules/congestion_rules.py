from src.utils.config import CONGESTION_THRESHOLD

def is_department_congested(current_patients: int, capacity: int) -> bool:
    """Evalúa si un departamento está congestionado basado en su capacidad."""
    if capacity <= 0:
        return True
    
    occupancy_rate = current_patients / capacity
    return occupancy_rate >= CONGESTION_THRESHOLD

def calculate_congestion_level(current_patients: int, capacity: int) -> float:
    """Retorna el nivel de ocupación."""
    if capacity <= 0:
        return 1.0
    return current_patients / capacity
