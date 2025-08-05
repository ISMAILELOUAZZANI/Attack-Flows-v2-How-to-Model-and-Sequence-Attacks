from .models import AttackFlow, AttackStep

class AttackFlowBuilder:
    def __init__(self, name, description=""):
        self.flow = AttackFlow(name=name, description=description, steps=[], edges=[])

    def add_step(self, name, description="", prerequisites=None, effects=None):
        step = AttackStep(
            name=name, description=description,
            prerequisites=prerequisites or [],
            effects=effects or []
        )
        self.flow.steps.append(step)
        return step.id

    def add_edge(self, from_step_id, to_step_id):
        self.flow.edges.append((from_step_id, to_step_id))

    def build(self):
        return self.flow