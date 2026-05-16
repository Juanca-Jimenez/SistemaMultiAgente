class SystemStatistics:
    def __init__(self):
        self.total_patients_processed = 0
        self.total_patients_rejected = 0
        self.wait_times = []
        self.department_loads = {} # {time: {dept: load}}

    def record_patient(self, wait_time: int):
        self.total_patients_processed += 1
        self.wait_times.append(wait_time)
        
    def record_rejection(self):
        self.total_patients_rejected += 1

    def record_department_load(self, tick: int, dept: str, load: float):
        if tick not in self.department_loads:
            self.department_loads[tick] = {}
        self.department_loads[tick][dept] = load
