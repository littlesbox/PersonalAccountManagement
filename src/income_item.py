class IncomeItem:
    def __init__(self,
                 date=None,
                 amount=None,
                 income_type=None,
                 income_way=None,
                 description=None):
        self.date = date
        self.amount = amount
        self.income_type = income_type
        self.income_way = income_way
        self.description = description

    def set_date(self, date):
        self.date = date

    def set_amount(self, amount):
        self.amount = amount

    def set_income_type(self, income_type):
        self.income_type = income_type

    def set_income_way(self, income_way):
        self.income_way = income_way

    def set_description(self, description):
        self.description = description

    def to_structure(self):
        structed_data = {"日期": self.date,
                         "金额": self.amount,
                         "类别": self.income_type,
                         "收款通道": self.income_way,
                         "说明": self.description}
        return structed_data

    @staticmethod
    def de_structure(data):
        income_item = IncomeItem(data["日期"],
                                 data["金额"],
                                 data["类别"],
                                 data["收款通道"],
                                 data["说明"])
        return income_item

if __name__ == "__main__":
    pass