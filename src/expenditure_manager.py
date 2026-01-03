from expenditure_item import ExpenditureItem
import json

class ExpenditureManager:
    def __init__(self):
        self.expenditure = {}
        self.id = 1

    @staticmethod
    def capture_input():
        data = {}
        with open("../table_header/expenditure.json", "r", encoding="utf-8") as f:
            elements = json.load(f)
            elements = elements["Header"]
        string = input(f"请分别输入{elements}的内容：")
        string = string.strip().split()
        for i in range(len(elements)):
            data[elements[i]] = string[i]
        data["金额"] = float(data["金额"])
        return data

    def add(self):
        data = ExpenditureManager.capture_input()
        self.expenditure[self.id] = ExpenditureItem.de_structure(data)
        self.id += 1

    def display(self):
        for key, value in self.expenditure.items():
            print(f"{key}: {value.to_structure()}")

if __name__ == '__main__':
    expenditure_manager = ExpenditureManager()
    expenditure_manager.add()
    expenditure_manager.display()