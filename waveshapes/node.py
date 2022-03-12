import numpy as np


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

        self._init_outlet_buffer()

        if outlets is None:
            self.outlets = []
        else:
            self.outlets = list(outlets)
        self._register_outlets()

        self.inlets = None

    @property
    def sample_rate(self):
        return self.scene.sample_rate

    @property
    def chunk_size(self):
        return self.scene.chunk_size

    def _init_outlet_buffer(self):
        self.outlet_buffer = np.zeros(self.chunk_size)

    def _register_outlets(self):
        """
        Let outlets know that this node is pointing at them.
        """
        for outlet in self.outlets:
            outlet.set_origin(self)
