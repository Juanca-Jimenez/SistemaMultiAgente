from typing import List

def calculate_average_wait_time(wait_times: List[int]) -> float:
    if not wait_times:
        return 0.0
    return sum(wait_times) / len(wait_times)

def calculate_department_occupancy(current: int, capacity: int) -> float:
    if capacity <= 0:
        return 0.0
    return (current / capacity) * 100
