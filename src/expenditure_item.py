class ExpenditureItem:
    def __init__(self,
                 date=None,
                 amount=None,
                 expenditure_way=None,
                 description=None):
        self.date = date
        self.amount = amount
        self.expenditure_way = expenditure_way
        self.description = description

    def set_date(self, date):
        self.date = date

    def set_amount(self, amount):
        self.amount = amount

    def set_expenditure_way(self, expenditure_way):
        self.expenditure_way = expenditure_way

    def set_description(self, description):
        self.description = description

    def to_structure(self):
        structed_data = {"日期": self.date,
                         "金额": self.amount,
                         "支付通道": self.expenditure_way,
                         "说明": self.description}
        return structed_data

    @staticmethod
    def de_structure(data):
        expenditure_item = ExpenditureItem(data["日期"],
                                           data["金额"],
                                           data["支付通道"],
                                           data["说明"])
        return expenditure_item

if __name__ == "__main__":
    a = ExpenditureItem('20250301',-9,'微信','早餐')
    a_structure = a.to_structure()
    a.set_expenditure_way('zhifubao')
    print(a.to_structure())
    b=ExpenditureItem.de_structure(a_structure)
    print(b.to_structure())