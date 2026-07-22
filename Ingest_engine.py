import numpy as np
import pandas as pd

# Load structural schema
df = pd.read_csv("data_schema.csv")

# Parse regional vectors
for idx, row in df.iterrows():
    node = row["node_id"]
    x_val = row["displacement_m"]
    s_val = row["stress_mpa"]

    # Map directly to network
    if node == "WASATCH":
        # Seed Node 1 tracking state
        print(f"W Ingested: {x_val}m")
    elif node == "ANTARCTICA":
        # Seed Node 2 tracking state
        print(f"A Ingested: {x_val}m")
    elif node == "MID_ATLANTIC":
        # Seed Node 3 tracking state
        print(f"V Ingested: {x_val}m")
