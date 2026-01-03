from src.income_item import IncomeItem


class IncomeManager:
    def __init__(self):
        self.income = {}
        self.im_id = 1

    def add(self, data):
        self.income[self.im_id] = IncomeItem.de_structure(data)
        self.im_id += 1

    def display(self):
        for key, value in self.income.items():
            print(f"{key}: {value.to_structure()}")

    def delete(self, im_id):
        self.income.pop(im_id)

    def modify(self, im_id, title, value):
        match title:
            case '日期':
                self.income[im_id].set_date(value)
            case '金额':
                self.income[im_id].set_amount(float(value))
            case '类别':
                self.income[im_id].set_income_type(value)
            case '收款通道':
                self.income[im_id].set_income_way(value)
            case '工资':
                self.income[im_id].set_description(value)

if __name__ == '__main__':
    income_manager = IncomeManager()
    data = {"日期":"20250301", "金额":6,"类别":"收入", "收款通道":"支付宝", "说明":"工资"}
    income_manager.add(data)
    income_manager.display()