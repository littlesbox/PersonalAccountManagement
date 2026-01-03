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
            elements = json.load(f)
            elements = elements["Header"]
        string = input(f"请分别输入{elements}的内容：")
        string = string.strip().split()
        for i in range(len(elements)):
            data[elements[i]] = string[i]
        data["金额"] = float(data["金额"])
        return data

    def add(self):
        data = IncomeManager.capture_input()
        self.income[self.id] = IncomeItem.de_structure(data)
        self.id += 1

    def display(self):
        for key, value in self.income.items():
            print(f"{key}: {value.to_structure()}")

if __name__ == '__main__':
    income_manager = IncomeManager()
    income_manager.add()
    income_manager.display()