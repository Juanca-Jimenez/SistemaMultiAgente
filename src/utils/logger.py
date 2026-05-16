import logging
import os
from src.utils.config import LOG_LEVEL, LOG_FILE

def get_logger(name: str):
    """Retorna un logger configurado."""
    logger = logging.getLogger(name)
    
    if not logger.handlers:
        logger.setLevel(getattr(logging, LOG_LEVEL))
        
        formatter = logging.Formatter(
            '%(asctime)s - [%(name)s] - %(levelname)s - %(message)s'
        )
        
        # Consola
        ch = logging.StreamHandler()
        ch.setFormatter(formatter)
        logger.addHandler(ch)
        
        # Archivo
        if LOG_FILE:
            os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
            fh = logging.FileHandler(LOG_FILE)
            fh.setFormatter(formatter)
            logger.addHandler(fh)
            
    return logger
