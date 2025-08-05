import unittest
from app.flow_builder import AttackFlowBuilder
from app.sequencer import AttackFlowSequencer

class TestAttackFlows(unittest.TestCase):
    def test_sequence_generation(self):
        builder = AttackFlowBuilder("Test Flow")
        step1 = builder.add_step("Phishing Email", "Initial compromise")
        step2 = builder.add_step("Credential Theft")
        step3 = builder.add_step("Privilege Escalation")
        builder.add_edge(step1, step2)
        builder.add_edge(step2, step3)
        flow = builder.build()

        sequencer = AttackFlowSequencer(flow)
        sequences = sequencer.get_all_sequences()
        self.assertTrue([step1, step2, step3] in sequences)

if __name__ == "__main__":
    unittest.main()