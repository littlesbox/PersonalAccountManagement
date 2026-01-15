import pandas as pd
from pathlib import Path

base_dir = Path(__file__).resolve().parent
path = base_dir.joinpath("bill_data", "balance.csv")
last_balance = pd.read_csv(path).iloc[-1]
a = last_balance.iloc[1:].sum()