import numpy as np


class Inlet:
    """
    Object that takes data from a node's output buffer when it
    becomes ready.
    """

    def __init__(self, inlets):
        self.inlets = inlets

    def set_origin(self, node):
        self.origin = node
        self.buffer = np.zeros_like(self.origin.outlet_buffer)


class InletsBase:
    """
    Base class for inlets objects which hold instances of `Inlet`.
    """

    def __init__(self, node):
        self.node = node
        self._inlets = []

    def __iter__(self):
        return iter(self._inlets)

    def _add_inlet(self):
        new_inlet = Inlet(inlets=self)
        self._inlets.append(new_inlet)
        return new_inlet


class Inlets(InletsBase):
    """
    Container class for `Inlets` objects for nodes that take an
    arbitrary amount of inlets.
    """

    def __init__(self, node):
        super().__init__(node)

    def __getitem__(self, i):
        return self._inlets[i]

    def new(self):
        return self._add_inlet()


class NamedInlets(InletsBase):
    """
    Container class for `Inlets` objects for nodes that take an
    defined amount of named inlets.
    """

    def __init__(self, node, names):
        super().__init__(node)
        self.names = names
        self._index_lookup = {name: self._add_inlet() for name in self.names}

    def __getitem__(self, name):
        return self._index_lookup[name]
