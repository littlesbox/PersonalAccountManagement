from pathlib import Path
import json
import pandas as pd

class BalanceManager:
    def __init__(self):
        self.balance = {}
        self.bm_id = 1
        self.balance_class = {}


    def add(self, data):
        self.balance[self.bm_id] = data
        self.balance_class[self.bm_id] = BalanceManager.classification(data)
        self.bm_id += 1

    def display(self):
        for key, value in self.balance.items():
            print(f"{key}: {value}")

    def display_class(self):
        for key, value in self.balance_class.items():
            print(f"id是 {key} {value[0]}")
            print(f"负债端为： {value[1]}")
            print(f"流动资产： {value[2]}")
            print(f"非流动资产 {value[3]}")

    def delete(self, bm_id):
        self.balance.pop(bm_id)

    def modify(self, bm_id, title, value):
        self.balance[bm_id][title] = value

    @staticmethod
    def classification(data):
        base_dir = Path(__file__).resolve().parent.parent
        path = base_dir.joinpath("table_header", "balance.json")
        with open(path, "r", encoding="utf-8") as f:
            elements = json.load(f)
        Date = elements["Date"]
        Liabilities = elements["Liabilities"]
        CurrentAssets = elements["CurrentAssets"]
        NonCurrentAssets = elements["NonCurrentAssets"]
        bl_D = { k:data[k] for k in Date}
        bl_L = {k:data[k] for k in Liabilities}
        bl_CA = {k:data[k] for k in CurrentAssets}
        bl_NCA = {k:data[k] for k in NonCurrentAssets}
        balance_class = [bl_D, bl_L, bl_CA, bl_NCA]
        return balance_class

    def save(self):
        base_dir = Path(__file__).resolve().parent.parent
        output_dir = base_dir.joinpath("tables", "expenditure.csv")
        df = pd.DataFrame.from_dict(self.balance, orient="index")
        df["日期"] = pd.to_datetime(df["日期"], format="%Y%m%d")
        df = df.sort_values("日期")
        df.to_csv(output_dir, index=False, encoding="utf-8-sig")


if __name__ == "__main__":
    balance_manager = BalanceManager()
    data= {'日期':'20250303','花呗': 0, '白条': 0, '抖音月付': 0,
           '美团月付': 0, '抖音放心借': 0, '微信': 0, 
           '余额宝': 0, '浦发': 0, '工商': 0, '建行': 0, 
           '农信': 0, '光大': 0, '京东钱包': 0, '定期存款': 0, 
           '理财投资': 0, '借出': 0}
    balance_manager.add(data)
    balance_manager.display_class()