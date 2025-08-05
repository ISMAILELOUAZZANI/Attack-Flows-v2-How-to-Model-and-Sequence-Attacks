from fastapi import FastAPI, HTTPException
from app.flow_builder import AttackFlowBuilder
from app.sequencer import AttackFlowSequencer
from app.visualizer import visualize_attack_flow
from app.database import save_flow, load_flow
from app.models import AttackFlow
from typing import List

app = FastAPI()

@app.post("/flows/", response_model=AttackFlow)
def create_flow(name: str, description: str = ""):
    builder = AttackFlowBuilder(name=name, description=description)
    flow = builder.build()
    save_flow(flow)
    return flow

@app.get("/flows/{flow_id}", response_model=AttackFlow)
def get_flow(flow_id: str):
    flow_data = load_flow(flow_id)
    if not flow_data:
        raise HTTPException(status_code=404, detail="Flow not found")
    return AttackFlow.parse_obj(flow_data)

@app.get("/flows/{flow_id}/sequences")
def get_sequences(flow_id: str):
    flow_data = load_flow(flow_id)
    if not flow_data:
        raise HTTPException(status_code=404, detail="Flow not found")
    flow = AttackFlow.parse_obj(flow_data)
    sequencer = AttackFlowSequencer(flow)
    return {"sequences": sequencer.get_all_sequences()}

@app.get("/flows/{flow_id}/visualize")
def visualize(flow_id: str):
    flow_data = load_flow(flow_id)
    if not flow_data:
        raise HTTPException(status_code=404, detail="Flow not found")
    flow = AttackFlow.parse_obj(flow_data)
    pdf_path = visualize_attack_flow(flow)
    return {"pdf_path": pdf_path}