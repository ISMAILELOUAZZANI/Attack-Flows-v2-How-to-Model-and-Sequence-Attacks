import networkx as nx

class AttackFlowSequencer:
    def __init__(self, flow):
        self.flow = flow
        self.graph = nx.DiGraph()
        self._build_graph()

    def _build_graph(self):
        for step in self.flow.steps:
            self.graph.add_node(step.id, name=step.name)
        for frm, to in self.flow.edges:
            self.graph.add_edge(frm, to)

    def get_all_sequences(self):
        # Returns all valid attack sequences (paths from roots to leaves)
        roots = [n for n in self.graph.nodes if self.graph.in_degree(n) == 0]
        leaves = [n for n in self.graph.nodes if self.graph.out_degree(n) == 0]
        sequences = []
        for root in roots:
            for leaf in leaves:
                for path in nx.all_simple_paths(self.graph, root, leaf):
                    sequences.append(path)
        return sequences