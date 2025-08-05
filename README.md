# Attack Flows v2 – How to Model and Sequence Attacks

A Python framework to model, sequence, analyze, and visualize cyberattack flows.

## Features

- Define attack steps, flows, and sequences
- Store and retrieve flows from database (JSON/NoSQL)
- Visualize flows as graphs (using graphviz)
- REST API for flow creation and analysis

## Quick Start

1. Install requirements:  
   `pip install -r requirements.txt`
2. Run the API server:  
   `uvicorn api.main:app --reload`
3. Explore `/docs` for API usage

See `docs/architecture.md` for more details.