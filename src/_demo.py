import json

with open("../table_header/balance.json", "r", encoding="utf-8") as f:
    config = json.load(f)
    config = config["Liabilities"] + config["CurrentAssets"] + config["NonCurrentAssets"]

# print(config)


def capture_input():
    data = {}
    with open("../table_header/balance.json", "r", encoding="utf-8") as f:
        elements = json.load(f)
        elements = elements["Liabilities"] + elements["CurrentAssets"] + elements["NonCurrentAssets"]
    for item in elements:
        data[item] = input(f"请输入 {item} 的金额：")
    return data

data = capture_input()