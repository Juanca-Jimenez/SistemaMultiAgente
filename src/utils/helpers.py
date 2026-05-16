from datetime import datetime

def parse_datetime(date_str: str, time_str: str) -> datetime:
    """Combina y parsea fecha y hora del dataset a datetime."""
    try:
        # Formato de ejemplo, ajustar según el dataset real
        return datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M:%S")
    except ValueError:
        try:
            return datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%dT%H:%M:%SZ %H:%M:%S")
        except:
            return None

def calculate_minutes_diff(start: datetime, end: datetime) -> int:
    if not start or not end:
        return 0
    return int((end - start).total_seconds() / 60)
