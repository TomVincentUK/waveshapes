from .node import NodeBase
from .inlets import Inlets


class Product(NodeBase):
    """
    Multiplies all inputs.
    """

    def __init__(self, scene, outlets=None):
        super().__init__(scene, outlets)
        self.inlets = Inlets(node=self)
