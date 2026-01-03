import json

def e(path, expenditure_way):
    data = {}
    with open(path, "r", encoding="utf-8") as f:
        elements = json.load(f)
        headers = elements["Header"]
        del headers[2]
    print(f"当前支付通道是{expenditure_way}")
    string = input(f"请分别输入{headers}的内容，输入 # 进入下一个支付通道:")
    if string == '#':
        return '#'
    else:
        string = string.strip().split()
        for i in range(len(headers)):
            data[headers[i]] = string[i]
        data["金额"] = float(data["金额"])
        data["支付通道"] = expenditure_way
        return data



def i(path):
    data = {}
    with open(path, "r", encoding="utf-8") as f:
        elements = json.load(f)
        headers = elements["Header"]
    string = input(f"请分别输入{headers}的内容，输入 # 退出添加:")
    if string == '#':
        return '#'
    else:
        string = string.strip().split()
        for i in range(len(headers)):
            data[headers[i]] = string[i]
        data["金额"] = float(data["金额"])
        return data



def b(path):
    data = {}
    with open(path, "r", encoding="utf-8") as f:
        elements = json.load(f)
        elements = elements["Date"]+elements["Liabilities"]+elements["CurrentAssets"]+elements["NonCurrentAssets"]
    for item in elements:
        if item != '日期':
            data[item] = float(input(f"请输入 {item} 的内容："))
        else:
            data[item] = input(f"请输入 {item} 的内容：")
    return data

if __name__ == "__main__":
    pass
    #a = e("weixin")