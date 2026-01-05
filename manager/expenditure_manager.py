import pandas as pd
from pathlib import Path

class ExpenditureManager:
    def __init__(self):
        self.expenditure = {}
        self.em_id = 1

    def add(self, data):
        self.expenditure[self.em_id] = data
        self.em_id += 1

    def display(self):
        for key, value in self.expenditure.items():
            print(f"{key}: {value}")

    def delete(self, em_id):
        self.expenditure.pop(em_id)

    def modify(self, em_id, title, value):
        self.expenditure[em_id][title] = value

    def save(self):
        base_dir = Path(__file__).resolve().parent.parent
        output_dir = base_dir.joinpath("tables", "expenditure.csv")
        df = pd.DataFrame.from_dict(self.expenditure, orient="index")
        df["日期"] = pd.to_datetime(df["日期"], format="%Y%m%d")
        df = df.sort_values("日期")
        df.to_csv(output_dir, index=False, encoding="utf-8-sig")


if __name__ == '__main__':
    expenditure_manager = ExpenditureManager()
    data = {"日期":"20250301", "金额":-6, "支付通道":"支付宝", "说明":"晚餐"}
    data2 = {"日期": "20250303", "金额": -12, "支付通道": "支付宝", "说明": "晚餐"}
    expenditure_manager.add(data)
    expenditure_manager.add(data2)
    expenditure_manager.display()
    expenditure_manager.save()