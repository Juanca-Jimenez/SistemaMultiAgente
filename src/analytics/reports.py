import json
import os
from src.utils.config import BASE_DIR
from src.analytics.statistics import SystemStatistics
from src.analytics.metrics import calculate_average_wait_time

def generate_summary_report(stats: SystemStatistics):
    report = {
        "total_processed": stats.total_patients_processed,
        "total_rejected": stats.total_patients_rejected,
        "average_wait_time": calculate_average_wait_time(stats.wait_times)
    }
    
    os.makedirs(os.path.join(BASE_DIR, 'logs'), exist_ok=True)
    report_path = os.path.join(BASE_DIR, 'logs', 'summary_report.json')
    
    with open(report_path, 'w') as f:
        json.dump(report, f, indent=4)
        
    return report_path
