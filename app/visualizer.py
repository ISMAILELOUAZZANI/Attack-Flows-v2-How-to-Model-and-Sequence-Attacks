import graphviz

def visualize_attack_flow(flow, path="attack_flow.gv"):
    dot = graphviz.Digraph(comment=flow.name)
    for step in flow.steps:
        dot.node(step.id, f"{step.name}\n{step.description}")
    for frm, to in flow.edges:
        dot.edge(frm, to)
    dot.render(path, view=False)
    return path + ".pdf"