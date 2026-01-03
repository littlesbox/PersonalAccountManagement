from src.expenditure_item import ExpenditureItem

class ExpenditureManager:
    def __init__(self):
        self.expenditure = {}
        self.em_id = 1

    def add(self, data):
        self.expenditure[self.em_id] = ExpenditureItem.de_structure(data)
        self.em_id += 1

    def display(self):
        for key, value in self.expenditure.items():
            print(f"{key}: {value.to_structure()}")

    def delete(self, em_id):
        self.expenditure.pop(em_id)

    def modify(self, em_id, title, value):
        match title:
            case "日期":
                self.expenditure[em_id].set_date(value)
            case "金额":
                self.expenditure[em_id].set_amount(float(value))
            case "支付通道":
                self.expenditure[em_id].set_expenditure_way(value)
            case "说明":
                self.expenditure[em_id].set_description(value)

if __name__ == '__main__':
    expenditure_manager = ExpenditureManager()
    data = {"日期":"20250301", "金额":-6, "支付通道":"支付宝", "说明":"晚餐"}
    expenditure_manager.add(data)
    expenditure_manager.display()