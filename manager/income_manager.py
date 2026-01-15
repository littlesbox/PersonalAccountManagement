import pandas as pd
from pathlib import Path
import os

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
        output_dir = base_dir.joinpath("bill_data", "income.csv")
        df = pd.DataFrame.from_dict(self.income, orient="index")
        df["日期"] = pd.to_datetime(df["日期"], format="%Y%m%d")
        df = df.sort_values("日期")
        df['日期'] = df['日期'].dt.strftime('%Y-%m-%d')
        if os.path.exists(output_dir):
            csv_header = pd.read_csv(output_dir, nrows=0).columns.tolist()
            df = df.reindex(columns=csv_header)
            df.to_csv(
                output_dir,
                mode='a',
                header=False,
                index=False,
                encoding="utf-8-sig"
            )
        else:
            df.to_csv(
                output_dir,
                mode='w',
                header=True,
                index=False,
                encoding="utf-8-sig"
            )

    def is_empty(self):
        if len(self.income) == 0:
            return True
        else:
            return False

    def get_ids(self):
        return list(self.income.keys())

    def get_header(self, im_id):
        return list(self.income[im_id].keys())

    def count(self):
        return len(self.income)

    def classification(self):
        im_class = {}
        for key, value in self.income.items():
            if value['收款通道'] in im_class.keys():
                im_class[value['收款通道']] += 1
            else:
                im_class[value['收款通道']] = 1
        return im_class


if __name__ == '__main__':
    income_manager = IncomeManager()
    data = {"日期":"20500301", "金额":6,"类别":"收入", "收款通道":"浦发银行卡", "说明":"工资"}
    data2 = {"日期": "20500301", "金额": 6, "类别": "收入", "收款通道": "微信", "说明": "工资"}
    income_manager.add(data)
    income_manager.add(data2)
    income_manager.display()
    a = income_manager.classification()
    # income_manager.save()