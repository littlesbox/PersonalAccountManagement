import pandas as pd
from pathlib import Path
import os

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
        output_dir = base_dir.joinpath("bill_data", "expenditure.csv")
        df = pd.DataFrame.from_dict(self.expenditure, orient="index")
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
        if len(self.expenditure) == 0:
            return True
        else:
            return False

    def get_ids(self):
        return list(self.expenditure.keys())

    def get_header(self, em_id):
        return list(self.expenditure[em_id].keys())

    def count(self):
        return len(self.expenditure)

    def classification(self):
        em_class = {}
        for key, value in self.expenditure.items():
            if value['支付通道'] in em_class.keys():
                em_class[value['支付通道']] += 1
            else:
                em_class[value['支付通道']] = 1
        return em_class




if __name__ == '__main__':
    expenditure_manager = ExpenditureManager()
    data = {"日期":"20500301", "金额":-6, "支付通道":"支付宝", "说明":"晚餐"}
    data2 = {"日期": "20500303", "金额": -12, "支付通道": "微信", "说明": "晚餐"}
    expenditure_manager.add(data)
    expenditure_manager.add(data2)
    expenditure_manager.display()
    a = expenditure_manager.classification()
    # expenditure_manager.save()