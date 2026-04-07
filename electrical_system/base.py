from abc import ABC

class Edge(ABC):
    """
    Base class representing a branch in the electrical circuit.
    Examples: Cables, Circuit Breakers.
    
    Edges typically possess impedance and carry current between two Nodes.
    """
    def __init__(self, name: str, source_node: str, target_node: str):
        self.name = name
        self.source_node = source_node
        self.target_node = target_node


class Node(ABC):
    """
    Base class representing a bus or connection point in the electrical circuit.
    Examples: Transformers, Distribution Boards, Loads.
    
    Nodes act as junctions and typically define a voltage level.
    """
    def __init__(self, name: str, nominal_voltage: float):
        self.name = name
        self.nominal_voltage = nominal_voltage
