def get_best_alternative_department(departments_status: dict) -> str:
    """
    Busca el departamento con menor nivel de congestión.
    departments_status = {"Cardiology": 0.5, "General": 0.2}
    """
    if not departments_status:
        return None
        
    best_dept = min(departments_status, key=departments_status.get)
    # Si el mejor departamento también está congestionado, igual lo retorna pero en la lógica del Coordinador se puede rechazar
    return best_dept
