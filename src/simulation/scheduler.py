import time
from src.utils.logger import get_logger

class Scheduler:
    """Controla el avance temporal de la simulación."""
    def __init__(self, max_ticks: int = 100):
        self.current_tick = 0
        self.max_ticks = max_ticks
        self.agents = []
        self.logger = get_logger("Scheduler")

    def register_agent(self, agent):
        self.agents.append(agent)
        
    def step(self):
        """Ejecuta un tick de la simulación."""
        if self.current_tick >= self.max_ticks:
            return False
            
        self.logger.debug(f"--- Tick {self.current_tick} ---")
        
        for agent in self.agents:
            agent.act(self.current_tick)
            
        self.current_tick += 1
        return True

    def run(self):
        self.logger.info("Iniciando simulación...")
        while self.step():
            pass # Loop hasta terminar max_ticks o condición
        self.logger.info("Simulación terminada.")
