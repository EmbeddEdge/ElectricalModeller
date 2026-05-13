from electrical_system.base import Edge

class Breaker(Edge):
    """
    Represents a circuit breaker for overcurrent and short-circuit protection.
    It links two nodes but generally assumes negligible steady-state impedance.
    """
    def __init__(self, name: str, source_node: str, target_node: str,
                 nominal_current_a: float, curve_type: str, short_circuit_capacity_ka: float):
        super().__init__(name, source_node, target_node)
        self.nominal_current_a = nominal_current_a
        self.curve_type = curve_type
        self.short_circuit_capacity_ka = short_circuit_capacity_ka
        
        # TODO for future phases:
        # - Add I2t let-through energy properties and specific manufacturer frame sizes.
        # - Add time-current characteristic curve definitions (or reference to standards/breaker_curves.py).
