from .node import NodeBase


class ArrayReader(NodeBase):
    """
    Yields an array-like object chunk-by-chunk.
    """

    def __init__(self, scene, array=None, outlets=None):
        super().__init__(scene, outlets)
        self.array = array
