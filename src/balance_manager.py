from balance_item import BalanceItem
import json

class BalanceManager:
    def __init__(self):
        self.balance = {}
        self.id = 1

    @staticmethod
    def capture_input():
        data = {}
        with open("../table_header/balance.json", "r", encoding="utf-8") as f:
            elements = json.load(f)
            elements = elements["Date"]+elements["Liabilities"]+elements["CurrentAssets"]+elements["NonCurrentAssets"]
        for item in elements:
            data[item] = float(input(f"请输入 {item} 的内容："))
        return data

    def add(self, data):
        self.balance[self.id] = BalanceItem.de_structure(data)
        self.id += 1

    def display(self):
        for key, value in self.balance.items():
            print(f"{key}: {value.to_structure()}")

if __name__ == "__main__":
    balance_manager = BalanceManager()
    data = BalanceManager.capture_input()
    balance_manager.add(data)
    balance_manager.display()