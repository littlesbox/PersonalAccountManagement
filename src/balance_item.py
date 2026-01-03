class BalanceItem:
    def __init__(self,
                 date = None,
                 huabei=0,
                 baitiao=0,
                 douyinyuefu=0,
                 meituanyuefu=0,
                 douyinfangxinjie=0,
                 weixin=0,
                 yu_e_bao=0,
                 pufa=0,
                 gongshang=0,
                 jianhang=0,
                 nongxin=0,
                 guangda=0,
                 jingdongqianbao=0,
                 dinqicunkuan=0,
                 licaitouzi=0,
                 jiechu=0):
        self.date = date
        self.huabei = huabei
        self.baitiao = baitiao
        self.douyinyuefu = douyinyuefu
        self.meituanyuefu = meituanyuefu
        self.douyinfangxinjie = douyinfangxinjie
        self.weixin = weixin
        self.yu_e_bao = yu_e_bao
        self.pufa = pufa
        self.gongshang = gongshang
        self.jianhang = jianhang
        self.nongxin = nongxin
        self.guangda = guangda
        self.jingdongqianbao = jingdongqianbao
        self.dinqicunkuan = dinqicunkuan
        self.licaitouzi = licaitouzi
        self.jiechu = jiechu

    def set_date(self, date):
        self.date = date

    def set_huabei(self, amount):
        self.huabei = amount

    def set_baitiao(self, amount):
        self.baitiao = amount

    def set_douyinyuefu(self, amount):
        self.douyinyuefu = amount

    def set_meituanyuefu(self, amount):
        self.meituanyuefu = amount

    def set_douyinfangxinjie(self, amount):
        self.douyinfangxinjie = amount

    def set_weixin(self, amount):
        self.weixin = amount

    def set_yu_e_bao(self, amount):
        self.yu_e_bao = amount

    def set_pufa(self, amount):
        self.pufa = amount

    def set_gongshang(self, amount):
        self.gongshang = amount

    def set_jianhang(self, amount):
        self.jianhang = amount

    def set_nongxin(self, amount):
        self.nongxin = amount

    def set_guangda(self, amount):
        self.guangda = amount

    def set_jingdongqianbao(self, amount):
        self.jingdongqianbao = amount

    def set_dinqicunkuan(self, amount):
        self.dinqicunkuan = amount

    def set_licaitouzi(self, amount):
        self.licaitouzi = amount

    def set_jiechu(self, amount):
        self.jiechu = amount

    def to_structure(self):
        structed_data = {"日期": self.date,
                         "花呗": self.huabei,
                         "白条": self.baitiao,
                         "抖音月付": self.douyinyuefu,
                         "美团月付": self.meituanyuefu,
                         "抖音放心借": self.douyinfangxinjie,
                         "微信": self.weixin,
                         "余额宝": self.yu_e_bao,
                         "浦发": self.pufa,
                         "工商": self.gongshang,
                         "建行": self.jianhang,
                         "农信": self.nongxin,
                         "光大": self.guangda,
                         "京东钱包": self.jingdongqianbao,
                         "定期存款": self.dinqicunkuan,
                         "理财投资": self.licaitouzi,
                         "借出": self.jiechu}
        return structed_data

    @staticmethod
    def de_structure(data):
        balance_item = BalanceItem(data["日期"],
                                   data["花呗"],
                                   data["白条"],
                                   data["抖音月付"],
                                   data["美团月付"],
                                   data["抖音放心借"],
                                   data["微信"],
                                   data["余额宝"],
                                   data["浦发"],
                                   data["工商"],
                                   data["建行"],
                                   data["农信"],
                                   data["光大"],
                                   data["京东钱包"],
                                   data["定期存款"],
                                   data["理财投资"],
                                   data["借出"])
        return balance_item

if __name__ == "__main__":
    a = BalanceItem(weixin=5)
    print(a.to_structure())