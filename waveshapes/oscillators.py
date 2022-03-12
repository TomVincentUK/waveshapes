from .node import NodeBase
from .inlets import NamedInlets


class Sine(NodeBase):
    """
    Sine wave oscillator.
    """

    def __init__(self, scene, outlets=None):
        super().__init__(scene, outlets)
        self.inlets = NamedInlets(node=self, names=("freq",))
