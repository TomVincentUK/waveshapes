class Inlet:
    def __init__(self, inlets):
        self.inlets = inlets


class InletsBase:
    def __init__(self, node):
        self.node = node
        self._inlets = []

    @property
    def inlets(self):
        return self._inlets

    def _add_inlet(self):
        new_inlet = Inlet(inlets=self)
        self._inlets.append(new_inlet)
        return new_inlet


class Inlets(InletsBase):
    def __init__(self, node):
        super().__init__(node)

    def __getitem__(self, name):
        return self._inlets[name]

    def new(self):
        return self._add_inlet()


class NamedInlets(InletsBase):
    def __init__(self, node, names):
        super().__init__(node)
        self.names = names
        self._index_lookup = {name: self._add_inlet() for name in self.names}

    def __getitem__(self, name):
        return self._index_lookup[name]
