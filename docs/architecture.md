# Architecture – Attack Flows v2

## Components

- **models.py**: Data models for AttackStep, AttackFlow
- **flow_builder.py**: Helper to construct flows programmatically
- **sequencer.py**: Generates valid attack sequences from flows
- **visualizer.py**: Renders flows as graphs (PDF/SVG)
- **database.py**: Simple JSON file persistence
- **API**: FastAPI endpoints for interacting with flows

## Data Flow

1. Create an attack flow (define steps, edges)
2. Save flow (JSON file)
3. Analyze sequences (all possible paths)
4. Visualize as a graph

## Extending

- Replace JSON with MongoDB or another DB for scalability
- Add user authentication and flow access controls
- Integrate MITRE ATT&CK step templates
- Support for probabilistic or weighted attack steps