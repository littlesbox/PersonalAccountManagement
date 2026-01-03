from src.balance_item import BalanceItem

class BalanceManager:
    def __init__(self):
        self.balance = {}
        self.bm_id = 1


    def add(self, data):
        self.balance[self.bm_id] = BalanceItem.de_structure(data)
        self.bm_id += 1

    def display(self):
        for key, value in self.balance.items():
            print(f"bm_id:{key} 日期:{value.date}")
            print(f"负债端: {value.l_to_structure()}")
            print(f"流动: {value.ca_to_structure()}")
            print(f"非流动: {value.nca_to_structure()}")

    def delete(self, bm_id):
        self.balance.pop(bm_id)

    def modify(self, bm_id, title, value):
        value1 = value
        value = float(value)
        match title:
            case '日期':
                self.balance[bm_id].set_date(value1)
            case '花呗':
                self.balance[bm_id].set_huabei(value)
            case '白条':
                self.balance[bm_id].set_baitiao(value)
            case '抖音月付':
                self.balance[bm_id].set_douyinyuefu(value)
            case '美团月付':
                self.balance[bm_id].set_meituanyuefu(value)
            case '抖音放心借':
                self.balance[bm_id].set_douyinfangxinjie(value)
            case '微信':
                self.balance[bm_id].set_weixin(value)
            case '余额宝':
                self.balance[bm_id].set_yu_e_bao(value)
            case '浦发':
                self.balance[bm_id].set_pufa(value)
            case '工商':
                self.balance[bm_id].set_gongshang(value)
            case '建行':
                self.balance[bm_id].set_jianhang(value)
            case '农信':
                self.balance[bm_id].set_nongxin(value)
            case '光大':
                self.balance[bm_id].set_guangda(value)
            case '京东钱包':
                self.balance[bm_id].set_jingdongqianbao(value)
            case '定期存款':
                self.balance[bm_id].set_dinqicunkuan(value)
            case '理财投资':
                self.balance[bm_id].set_licaitouzi(value)
            case '借出':
                self.balance[bm_id].set_jiechu(value)

if __name__ == "__main__":
    balance_manager = BalanceManager()
    data= {'日期':'20250303','花呗': 0, '白条': 0, '抖音月付': 0,
           '美团月付': 0, '抖音放心借': 0, '微信': 0, 
           '余额宝': 0, '浦发': 0, '工商': 0, '建行': 0, 
           '农信': 0, '光大': 0, '京东钱包': 0, '定期存款': 0, 
           '理财投资': 0, '借出': 0}
    balance_manager.add(data)
    balance_manager.display()