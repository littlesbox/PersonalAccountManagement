import json
import re

def e(path, expenditure_way):
    data = {}
    with open(path, "r", encoding="utf-8") as f:
        elements = json.load(f)
        headers = elements["Header"]
        del headers[2]
    print(f"\n当前支付通道是{expenditure_way}")
    string = input(f"\n请分别输入{headers}的内容，例如，“20260301 -9 早餐”,"
                   f"\n注意金额请输入负值，输入 # 进入下一个支付通道:")
    if string == '#':
        return '#'
    else:
        string = string.strip()
        m = re.match(r"^\d{8} -\d+\.?\d* .+$", string)
        if m is not None:
            string = string.split()
            for i in range(len(headers)):
                data[headers[i]] = string[i]
            data["金额"] = float(data["金额"])
            data["支付通道"] = expenditure_way
            return data
        else:
            return data




def i(path):
    data = {}
    with open(path, "r", encoding="utf-8") as f:
        elements = json.load(f)
        headers = elements["Header"]
    string = input(f"\n请分别输入{headers}的内容，例如，“20260105 1000 收入 浦发银行卡 1月份工资”"
                   f"\n注意金额请输入正值，输入 # 退出添加:")
    if string == '#':
        return '#'
    else:
        string = string.strip()
        m = re.match(r"^\d{8} \d+\.?\d* .+ .+ .+$", string)
        if m is not None:
            string = string.split()
            for i in range(len(headers)):
                data[headers[i]] = string[i]
            data["金额"] = float(data["金额"])
            return data
        else:
            return data



def b(path):
    data = {}
    with open(path, "r", encoding="utf-8") as f:
        elements = json.load(f)

    for item in elements["Date"]:
        while True:
            string = input(f"\n请输入 {item} 的内容：")
            string = string.strip()
            m = re.match(r"^\d{8}$", string)
            if m is not None:
                data[item] = string
                break
            else:
                print('\n输入日期格式有误，请输入正确格式，例如，20260101')

    for item in elements["Liabilities"]:
        while True:
            string = input(f"\n请输入 {item} 的内容：")
            string = string.strip()
            m = re.match(r"^-\d+\.?\d*$", string)
            n = re.match(r"^0$", string)
            if m is not None:
                data[item] = float(string)
                break
            elif n is not None:
                data[item] = float(string)
                break
            else:
                print('\n输入内容有误，请输入数字，注意负债类应输入负数')

    for item in elements["CurrentAssets"]+elements["NonCurrentAssets"]:
        while True:
            string = input(f"\n请输入 {item} 的内容：")
            string = string.strip()
            m = re.match(r"^\d+\.?\d*$", string)
            if m is not None:
                data[item] = float(string)
                break
            else:
                print('\n输入内容有误，请输入数字，注意资产类应输入正数')

    return data

if __name__ == "__main__":
    pass
