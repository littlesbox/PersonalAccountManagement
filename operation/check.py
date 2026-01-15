import pandas as pd
from pathlib import Path

def check(em, im , bm):
    base_dir = Path(__file__).resolve().parent.parent
    path = base_dir.joinpath("bill_data", "balance.csv")
    last_balance = pd.read_csv(path).iloc[-1,:]
    amount = last_balance.iloc[1:].sum()
