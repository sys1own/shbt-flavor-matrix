import anyon_simulator
from pathlib import Path

class AnomalyClosureError(Exception):
    """Raised when unphysical phase space drift is detected."""
    pass

class FlavorOrchestrator:
    def run_simulation(self, iterations=100):
        try:
            return anyon_simulator.compute_matrix_loop(iterations)
        except Exception as e:
            raise AnomalyClosureError(f"Drift detected: {e}")
