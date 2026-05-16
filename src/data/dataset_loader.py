import pandas as pd
# pyrefly: ignore [missing-import]
import numpy as np
import os
from src.utils.logger import get_logger

logger = get_logger("DatasetLoader")

class DatasetLoader:
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.data = None

    def load_and_clean(self) -> pd.DataFrame:
        if not os.path.exists(self.filepath):
            logger.error(f"Dataset no encontrado en {self.filepath}")
            # Retornar un dataset falso por si queremos probar sin el real
            return self._generate_mock_data()
            
        logger.info(f"Cargando dataset desde {self.filepath}")
        df = pd.read_csv(self.filepath)
        
        # Limpieza básica
        df.columns = [c.strip().lower().replace(' ', '_') for c in df.columns]
        
        required_cols = [
            'patient_id', 'patient_admission_date', 'patient_admission_time',
            'department_referral', 'patient_waittime'
        ]
        
        for col in required_cols:
            if col not in df.columns:
                logger.warning(f"Columna {col} no encontrada en el dataset.")
        
        # Eliminar duplicados
        df = df.drop_duplicates()
        
        # Manejo de nulos básicos (se asume 0 para tiempos o 'Unknown' para cats)
        if 'patient_waittime' in df.columns:
            df['patient_waittime'] = df['patient_waittime'].fillna(0)
            
        if 'department_referral' in df.columns:
            df['department_referral'] = df['department_referral'].fillna('General')
            
        # Ordenar por fecha y hora de admisión
        if 'patient_admission_date' in df.columns and 'patient_admission_time' in df.columns:
            df['datetime'] = pd.to_datetime(df['patient_admission_date'] + ' ' + df['patient_admission_time'], errors='coerce')
            df = df.dropna(subset=['datetime'])
            df = df.sort_values('datetime')
            
        self.data = df
        logger.info(f"Dataset cargado con {len(df)} registros.")
        return df

    def _generate_mock_data(self) -> pd.DataFrame:
        """Genera datos de prueba si no existe el archivo CSV."""
        logger.info("Generando datos simulados (Mock).")
        dates = pd.date_range("2023-01-01 08:00:00", periods=100, freq="15min")
        
        df = pd.DataFrame({
            'patient_id': range(1, 101),
            'patient_admission_date': dates.strftime('%Y-%m-%d'),
            'patient_admission_time': dates.strftime('%H:%M:%S'),
            'patient_gender': np.random.choice(['M', 'F'], 100),
            'patient_age': np.random.randint(1, 90, 100),
            'department_referral': np.random.choice(['Cardiology', 'Neurology', 'General', 'Orthopedics'], 100),
            'patient_admission_flag': np.random.choice([True, False], 100),
            'patient_waittime': np.random.randint(0, 120, 100)
        })
        df['datetime'] = pd.to_datetime(df['patient_admission_date'] + ' ' + df['patient_admission_time'])
        return df
