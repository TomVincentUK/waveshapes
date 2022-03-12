class NodeBase:
    """
    Abstract base class for DSP nodes.
    """

    def __init__(self, scene, outlets=None):
        # In future I may want to account for people switching nodes
        # between scenes after their creation, which will need some
        # more thought about protection/warnings.
        # For now, I'll assume that the only way to link a node to a
        # scene is by initializing the Node object.
        self.scene = scene
        self.scene.add_node(self)

    @property
    def sample_rate(self):
        return self.scene.sample_rate

    @property
    def chunk_size(self):
        return self.scene.chunk_size
