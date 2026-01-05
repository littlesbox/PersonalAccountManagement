import pandas as pd
from pathlib import Path

class IncomeManager:
    def __init__(self):
        self.income = {}
        self.im_id = 1

    def add(self, data):
        self.income[self.im_id] = data
        self.im_id += 1

    def display(self):
        for key, value in self.income.items():
            print(f"{key}: {value}")

    def delete(self, im_id):
        self.income.pop(im_id)

    def modify(self, im_id, title, value):
        self.income[im_id][title] = value

    def save(self):
        base_dir = Path(__file__).resolve().parent.parent
        output_dir = base_dir.joinpath("tables", "expenditure.csv")
        df = pd.DataFrame.from_dict(self.income, orient="index")
        df["日期"] = pd.to_datetime(df["日期"], format="%Y%m%d")
        df = df.sort_values("日期")
        df.to_csv(output_dir, index=False, encoding="utf-8-sig")


if __name__ == '__main__':
    income_manager = IncomeManager()
    data = {"日期":"20250301", "金额":6,"类别":"收入", "收款通道":"支付宝", "说明":"工资"}
    income_manager.add(data)
    income_manager.display()