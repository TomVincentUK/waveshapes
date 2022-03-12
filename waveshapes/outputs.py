from .node import NodeBase
from .inlets import NamedInlets


class DACStereo(NodeBase):
    """
    Sends two inputs to a stereo out.
    """

    def __init__(self, scene, outlets=None):
        super().__init__(scene, outlets)
        self.inlets = NamedInlets(node=self, names=("R", "L"))
