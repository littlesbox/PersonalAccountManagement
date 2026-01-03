from income_item import IncomeItem
import json

class IncomeManager:
    def __init__(self):
        self.income = {}
        self.id = 1

    @staticmethod
    def capture_input():
        data = {}
        with open("../table_header/income.json", "r", encoding="utf-8") as f:
            config = json.load(f)
            headers = config["Header"]
        string = input(f"请分别输入{headers}的内容：")
        string = string.strip().split()
        for i in range(len(headers)):
            data[headers[i]] = string[i]
        data["金额"] = float(data["金额"])
        return data

    def add(self, data):
        self.income[self.id] = IncomeItem.de_structure(data)
        self.id += 1

    def display(self):
        for key, value in self.income.items():
            print(f"{key}: {value.to_structure()}")

if __name__ == '__main__':
    income_manager = IncomeManager()
    data = IncomeManager.capture_input()
    income_manager.add(data)
    income_manager.display()