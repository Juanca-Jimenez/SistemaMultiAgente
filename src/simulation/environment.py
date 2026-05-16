class HospitalEnvironment:
    """Mantiene el estado global del hospital y de los departamentos."""
    def __init__(self, departments_config: dict):
        self.departments = departments_config # {"Cardiology": {"capacity": 10}, ...}
        self.active_patients = {} # {id: agent_instance}
        self.stats = {"total_admissions": 0, "total_discharges": 0}

    def get_department_list(self) -> list:
        return list(self.departments.keys())
        
    def add_patient(self, patient):
        self.active_patients[patient.agent_id] = patient
        
    def remove_patient(self, patient_id):
        if patient_id in self.active_patients:
            del self.active_patients[patient_id]
            self.stats["total_discharges"] += 1
