import os

# Configuración General de la Simulación
SIMULATION_TICK_MINUTES = 5 # Cada tick equivale a 5 minutos
MAX_TICKS = 1000 # Límite de seguridad
RANDOM_SEED = 42

# Rutas
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA_DIR = os.path.join(BASE_DIR, 'data')
RAW_DATA_PATH = os.path.join(DATA_DIR, 'raw', 'hospital_data.csv')
LOG_FILE = os.path.join(BASE_DIR, 'logs', 'sma_hospital.log')

LOG_LEVEL = 'INFO'

# Parámetros Hospitalarios
DEFAULT_DEPARTMENT_CAPACITY = 10
CONGESTION_THRESHOLD = 0.85 # 85% de capacidad = congestionado
MAX_WAIT_TIME_MINUTES = 120 # 2 horas máximo
