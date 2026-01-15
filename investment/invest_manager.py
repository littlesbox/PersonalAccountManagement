import pandas as pd
from pathlib import Path
from datetime import datetime
import json
import re


class InvestManager:
    def __init__(self):
        self.invest = InvestManager.load()
        if self.invest is None:
            self.iv_id = 0
        else:
            self.iv_id = len(self.invest)

    def insert(self):
        base_dir = Path(__file__).resolve().parent.parent
        path = base_dir.joinpath("table_header", "invest.json")
        with open(path, "r", encoding="utf-8") as f:
            content = json.load(f)
        headers = content["Header"]
        while True:
            data = {}
            string = input(f"\n请分别输入{headers}的内容，例如，“工商银行积存金 黄金 10000 10001.1”"
                           f"\n输入 # 结束插入:")
            if string == "#":
                break
            else:
                string = string.strip()
                m = re.match(r"^.+ .+ \d+\.?\d* \d+\.?\d*$", string)
                if m is not None:
                    string = string.split()
                    for i in range(len(headers)):
                        data[headers[i]] = string[i]
                    data["金额"] = float(data["金额"])
                    data["现值"] = float(data["现值"])
                    invest_dict = {self.iv_id: data}
                    new = pd.DataFrame.from_dict(invest_dict, orient="index")
                    self.iv_id += 1
                    self.invest = pd.concat([self.invest, new])
                else:
                    print('\n输入内容有误，请按照正确格式输入')

    def view(self):
        print('\n')
        print(self.invest)

    def remove(self):
        iv_id = int(input("\n请输入想要删除数据的 id:"))
        index_list = self.invest.index.tolist()
        if iv_id in index_list:
            self.invest = self.invest.drop(iv_id)
        else:
            print('\n不存在该条数据，请输入正确的id')

    def update(self):
        iv_id = int(input("\n请输入想要更新的数据的 id:"))
        index_list = self.invest.index.tolist()
        if iv_id in index_list:
            title = input('\n请选择想要修改数据的字段:')
            title_list = self.invest.columns.tolist()
            if title in title_list:
                if title == '金额' or title == '现值':
                    while True:
                        value = input('\n请输入新值:')
                        m = re.match(r"^\d+\.?\d*$", value)
                        if m is not None:
                            self.invest.at[iv_id, title] = float(value)
                            break
                        else:
                            print('\n请输入数字')
                else:
                    value = input('\n请输入新值:')
                    self.invest.at[iv_id, title] = value
            else:
                print('\n不存在该字段，请输入正确的字段')
        else:
            print('\n不存在该条数据，请输入正确的id')

    def store(self):
        while True:
            name = input('\n请输入日期:')
            m = re.match(r"^\d{8}$", name)
            if m is not None:
                base_dir = Path(__file__).resolve().parent.parent
                output_dir = base_dir.joinpath("investment_data", name+".csv")
                self.invest.to_csv(output_dir, index=False, encoding="utf-8-sig")
                break
            else:
                print('\n请输入正确的日期格式，例如“20260101”')

    @staticmethod
    def load():
        base_dir = Path(__file__).resolve().parent.parent
        path = base_dir.joinpath("investment_data")
        no_file = not any(path.iterdir())
        if no_file:
            return None
        else:
            filename = sorted(
                (
                    p.stem
                    for p in path.iterdir()
                    if p.is_file() and len(p.stem) == 8 and p.stem.isdigit()
                ),
                key=lambda s: datetime.strptime(s, "%Y%m%d"),
                reverse=True
            )
            invest_df = pd.read_csv(path.joinpath(filename[0]+".csv"))
            return invest_df

if __name__ == '__main__':
    invest_manager = InvestManager()
    while True:
        prompt = input('\n请选择操作(insert/remove/update/view/store):')
        if prompt == "insert":
            invest_manager.insert()
        elif prompt == "view":
            invest_manager.view()
        elif prompt == "remove":
            invest_manager.remove()
        elif prompt == "update":
            invest_manager.update()
        elif prompt == "store":
            invest_manager.store()
        else:
            print('\n未知命令请重新输入\n')

