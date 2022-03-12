class Scene:
    def __init__(self, sample_rate=44100, chunk_size=64):
        self.sample_rate = sample_rate
        self.chunk_size = chunk_size
        self.nodes = []

    def add_node(self, node):
        if node not in self.nodes:
            self.nodes.append(node)

    def run(self, duration=1):
        print("I am pretending to run")
